(use gauche.sequence)
(use srfi-13)
(use srfi-27)

(define (func word-list)
  (define (subproc str)
    (if (= (string-length str) 0)
        ""
        (let ((r-i (random-integer (string-length str))))
          (string-append (make-string 1 (ref str r-i))
                         (subproc (string-append (subseq str 0 r-i)
                                                 (subseq str (+ r-i 1))))))))
  (define (proc w-list)
    (if (null? w-list)
        '()
        (let ((word (car w-list)))
          (let ((word-len (string-length word)))
            (if (<= (string-length word) 4)
                (cons word (proc (cdr w-list)))
                (cons (string-append (make-string 1 (ref word 0))
                                     (subproc (substring word 1 (- word-len 1)))
                                     (make-string 1 (ref word (- word-len 1))))
                      (proc (cdr w-list))))))))
  (proc word-list))
  



(define sentence "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind .")

(print (func (string-split sentence #\Space)))
