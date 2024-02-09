import json
import csv

radioTitle = "リコラジ"
workTitle = "lycoreco"

my_Table = [["title","delivery_date","streaming_url","poster_image_url"]]

with open("{}.json".format(workTitle)) as f:
    D_json = json.load(f)

for num in D_json["contents"]:
    my_Table.append([radioTitle + num["title"], num["delivery_date"], num["streaming_url"], num["poster_image_url"]])

#print(my_Table)

with open("{}.csv".format(workTitle), 'w') as f:
    # writer = csv.writer(f, delimiter='\t')
    writer = csv.writer(f, delimiter=',')
    writer.writerows(my_Table)