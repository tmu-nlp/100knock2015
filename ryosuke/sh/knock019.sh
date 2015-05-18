# bash knock019.sh ../Data/hightemp.sh
cut -d $'\t' -f 1 $1  | sort | uniq -c | sort -r
