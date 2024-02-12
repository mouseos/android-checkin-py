from checkin_pb2 import AndroidCheckinRequest,GservicesSetting
from logs_pb2 import AndroidCheckinProto,AndroidBuildProto,AndroidEventProto,AndroidStatisticProto,AndroidIntentProto
from config_pb2 import DeviceConfigurationProto
import time
import requests
import gzip
from io import BytesIO
android_checkin_request= AndroidCheckinRequest()
print(dir(android_checkin_request))
gservices_setting = GservicesSetting()
android_checkin_proto = AndroidCheckinProto()
android_build_proto = AndroidBuildProto()
android_event_proto = AndroidEventProto()
android_statistic_proto = AndroidStatisticProto()
android_intent_proto = AndroidIntentProto()
device_configution_proto = DeviceConfigurationProto()

# 値をセット
android_build_proto.id = "google/yakju/maguro:4.1.1/JRO03C/398337:user/release-keys"
android_build_proto.product = "tuna"
android_build_proto.carrier = "Google"
android_build_proto.radio = "I9250XXLA2"
android_build_proto.bootloader = "PRIMELA03"
android_build_proto.client = "android-google"
android_build_proto.timestamp = int(time.time())
android_build_proto.device = "maguro"
android_build_proto.model = "Galaxy Nexus"
android_build_proto.manufacturer = "Samsung"

#　バイナリデータに変換
result_bytes = android_build_proto.SerializeToString()
# Gzip圧縮
compressed_data = gzip.compress(result_bytes)

# https://android.clients.google.com/checkinにPOSTリクエストを送信
checkin_url = "https://android.clients.google.com/checkin"

try:
    headers = {'Content-Encoding': 'gzip', 'Content-Type': 'application/x-protobuf'}
    response = requests.post(checkin_url, data=compressed_data, headers=headers,verify=False)
    if response.status_code == 200:
        print("Check-in successful!")
        # Parse the response if needed
        response_proto = AndroidCheckinProto()
        response_proto.ParseFromString(response.content)
        # Do something with the response data
    else:
        print(f"Check-in failed with status code {response.status_code}")
except requests.RequestException as e:
    print(f"Error during check-in: {str(e)}")