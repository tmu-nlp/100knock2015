(add-load-path "/Users/oowadakenichi/hund2015/scheme/chapter2")
(use ex10)
(use gauche.sequence)


(define (func file n)
  (let ((line-lst (read-file-by-line file)))
    (map print (subseq line-lst 0 n))))


(define (main args)
  (func "hightemp.txt" (string->number (cadr args))))      
