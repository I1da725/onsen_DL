import requests
import json
import csv
import os
import ffmpeg
import re

#_session_id はpremiumでログインしたブラウザのクッキーから取得
#============変更部================
radioPara = "lycoris-recoil"
radioTitle = "リコラジ"
workTitle = "lycoreco"
artist = "古賀葵,山根綺"
album_artist = "古賀葵,山根綺"
album = "16bit_radio"
CK = {"_session_id" : ""}
#=================================

my_Table = [["title","delivery_date","streaming_url","poster_image_url", "output_m4a"]]
tsfalder = "./output_ts/"
m4afalder = "./output_m4a/"
tstail = ".ts"
m4atail = ".m4a"
#APIエンドポイントのURL
url = "https://www.onsen.ag/web_api/programs/{}".format(radioPara) 

# APIからデータを取得
response = requests.get(url, cookies = CK)

# JSON形式で取得データを保存
with open("{}.json".format(workTitle), "w") as f:
    json.dump(response.json(), f, ensure_ascii=False)

#.tsファイル出力先フォルダの存在確認と作成
is_dir = os.path.isdir(tsfalder)
if is_dir:
    print(f"{tsfalder} is exist.")
else:
    os.mkdir(tsfalder)
#.m4aファイル出力先フォルダの存在確認と作成
is_dir = os.path.isdir(m4afalder)
if is_dir:
    print(f"{m4afalder} is exist.")
else:
    os.mkdir(m4afalder)

#jsonファイルをリスト形式に変換　./output/radioTitle"title".ts | 日付 | streaming_url | poster_image_url
with open("{}.json".format(workTitle)) as f:
    D_json = json.load(f)
for num in D_json["contents"]:
    my_Table.append([tsfalder + radioTitle + num["title"] + tstail, num["delivery_date"], num["streaming_url"], num["poster_image_url"], m4afalder + radioTitle + num["title"] + m4atail])
    #ポスター画像の取得
    responseImage = requests.get(num["poster_image_url"])
    posterImage = responseImage.content
    matches = re.findall(r'=(.*)$', num["poster_image_url"])
    if matches:
        result = matches[-1]
        result = result + ".jpeg"
        with open(result, "wb") as f:
            f.write(posterImage)
    else:
        print("error ポスター画像を取得できませんでした。")


#リスト形式からcsvファイルに出力
with open("{}.csv".format(workTitle), 'w') as f:
    # writer = csv.writer(f, delimiter='\t')
    writer = csv.writer(f, delimiter=',')
    writer.writerows(my_Table)

#これ以降はautoDL.commandを実行
#ファイルの実行方法 $./autoDL.command lycoreco.csv
#CSVファイル名を引数として受け取る
os.system("./autoDL.command {}.csv".format(workTitle))

#autoChange.command実行
#ファイルの実行方法 $./autoChange.command ./output_ts/****.ts ./output_m4a/****.m4a
for ts, hoge1, hoge2, hoge3, m4a in my_Table[1:]:
    os.system("./autoChange.command {} {}".format(ts,m4a))

#m4aファイルのメタデータ適用