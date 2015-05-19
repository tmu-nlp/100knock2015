# bash knock016.sh ../Data/hightemp.txt [outdir] [n]
lcount=`cat $1 | wc -l`
lcount=`expr $lcount + $3 - 1`
num=`expr $lcount / $3`
split -l $num $1 $2/split_
