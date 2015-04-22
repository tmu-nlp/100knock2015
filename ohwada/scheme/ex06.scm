(add-load-path "/Users/oowadakenichi/hund2015/scheme/chapter1")
(use ex05)
(use srfi-1)
    
 
(define str1 "paraparaparadise")
(define str2 "paragraph")

(define X (delete-duplicates (get-ngram str1 2))) 
(define Y (delete-duplicates (get-ngram str2 2))) 


(print (lset-union equal? X Y))
(print (lset-intersection equal? X Y))
(print (lset-difference equal? X Y))
(print (lset-difference equal? Y X))


(define (in? obj lst)
  (if (equal? (find (lambda (x) (equal? x obj)) lst) #f)
      #f
      #t))

(print (in? "se" X))
(print (in? "se" Y))
