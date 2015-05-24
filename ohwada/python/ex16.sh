#!/bin/sh
# usage: ./ex16.sh filename N


file=$1                                 # 対象ファイル
ln=`wc -l $1 | cut -d " " -f 7`         # その行数
N=$2                                    # 分割数

x=`expr $ln / $N`                       # 商（切り捨て）
y=`expr $ln % $N`                       # 余り

a=`expr \( $x + 1 \) \* $y`             # (商+1) * 余り
b=`expr $ln - $a`                       # 行数 - a


head -n $a $file >"head.txt"            # 最初の a 行と残りの b 行に分ける
tail -n $b $file >"tail.txt"

split -l `expr $x + 1` "head.txt" out   # outaa, outab... に分割
c=1
for f in out* ; do                      # ファイル名を変更。c で連番にする
  mv $f result_ex16/f$c.txt
  c=`expr $c + 1`
done

split -l $x "tail.txt" out
for f in out* ; do
  mv $f result_ex16/f$c.txt
  c=`expr $c + 1`
done

rm "head.txt" "tail.txt"
