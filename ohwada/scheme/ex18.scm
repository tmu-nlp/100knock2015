(add-load-path "/Users/oowadakenichi/hund2015/scheme/chapter2")
(use ex10)


(map print (sort-by (read-file-by-line "hightemp.txt")
                    (lambda (x) (caddr (string-split x "\t")))))


