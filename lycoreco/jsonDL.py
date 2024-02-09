import requests
import json
import base64

# APIエンドポイントのURL
url = "https://www.onsen.ag/web_api/programs/lycoris-recoil"

# APIからデータを取得
response = requests.get(url)

# JSON形式で保存
with open("lycoreco.json", "w") as f:
    json.dump(response.json(), f)
