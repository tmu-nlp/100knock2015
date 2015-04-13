# bash knock012.sh ../Data/hightemp.txt ../Data/col1.txt ../Data/col2.txt
cut -f 1 -d $'\t' $1 > $2
cut -f 2 -d $'\t' $1 > $3

