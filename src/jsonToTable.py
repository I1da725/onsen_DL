import json
import csv
import os

radioTitle = "リコラジ"
workTitle = "lycoreco"
tail = ".ts"
falder = "./output/"

is_dir = os.path.isdir(falder)
if is_dir:
    print(f"{falder} is exist.")
else:
    os.mkdir(falder)

my_Table = [["title","delivery_date","streaming_url","poster_image_url"]]

with open("{}.json".format(workTitle)) as f:
    D_json = json.load(f)

for num in D_json["contents"]:
    my_Table.append([falder + radioTitle + num["title"] + tail, num["delivery_date"], num["streaming_url"], num["poster_image_url"]])

#print(my_Table)

with open("{}.csv".format(workTitle), 'w') as f:
    # writer = csv.writer(f, delimiter='\t')
    writer = csv.writer(f, delimiter=',')
    writer.writerows(my_Table)