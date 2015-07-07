DIR="../Data/result/knock078/python/"
echo "" >> $DIR/result.txt
for f in `ls $DIR/tests`
do
    python ../python/knock076.py $DIR/models/$f.model $DIR/tests/$f > $DIR/labelings/$f
    python ../python/knock077.py $DIR/labelings/$f >> $DIR/result.txt
done
