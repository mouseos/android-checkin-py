# android-checkin-py

Android端末のOTAアップデート情報を取得・ダウンロードするツールです。アップデート情報を取得し、自動的にOTAファイルをダウンロードできます。

## 機能

- **チェックイン機能**: Android端末のfingerprintとモデル名からOTAアップデート情報を取得
- **自動ダウンロード**: 利用可能なアップデートを自動的に検出・ダウンロード
- **連続アップデート**: 複数のアップデートが存在する場合、連続して取得
- **メタデータ保存**: アップデート情報とメタデータを保存

## 必要な環境

- Python 3.x
- aria2c (ダウンロード用)

## インストール

1. リポジトリをクローン:
```bash
git clone https://github.com/mouseos/android-checkin-py
cd android-checkin-py
```

2. 依存関係をインストール:
```bash
pip install -r requirements.txt
```

3. aria2cをインストール:
```bash
# Ubuntu/Debian
sudo apt install aria2

# Windows
aria2c.exeが既に含まれています
```

## 使用方法

### 基本的な使用方法 (checkin.py)

単一のアップデート情報を取得:

```bash
python checkin.py "[ro.build.fingerprint]" "[ro.product.model]"
```

例:
```bash
python checkin.py "Fairphone/FP3/FP3:9/8901.2.A.0105.20191217/12171325:user/release-keys" "FP3"
```

### 自動ダウンロード (auto_downloader.py)

提供されたビルドを起点に利用可能なすべてのアップデートを自動的にダウンロード:

```bash
python auto_downloader.py "[ro.build.fingerprint]" "[ro.product.model]"
```

## 出力形式

### checkin.py
JSON形式でアップデート情報を出力:
```json
{
  "description": "アップデートの説明",
  "device": "デバイス名",
  "fingerprint": "ビルドフィンガープリント",
  "title": "アップデートタイトル",
  "url": "ダウンロードURL"
}
```

### auto_downloader.py
`out/` ディレクトリに以下のファイルを保存:
- `[post-build]/` - アップデートごとのディレクトリ
  - `[post-build].zip` - OTAアップデートファイル
  - `description.html` - アップデート説明
  - `metadata.txt` - メタデータ (URLを含む)

## トラブルシューティング

### "No update found."が表示される場合
- fingerprintまたはモデル名が正しいか確認してください
- 該当するアップデートが存在しない可能性があります
- Google OTAではない独自OTAの可能性があります。

### ダウンロードエラーが発生する場合
- aria2cがインストールされているか確認してください
- ネットワーク接続を確認してください