(add-load-path "/Users/oowadakenichi/hund2015/scheme/chapter2")
(use ex10)


(define (count lst)
  (define (iter l d)
    (if (null? l)
        d    ; 出現回数が value の連想リストを返す 
        (iter (cdr l)
              (let ((p (assoc (car l) d)))
                (if p
                   (assoc-set! d (car l) (+ (cdr p) 1))
                   (assoc-set! d (car l) 1))))))
  (iter lst '()))



(define count-dic
        (count (map (lambda (x) (car (string-split x "\t")))
                    (read-file-by-line "hightemp.txt"))))

(map (lambda (x) (print (car x)))
     (reverse (sort-by count-dic cdr)))


(define (func dic lst)
  (define (proc d)
    (if (null? d)
        '()
        (append (filter (lambda (x) (equal? (caar d) (car x)))
                        lst)
                (proc (cdr d)))))
  (proc dic))

(map print
     (func (reverse (sort-by count-dic cdr))
           (map (lambda (x) (string-split x "\t"))
                (read-file-by-line "hightemp.txt"))))


