(define (split-at lst n)
    (cond
        ((null? lst) nil)
        ((= n 0) lst)
        (else
            (cons (car lst) (split-at (cdr lst) (- n 1)))))
)

(define (compose-all funcs) 'YOUR-CODE-HERE)
