#!/bin/zsh

# ファイル名を引数として受け取る
input_file=$1

# ファイル名から拡張子を除いた部分を取得
base_name=$(basename $input_file .${input_file##*.})

# 出力ファイル名を作成（拡張子を.m4aに変更）
output_file="${base_name}.m4a"

# ffmpegコマンドを実行
ffmpeg -i $input_file $output_file