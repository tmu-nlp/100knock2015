python ../python/knock016.py ../Data/sentiment.txt ../Data/result/knock078/python/splits 5
cd ../Data/result/knock078/python/
for f in `ls splits`
do
    mv splits/$f tests
    cat splits/* > trains/$f
    cp tests/$f splits/
done

