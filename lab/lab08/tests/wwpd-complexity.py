test = {
  'name': 'Orders of Growth',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'answer': '4b9e5fd8f91a1086c65a62b4034aa828',
          'choices': [
            'Logarithmic - Θ(log(n))',
            'Linear - Θ(n)',
            'Quadratic - Θ(n^2)',
            'Exponential - Θ(2^n)'
          ],
          'hidden': False,
          'locked': True,
          'question': r"""
          What is the order of growth of `is_prime` in terms of `n`?
          
          def is_prime(n):
              for i in range(2, n):
                  if n % i == 0:
                      return False
              return True
          """
        },
        {
          'answer': '82f9cb757399850b080cd44aca561f98',
          'choices': [
            'Logarithmic - Θ(log(n))',
            'Linear - Θ(n)',
            'Quadratic - Θ(n^2)',
            'Exponential - Θ(2^n)'
          ],
          'hidden': False,
          'locked': True,
          'question': r"""
          What is the order of growth of `bar` in terms of `n`?
          
          def bar(n):
              i, sum = 1, 0
              while i <= n:
                  sum += biz(n)
                  i += 1
              return sum
          
          def biz(n):
              i, sum = 1, 0
              while i <= n:
                  sum += i**3
                  i += 1
              return sum
          """
        }
      ],
      'scored': False,
      'type': 'concept'
    }
  ]
}
