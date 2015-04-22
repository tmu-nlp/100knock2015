(define (func str1 str2)
  (define (proc i)
    (if (= i (string-length str1))
        ""
        (string-append (make-string 1 (ref str1 i))
                       (make-string 1 (ref str2 i))
                       (proc (+ i 1)))))
  (proc 0))


(define str1 "パトカー")
(define str2 "タクシー")


(print (func str1 str2))


