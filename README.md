# OUI_lookup_api
## つかいかた
1. FastAPIとuvicornをインストールする
1. uvicorn api:app --reloadする
1. http://[サーバのIP]:8000/[OUI] を叩く (例：MACアドレスがF4:BD:9E:04:F1:5Dの場合、OUI = F4BD9Eと入力)
1. 結果にコミットされます(例：{"company_name":"Cisco Systems, Inc","address_line":"80 West Tasman Drive","region":"San Jose  CA  94568","country":"US"}と返ってくる)

## api.py
MACアドレスのOUI(Organizationally Unique Identifier)からベンダ名と所在地を返すFastAPI製のWeb API

## generate_oui_json.py
IEEE発行の[oui.txt](https://standards-oui.ieee.org/oui/oui.txt)をapi.pyで扱いやすいようにjsonファイルに変換するスクリプト
