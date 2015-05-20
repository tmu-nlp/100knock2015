(define-module ex12
  (export write-file-by-string
          write-file-by-line))

(select-module ex12)


(add-load-path "/Users/oowadakenichi/hund2015/scheme/chapter2")
(use ex10)


; 1
(define (write-file-by-string text file)
  (let ((f (open-output-file file)))
    (display text f)))

(define (write-col-n text file n)
  (let ((line-lst (string-split text "\n")))
    (write-file-by-string
      (string-join
        (map (lambda (x) (list-ref (string-split x "\t") n))
             line-lst)
        "\n")
      file)))



; 2
(define (write-file-by-line line-lst file)
  (let ((f (open-output-file file)))
    (map (lambda (x) (display (string-append x "\n") f)) line-lst)))

(define (write-col-n line-lst file n)
  (write-file-by-line
    (map (lambda (x) (list-ref (string-split x "\t") n))
         line-lst)
    file))


(define (main args)
  (write-col-n (read-file-by-line "hightemp.txt") "col1.txt" 0)
  (write-col-n (read-file-by-line "hightemp.txt") "col2.txt" 1))
