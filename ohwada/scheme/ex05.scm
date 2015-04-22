(define-module ex05
  (export get-ngram))

(select-module ex05)


(use gauche.sequence)

(define (get-ngram sequence n)
  (let ((len (if (string? sequence)
                 (string-length sequence)
                 (length sequence))))
    (define (proc i)
      (if (= i (+ (- len n) 1))
          '()
          (cons (subseq sequence i (+ i n))
                (proc (+ i 1)))))
    (proc 0)))


(define sentence "I am an NLPer")


(define (main args)
  ; gosh -m ex05 ex05.scm で出力
  (print (get-ngram (string-split sentence #\Space) 2))
  (print (map (lambda (x) (get-ngram x 2)) (string-split sentence #\Space))))


