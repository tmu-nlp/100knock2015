(define str "stressed")

(print (list->string (reverse (string->list str))))


(use srfi-13)

(print (string-reverse str))
