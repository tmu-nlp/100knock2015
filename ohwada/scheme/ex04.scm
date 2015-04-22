(define (func word-list number-list)
  (define (proc wl nl i)
    (cond ((null? wl) '())
          ((memq i number-list)
           (cons (cons (make-string 1 (string-ref (car wl) 0)) i)
                 (proc (cdr wl) (cdr nl) (+ i 1))))
          (else (cons (cons (substring (car wl) 0 2) i)
                (proc (cdr wl) nl (+ i 1))))))
  (proc word-list number-list 1))


(define sentence "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.")

(define number-list (list 1 5 6 7 8 9 15 16 19))


(print (func (string-split sentence #\Space) number-list))
(print (assoc "Ne" (func (string-split sentence #\Space) number-list)))
