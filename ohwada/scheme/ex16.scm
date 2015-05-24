(add-load-path "/Users/oowadakenichi/hund2015/scheme/chapter2")
(use gauche.sequence)
(use ex10)
(use ex12)


(define (get-linage-lst file N)
  (let ((all-linage (length (read-file-by-line file))))
    (let ((x1 (abs (div (* -1 all-linage) N)))
          (x2 (div all-linage N)))
      (let loop ((ln (- all-linage x2)) (c 1))
           (if (= (+ (* x1 (- N c)) (* x2 c)) all-linage)
               (append (make-list (- N c) x1) (make-list c x2))
               (loop (- ln x2) (+ c 1)))))))


(define (split-file file linage-lst)
  (let loop ((c 1) (lines (read-file-by-line file)))
    (if (> c (length linage-lst))
        (print "done!")
        (begin
          (write-file-by-line (subseq lines 0 (ref linage-lst (- c 1)))
                              (format "result_ex16/f~s.txt" c))
          (loop (+ c 1) (subseq lines (ref linage-lst (- c 1))))))))




(define (main args)
  (let ((linage-lst (get-linage-lst "hightemp.txt" (string->number (cadr args)))))
    ;(print linage-lst)
    (split-file "hightemp.txt" linage-lst)))
  




