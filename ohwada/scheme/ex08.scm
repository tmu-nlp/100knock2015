(define (cipher str)
  (define (proc s i)
    (if (= i (string-length s))
        ""
        (let ((c (if (char-lower-case? (ref s i))
                     (integer->char (- 219 (char->integer (ref s i))))
                     (ref s i))))
             (string-append (make-string 1 c) (proc s (+ i 1))))))
  (proc str 0))


(define message "I want to hold your hand.")

(print (cipher message))
  
