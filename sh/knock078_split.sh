python ../python/knock016.py ../Data/sentiment.txt ../Data/knock078/python/splits 5
cd ../Data/result/knock078/python/
for f in `ls splits`
do
    mv splits/$f tests
    cat splits/* > train/$f
    cp tests/$f
done

