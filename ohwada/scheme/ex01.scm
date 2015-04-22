(define (func str number_list)
  (if (null? number_list)
      ""
      (let ((x (make-string 1 (ref str (- (car number_list) 1)))))
        (string-append x (func str (cdr number_list))))))


(define str "パタトクカシーー")
(define number_list (list 1 3 5 7))

(print (func str number_list))
