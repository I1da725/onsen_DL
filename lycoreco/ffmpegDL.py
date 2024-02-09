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