test = {
  'name': 'without-duplicates',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (without-duplicates (list 5 4 2))
          (5 4 2)
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (without-duplicates (list 5 4 5 4 2 2))
          (5 4 2)
          scm> (without-duplicates (list 5 5 5 5 5))
          (5)
          scm> (without-duplicates ())
          ()
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (without-duplicates '(5 4 3 2 1))
          (5 4 3 2 1)
          scm> (without-duplicates '(5 4 3 2 1 1))
          (5 4 3 2 1)
          scm> (without-duplicates '(5 5 4 3 2 1))
          (5 4 3 2 1)
          scm> (without-duplicates '(12))
          (12)
          scm> (without-duplicates '(1 1 1 1 1 1))
          (1)
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load-all ".")
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
