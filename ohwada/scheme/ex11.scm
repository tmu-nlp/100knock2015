(add-load-path "/Users/oowadakenichi/hund2015/scheme/chapter2")
(use ex10)

(define (func line-lst)
  (map (lambda (x) (string-join (string-split x "\t") " ")) line-lst))

(map print (func (read-file-by-line "hightemp.txt"))) 
