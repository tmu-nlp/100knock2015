(define-module ex10
  (export read-file-by-char
          read-file-by-line))

(select-module ex10)


(use gauche.sequence)

; 1
(define (read-file-by-char file)
  (let ((f (open-input-file file)))
    (define (iter lst c)
      (if (eof-object? c)
          (begin (close-input-port f)
                 (let ((last-i (- (length lst) 1)))
                   (if (char=? (ref lst last-i) #\newline)
                       ; string を返す
                       (list->string (subseq lst 0 last-i))
                       (list->string lst))))
          (iter (append lst (list c)) (read-char f))))
    (iter '() (read-char f))))


(define (count-lines text)
  (length (string-split text #\newline)))


; 2
(define (read-file-by-line file)
  (let ((f (open-input-file file)))
    (define (iter lst l)
      (if (eof-object? l)
          (begin (close-input-port f)
                 ; list を返す
                 lst)
          (iter (append lst (list l)) (read-line f))))
    (iter '() (read-line f))))


(define (main args)
    ; gosh -m ex10 ex10.scm で出力
    (print (count-lines (read-file-by-char "hightemp.txt")))
    (print (length (read-file-by-line "hightemp.txt"))))

