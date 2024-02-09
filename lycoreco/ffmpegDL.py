import csv
import ffmpeg

radioTitle = "リコラジ"
workTitle = "lycoreco"

with open("{}.csv".format(workTitle), encoding='utf8') as f:
    Table = csv.reader(f)
    rawTable = [row for row in Table]

# print(rawTable)

for i in rawTable[1:]:
    print(i[0],i[2])
    # stream = ffmpeg.input("{}".format(i[2])).output("{}.ts".format(i[0]))
    # ffmpeg.run(stream)

#ffmpeg-pythonが本家ffmpeg全部をラップしていないため、断念シェルスクリプトで実装