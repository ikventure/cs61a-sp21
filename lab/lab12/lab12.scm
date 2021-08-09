(define (tail-replicate x n)
  (define (tail-replicate-optimize x n so-far)
    (if (= n 0)
        so-far
        (tail-replicate-optimize x
                                 (- n 1)
                                 (cons x so-far))))
  (tail-replicate-optimize x n nil))

(define-macro (def func args body)
  `(define ,func (lambda ,args ,body)))

(define-macro (def2 func args body)
  `(define (,func ,@args) ,body))

(define (repeatedly-cube n x)
  (if (zero? n)
      x
      (let ((y (repeatedly-cube (- n 1) x)))
        (* y y y))))