#!/bin/zsh
# 本ファイルの実行方法 $./autoDL.command lycoreco.csv
# CSVファイル名を引数として受け取る
csv_file=$1

# CSVファイルのA列とC列を2行目から取得し、それぞれの行に対してffmpegコマンドを実行
tail -n +2 $csv_file | awk -F',' '{system("ffmpeg -headers \"Referer: https://www.onsen.ag/\" -i "$3" -c copy "$1)}'
