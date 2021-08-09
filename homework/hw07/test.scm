(define (filter-lst fn lst)
    (if (null? lst)
        lst
        (if (fn (car lst))
            (cons (car lst) (filter-lst fn (cdr lst)))
            (filter-lst fn (cdr lst))))
)

(define (without-duplicates lst)
    (if (null? lst) lst
        (cons (car lst) 
              (without-duplicates 
                    (filter-lst 
                        (lambda (x) (not (= x (car lst)))) 
                        lst)))))