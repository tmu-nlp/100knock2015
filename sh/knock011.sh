# bash knock011.sh ../Data/hightemp.txt

cat $1 | sed -e $'s/\t/ /g'
