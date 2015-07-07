DIR="../Data/result/knock078/python/"
for f in `ls $DIR/trains`
do
    classias-train -tb -m $DIR/models/$f.model $DIR/trains/$f
done
