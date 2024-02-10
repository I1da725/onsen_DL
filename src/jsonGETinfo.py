import json

with open('lycoreco.json') as f:
    J_dict = json.load(f)

print(J_dict["contents"])

for v in J_dict["contents"]:
    print(v["title"])
    print(v["streaming_url"])
    print(v["delivery_date"])
    print("===================")


##解説
##jsonが階層構造になっているため、構造を把握しづらい
##4行目でjsonファイルをpythonで取り扱いしやすい辞書オブジェクトとして読み込む
##6行目では、辞書オブジェクトの["contents"]キーにアクセス
##["contents"]キーの値もさらに辞書となっていたため、forループで各話を回した
