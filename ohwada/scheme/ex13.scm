(add-load-path "/Users/oowadakenichi/hund2015/scheme/chapter2")
(use ex10)
(use ex12)


(define (func file1 file2 out-file delim)
  (let ((line-lst1 (read-file-by-line file1))
        (line-lst2 (read-file-by-line file2)))
    (write-file-by-line
      (map (lambda (x y) (string-join (list x y) delim)) line-lst1 line-lst2)
      out-file)))


(func "col1.txt" "col2.txt" "col1-2.txt" "\t")
