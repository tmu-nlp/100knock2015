#!/bin/sh 

DATA=train1.txt
MODEL=model.txt

if [ -e all_score.txt ]; then
  rm all_score.txt
fi
python ex16.py $DATA 5

c=1
while [ $c -le 5 ]; do
    # 学習ファイル作成
    find . -name "split*.txt" -not -name "split0$c.txt" | xargs cat > train.txt
    # 学習
    classias-train -tb -m $MODEL train.txt > train.log
    # テスト
    cat split0$c.txt | classias-tag -r -p -m $MODEL | python ex76.py > output_ex76.txt
    # スコア出力
    python ex77.py >>all_score.txt
    c=`expr $c + 1`
done

# 平均を計算
cat all_score.txt | python ex78.py
