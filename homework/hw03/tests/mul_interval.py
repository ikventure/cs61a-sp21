test = {
  'name': 'mul_interval',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> str_interval(mul_interval(interval(-1, 2), interval(4, 8)))
          e81fb795bd91f72bc8763c8dd3f9a060
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': True,
      'setup': r"""
      >>> import hw04
      >>> from hw04 import *
      """,
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> # Testing for abstraction violations
          >>> # Your code should not check for which implementation is used
          >>> str_interval(mul_interval(interval(-1, 2), interval(4, 8)))
          '-8 to 16'
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> import hw04
      >>> old_abstraction = hw04.interval, hw04.lower_bound, hw04.upper_bound
      >>> hw04.interval = lambda a, b: lambda x: a if x == 0 else b
      >>> hw04.lower_bound = lambda s: s(0)
      >>> hw04.upper_bound = lambda s: s(1)
      >>> from hw04 import *
      """,
      'teardown': r"""
      >>> hw04.interval, hw04.lower_bound, hw04.upper_bound = old_abstraction
      """,
      'type': 'doctest'
    }
  ]
}
