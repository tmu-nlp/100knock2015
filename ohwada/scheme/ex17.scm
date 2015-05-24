(add-load-path "/Users/oowadakenichi/hund2015/scheme/chapter2")
(use ex10)


(map print (delete-duplicates (read-file-by-line "col1.txt")))
