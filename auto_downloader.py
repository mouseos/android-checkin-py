import sys
import os
import shutil
import zipfile
import subprocess
from urllib.parse import urlparse
import re

# Assuming checkin.py is in the same directory
import checkin
import requests
requests.packages.urllib3.disable_warnings()

def sanitize_filename(filename):
    """Replace invalid characters in a filename with underscores."""
    return re.sub(r'[\\/*?:"<>|]', "_", filename)

def download_file(url, destination, downloader="aria2c", num_connections=16):
    """Downloads a file using aria2c."""
    try:
        if downloader == "aria2c":
            command = [
                "aria2c",
                "--continue=true",  # Continue partial downloads
                f"--max-connection-per-server={num_connections}",
                "--split=16",
                "--min-split-size=1M",
                f"--out={destination}",
                url,
            ]
        else:
            raise ValueError("Invalid downloader specified. Only 'aria2c' is supported.")

        subprocess.run(command, check=True, capture_output=False, text=False)
        print(f"Download complete: {destination}")

    except subprocess.CalledProcessError as e:
        print(f"Error during download: {e}")
        sys.exit(1)
    except FileNotFoundError:
        print(f"Downloader aria2c not found.  Please install it.")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)



def auto_download(fingerprint, model):
    """
    Automatically downloads and extracts OTA updates.
    """

    while fingerprint:
        update_info = checkin.get_update_url(fingerprint, model)

        if not update_info:
            print("No further updates found.")
            break

        # 1. Prepare tmp directory
        if os.path.exists("tmp"):
            shutil.rmtree("tmp")
        os.makedirs("tmp")

        # 2. Save update information (description)
        description_html = f"<!DOCTYPE html><html><head><title>{update_info['title']}</title></head><body>{update_info['description']}</body></html>"
        with open("tmp/description.html", "w", encoding="utf-8") as f:
            f.write(description_html)


        # 3. Download the update file.  *Before* determining the output dir.
        download_file(update_info['url'], os.path.join("tmp", "temp.zip"))  # Temporary name

        # 4. Extract *only* metadata
        with zipfile.ZipFile(os.path.join("tmp", "temp.zip"), 'r') as zip_ref:
            try:
                zip_ref.extract("META-INF/com/android/metadata", "tmp")
            except KeyError:
                print("META-INF/com/android/metadata not found in the ZIP file.")
                shutil.rmtree("tmp")
                sys.exit(1)
        shutil.copy("tmp/META-INF/com/android/metadata", "tmp/metadata.txt")

        # 5.  Determine output directory name (and ZIP filename) *from metadata*
        with open("tmp/metadata.txt", "r", encoding="utf-8") as f:
             metadata_content = f.read()
        metadata_lines = metadata_content.splitlines()

        post_build = None
        for line in metadata_lines:
            if line.startswith("post-build="):
                post_build = line.split("=")[1].strip()
                break
        if not post_build:
            print("post-build not found in metadata.txt")
            shutil.rmtree("tmp")
            sys.exit(1)

        zip_filename_base = sanitize_filename(post_build)
        zip_filename = f"{zip_filename_base}.zip"
        output_dir = os.path.join("out", zip_filename_base)


        # 6. Update metadata (add url)
        with open("tmp/metadata.txt", "a", encoding="utf-8") as f:
            f.write(f"url={update_info['url']}\n")

        # 7. Create output directory
        if not os.path.exists("out"):
            os.makedirs("out")
        os.makedirs(output_dir, exist_ok=True)

        # 8. Move files, renaming the ZIP file
        shutil.move("tmp/description.html", os.path.join(output_dir, "description.html"))
        shutil.move(os.path.join("tmp", "temp.zip"), os.path.join(output_dir, zip_filename)) # Rename
        shutil.move("tmp/metadata.txt", os.path.join(output_dir, "metadata.txt"))


        # 9. Prepare for the next iteration (recursive call)
        fingerprint = post_build  # Use the extracted post_build
        # model remains the same

        # Clean up the tmp directory
        shutil.rmtree("tmp")



if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python auto_download.py <ro.build.fingerprint> <ro.product.model>")
        sys.exit(1)

    fingerprint = sys.argv[1]
    model = sys.argv[2]

    auto_download(fingerprint, model)