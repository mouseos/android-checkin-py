from checkin_pb2 import AndroidCheckinRequest,GservicesSetting
from logs_pb2 import AndroidCheckinProto,AndroidBuildProto,AndroidEventProto,AndroidStatisticProto,AndroidIntentProto
from config_pb2 import DeviceConfigurationProto
import time
import requests
import gzip
from io import BytesIO
android_checkin_request= AndroidCheckinRequest()
gservices_setting = GservicesSetting()
android_checkin_proto = AndroidCheckinProto()
android_build_proto = AndroidBuildProto()
android_event_proto = AndroidEventProto()
android_statistic_proto = AndroidStatisticProto()
android_intent_proto = AndroidIntentProto()
device_configution_proto = DeviceConfigurationProto()

# 値をセット
android_checkin_request.id=0
android_checkin_request.digest= "1-da39a3ee5e6b4b0d3255bfef95601890afd80709" 
android_build_proto.id="Fairphone/FP3/FP3:9/8901.2.A.0105.20191217/12171325:user/release-keys"

#　バイナリデータに変換
result_bytes = android_checkin_request.SerializeToString()
# Gzip圧縮
compressed_data = gzip.compress(result_bytes)

# https://android.clients.google.com/checkinにPOSTリクエストを送信
checkin_url = "https://android.clients.google.com/checkin"

try:
    headers = {'Content-Encoding': 'gzip', 'Content-Type': 'application/x-protobuf'}
    response = requests.post(checkin_url, data=compressed_data, headers=headers,verify=False)
    if response.status_code == 200:
        print("Check-in 成功!")
        # パースする
        response_proto = AndroidCheckinProto()
        response_proto.ParseFromString(response.content)
    else:
        print(f"Check-in 失敗　status code {response.status_code}")
except requests.RequestException as e:
    print(f"check-in中にエラーが発生: {str(e)}")