# android-checkin-py
Google OTAからupdate.zipのURLを取得します。これを用いてファームウェアを取得することで起動不能になった端末を修復できる可能性があります。
```
python ./checkin.py ro.build.fingerprintの値 ro.product.modelの値
```
