(define (func word-list)
  (if (null? word-list) '()
      (let ((last-letter
            (string-ref (car word-list) (- (string-length (car word-list)) 1))))
        (if (or (char=? last-letter #\,) (char=? last-letter #\.))
            (cons (- (string-length (car word-list)) 1) (func (cdr word-list)))
            (cons (string-length (car word-list)) (func (cdr word-list)))))))       


(define sentence "Now I need a drink, alcoholic of cource, after the heavy lectures involving quantum mechanics.")


(print (func (string-split sentence #\Space)))

