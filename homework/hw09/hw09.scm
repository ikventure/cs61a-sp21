(define-macro (switch expr cases)
  (cons 'cond
        (map (lambda (case)
               (cons `(eqv? ,expr ',(car case)) (cdr case)))
             cases)))
