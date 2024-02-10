import requests
import json
import csv
import os
import ffmpeg

radioPara = "lycoris-recoil"
radioTitle = "リコラジ"
workTitle = "lycoreco"
tail = ".ts"
falder = "./output/"
my_Table = [["title","delivery_date","streaming_url","poster_image_url"]]

url = "https://www.onsen.ag/web_api/programs/{}".format(radioPara) #APIエンドポイントのURL

# APIからデータを取得
response = requests.get(url)
print(type(response))
print(type(response.json()))

# JSON形式で取得データを保存
with open("{}.json".format(workTitle), "w") as f:
    json.dump(response.json(), f, ensure_ascii=False)

#.tsファイル出力先フォルダの存在確認と作成
is_dir = os.path.isdir(falder)
if is_dir:
    print(f"{falder} is exist.")
else:
    os.mkdir(falder)

#jsonファイルをリスト形式に変換　./output/radioTitle"title".ts | 日付 | streaming_url | poster_image_url
with open("{}.json".format(workTitle)) as f:
    D_json = json.load(f)
for num in D_json["contents"]:
    my_Table.append([falder + radioTitle + num["title"] + tail, num["delivery_date"], num["streaming_url"], num["poster_image_url"]])

#リスト形式からcsvファイルに出力
with open("{}.csv".format(workTitle), 'w') as f:
    # writer = csv.writer(f, delimiter='\t')
    writer = csv.writer(f, delimiter=',')
    writer.writerows(my_Table)

#これ以降はautoDL.commandを実行
#ファイルの実行方法 $./autoDL.command lycoreco.csv
#CSVファイル名を引数として受け取る
    
os.system("./autoDL.command {}.csv".format(workTitle))