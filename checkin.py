from checkin_pb2 import AndroidCheckinRequest,AndroidCheckinResponse,GservicesSetting
from logs_pb2 import AndroidCheckinProto,AndroidBuildProto,AndroidEventProto,AndroidStatisticProto,AndroidIntentProto
from config_pb2 import DeviceConfigurationProto
import sys
import requests
import gzip
import json
from io import BytesIO
from pprint import pprint
from urllib3.exceptions import InsecureRequestWarning

def get_update_url(fingerprint,device):
    if(fingerprint=="" or device==""):
        print("引数を正しく入力してください。")
        return None
    android_checkin_request= AndroidCheckinRequest()
    android_checkin_respoonse= AndroidCheckinResponse()
    gservices_setting = GservicesSetting()
    android_checkin_proto = AndroidCheckinProto()
    android_build_proto = AndroidBuildProto()
    android_event_proto = AndroidEventProto()
    android_statistic_proto = AndroidStatisticProto()
    android_intent_proto = AndroidIntentProto()
    device_configution_proto = DeviceConfigurationProto()


    '''
    message AndroidCheckinRequest {
    optional string imei = 1;
    optional int64 id = 2;
    optional string digest = 3;
    optional AndroidCheckinProto checkin = 4;
    optional string desiredBuild = 5;
    optional string locale = 6;
    optional int64 loggingId = 7;
    optional string marketCheckin = 8;
    repeated string macAddr = 9;
    optional string meid = 10;
    repeated string accountCookie = 11;
    optional string timeZone = 12;
    optional fixed64 securityToken = 13;
    optional int32 version = 14;
    repeated string otaCert = 15;
    optional string serialNumber = 16;
    optional string esn = 17;
    optional DeviceConfigurationProto deviceConfiguration = 18;
    repeated string macAddrType = 19;
    optional int32 fragment = 20;
    optional string userName = 21;
    }
    '''
    # 値をセット
    #android_checkin_request.id=0
    android_checkin_request.digest= "1-da39a3ee5e6b4b0d3255bfef95601890afd80709"  #値は何でもよい
    #android_checkin_request.locale="ja_JP"
    #android_checkin_request.loggingId=0
    #android_checkin_request.marketCheckin=""
    #android_checkin_request.macAddr=[]
    #android_checkin_request.meid=""
    #android_checkin_request.accountCookie=[]
    #android_checkin_request.timeZone="America/New_York"
    #android_checkin_request.securityToken=0
    android_checkin_request.version=3 #2 or 3
    #android_checkin_request.otaCert.extend(["+eBjakVbKgvqGgpzlIx35lE6iiM="])
    #android_checkin_request.serialNumber=""
    #android_checkin_request.esn=""
    #android_checkin_request.deviceConfiguration=null
    #android_checkin_request.macAddrType=[]
    #android_checkin_request.fragment=0
    #android_checkin_request.userName=""
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
    android_build_proto.id=fingerprint
    #android_build_proto.product="qcom"
    #android_build_proto.carrier="Fairphone"
    #android_build_proto.radio=".TA.3.0.c1-00565-8953_GEN_PACK-1,.TA.3.0.c1-00565-8953_GEN_PACK-1"
    #android_build_proto.bootloader="unknown"
    #android_build_proto.client="android-uniscope"
    android_build_proto.timestamp=0 #元の値は1576561122だったがそれ以下の値でも動く
    #android_build_proto.googleServices=19275037 
    android_build_proto.device=device
    #android_build_proto.sdkVersion=28
    #android_build_proto.model="FP3"
    #android_build_proto.manufacturer="Fairphone"
    #android_build_proto.buildProduct="FP3"
    #android_build_proto.otaInstalled=False

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
    #android_checkin_proto.lastCheckinMsec=0
    #android_checkin_proto.event.extend([])
    #android_checkin_proto.stat.extend([])
    #android_checkin_proto.requestedGroup.extend([])
    #android_checkin_proto.cellOperator=""
    #android_checkin_proto.simOperator=""
    #android_checkin_proto.roaming=""
    #android_checkin_proto.userNumber=0

    android_checkin_request.checkin.MergeFrom(android_checkin_proto)

    #　バイナリデータに変換
    result_bytes = android_checkin_request.SerializeToString()
    # Gzip圧縮
    compressed_data = gzip.compress(result_bytes)

    # https://android.clients.google.com/checkinにPOSTリクエストを送信
    checkin_url = "https://android.clients.google.com/checkin"

    try:
        headers = {'Content-Encoding': 'gzip', 'Content-Type': 'application/x-protobuf'}
 
        # 警告を非表示
        requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
        response = requests.post(checkin_url, data=compressed_data, headers=headers,verify=False)
        if response.status_code == 200:
            #print("Succeed Check-in")
            # パースする
            response_proto = AndroidCheckinResponse()
            response_proto.ParseFromString(response.content)
            result={'fingerprint':fingerprint,'device':device,'description':"","title":"",'url':""}
            for data in response_proto.setting:
                if((data.name.decode('utf-8'))=="update_url"):
                    '''
                    print("OTA Update file")
                    print("============================================================================================")
                    print("Build:"+android_build_proto.id)
                    print("URL:"+data.value.decode('utf-8'))
                    '''
                    
                    result["url"]=data.value.decode('utf-8')
                if((data.name.decode('utf-8'))=="update_description"):
                    result["description"]=data.value.decode('utf-8')
                if((data.name.decode('utf-8'))=="update_title"):
                    result["title"]=data.value.decode('utf-8')
            if(len(result["url"])!=0):
                return(result)
            else:
                return(None)
        else:
            print(f"Check-in Failure:\nStatusCode: {response.status_code}")
    except requests.RequestException as e:
        print(f"FAILURE CHECK-IN:\n{str(e)}")


#アップデートURLを取得
#pprint(get_update_url("Fairphone/FP3/FP3:9/8901.2.A.0105.20191217/12171325:user/release-keys","FP3"))
#pprint(get_update_url("benesse/TAB-A05-BD/TAB-A05-BD:9/01.00.000/01.00.000:user/release-keys","TAB-A05-BD"))
if __name__=="__main__":
    if not len(sys.argv) == 3:
        print()
        print("Use: python3 " + sys.argv[0] + " [ro.build.fingerprint] [ro.product.model]")
        print()
        sys.exit(1)
    print(json.dumps(get_update_url(sys.argv[1],sys.argv[2]), indent=2, sort_keys=True))
