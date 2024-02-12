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

'''
message AndroidBuildProto {
  optional string id = 1;
  optional string product = 2;
  optional string carrier = 3;
  optional string radio = 4;
  optional string bootloader = 5;
  optional string client = 6;
  optional int64 timestamp = 7;
  optional int32 googleServices = 8;
  optional string device = 9;
  optional int32 sdkVersion = 10;
  optional string model = 11;
  optional string manufacturer = 12;
  optional string buildProduct = 13;
  optional bool otaInstalled = 14;
}

'''
#AndroidBuildProtoの値をセット
android_build_proto.id="Fairphone/FP3/FP3:9/8901.2.A.0105.20191217/12171325:user/release-keys"
android_build_proto.product="qcom"
android_build_proto.carrier="Fairphone"
android_build_proto.radio=".TA.3.0.c1-00565-8953_GEN_PACK-1,.TA.3.0.c1-00565-8953_GEN_PACK-1"
android_build_proto.bootloader="unknown"
android_build_proto.client="android-uniscope"
android_build_proto.timestamp=1576561122 
android_build_proto.googleServices=19275037 
android_build_proto.device="FP3"
android_build_proto.sdkVersion=28
android_build_proto.model="FP3"
android_build_proto.manufacturer="Fairphone"
android_build_proto.buildProduct="FP3"
android_build_proto.otaInstalled=False

'''
message AndroidCheckinProto {
  optional AndroidBuildProto build = 1;
  optional int64 lastCheckinMsec = 2;
  repeated AndroidEventProto event = 3;
  repeated AndroidStatisticProto stat = 4;
  repeated string requestedGroup = 5;
  optional string cellOperator = 6;
  optional string simOperator = 7;
  optional string roaming = 8;
  optional int32 userNumber = 9;
}
'''
android_checkin_proto.build.MergeFrom(android_build_proto)
android_checkin_proto.lastCheckinMsec=0
#android_checkin_proto.event.extend([])
#android_checkin_proto.stat.extend([])
#android_checkin_proto.requestedGroup.extend([])
#android_checkin_proto.cellOperator=""
#android_checkin_proto.simOperator=""
#android_checkin_proto.roaming=""
#android_checkin_proto.userNumber=0
#19: "2019-12-05"を入れたいがなぜか19番がない

android_checkin_request.checkin.MergeFrom(android_checkin_proto)


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