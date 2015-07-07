sort ../Data/knock045.result| uniq -c | sort -r | less
grep -e "^する\t" -e "^見る\t" -e "^与える\t" ../Data/knock045.result|sort|uniq -c|sort -r | less
