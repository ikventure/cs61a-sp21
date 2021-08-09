test = {
  'name': 'Question 11',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> more_boar_strategy(3, 19, cutoff=8, num_rolls=6)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(30, 54, cutoff=7, num_rolls=6)
          6
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(17, 36, cutoff=100, num_rolls=6)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(24, 3, cutoff=8, num_rolls=6)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> from tests.check_strategy import check_strategy
          >>> check_strategy(more_boar_strategy)
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from hog import *
      """,
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> more_boar_strategy(9, 83, cutoff=18, num_rolls=5)
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(68, 87, cutoff=9, num_rolls=2)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(15, 72, cutoff=11, num_rolls=3)
          3
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(24, 3, cutoff=8, num_rolls=1)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(46, 55, cutoff=5, num_rolls=2)
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(16, 73, cutoff=8, num_rolls=5)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(62, 25, cutoff=1, num_rolls=10)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(23, 92, cutoff=14, num_rolls=8)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(14, 93, cutoff=9, num_rolls=4)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(92, 54, cutoff=1, num_rolls=7)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(31, 57, cutoff=4, num_rolls=3)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(13, 76, cutoff=1, num_rolls=8)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(3, 67, cutoff=12, num_rolls=1)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(48, 74, cutoff=16, num_rolls=7)
          7
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(3, 97, cutoff=12, num_rolls=6)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(12, 5, cutoff=0, num_rolls=8)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(41, 96, cutoff=16, num_rolls=9)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(31, 68, cutoff=7, num_rolls=5)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(66, 8, cutoff=2, num_rolls=2)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(9, 75, cutoff=9, num_rolls=5)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(7, 98, cutoff=6, num_rolls=10)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(48, 84, cutoff=12, num_rolls=9)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(27, 84, cutoff=2, num_rolls=3)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(96, 56, cutoff=13, num_rolls=7)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(3, 64, cutoff=17, num_rolls=2)
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(62, 90, cutoff=15, num_rolls=7)
          7
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(98, 45, cutoff=17, num_rolls=8)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(56, 72, cutoff=16, num_rolls=6)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(24, 94, cutoff=18, num_rolls=9)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(94, 94, cutoff=17, num_rolls=6)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(17, 46, cutoff=3, num_rolls=10)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(87, 16, cutoff=2, num_rolls=8)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(38, 77, cutoff=11, num_rolls=9)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(73, 57, cutoff=3, num_rolls=7)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(11, 78, cutoff=18, num_rolls=10)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(55, 94, cutoff=12, num_rolls=8)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(19, 88, cutoff=18, num_rolls=3)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(50, 68, cutoff=13, num_rolls=5)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(2, 97, cutoff=16, num_rolls=2)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(71, 97, cutoff=16, num_rolls=3)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(91, 7, cutoff=5, num_rolls=9)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(35, 12, cutoff=2, num_rolls=1)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(51, 92, cutoff=14, num_rolls=8)
          8
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(64, 49, cutoff=16, num_rolls=4)
          4
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(35, 45, cutoff=3, num_rolls=1)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(35, 68, cutoff=15, num_rolls=2)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(75, 93, cutoff=16, num_rolls=3)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(98, 34, cutoff=7, num_rolls=9)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(51, 81, cutoff=4, num_rolls=1)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(45, 40, cutoff=18, num_rolls=6)
          6
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(96, 11, cutoff=13, num_rolls=2)
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(16, 21, cutoff=9, num_rolls=6)
          6
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(97, 99, cutoff=1, num_rolls=6)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(18, 89, cutoff=11, num_rolls=5)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(97, 64, cutoff=7, num_rolls=2)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(49, 88, cutoff=16, num_rolls=9)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(33, 89, cutoff=10, num_rolls=6)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(98, 56, cutoff=8, num_rolls=2)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(0, 84, cutoff=10, num_rolls=3)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(9, 55, cutoff=12, num_rolls=2)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(96, 43, cutoff=13, num_rolls=7)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(18, 34, cutoff=16, num_rolls=3)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(24, 81, cutoff=9, num_rolls=4)
          4
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(11, 87, cutoff=18, num_rolls=1)
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(51, 85, cutoff=16, num_rolls=9)
          9
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(63, 40, cutoff=7, num_rolls=9)
          9
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(60, 51, cutoff=13, num_rolls=6)
          6
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(53, 74, cutoff=5, num_rolls=8)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(27, 72, cutoff=11, num_rolls=6)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(75, 73, cutoff=11, num_rolls=8)
          8
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(86, 24, cutoff=0, num_rolls=5)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(18, 95, cutoff=1, num_rolls=1)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(94, 69, cutoff=15, num_rolls=8)
          8
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(53, 46, cutoff=3, num_rolls=3)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(91, 9, cutoff=9, num_rolls=5)
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(19, 81, cutoff=8, num_rolls=1)
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(79, 98, cutoff=8, num_rolls=8)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(47, 78, cutoff=15, num_rolls=8)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(68, 89, cutoff=2, num_rolls=8)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(13, 76, cutoff=6, num_rolls=4)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(8, 79, cutoff=7, num_rolls=6)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(45, 65, cutoff=16, num_rolls=6)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(31, 98, cutoff=14, num_rolls=1)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(40, 3, cutoff=4, num_rolls=9)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(89, 56, cutoff=14, num_rolls=1)
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(32, 13, cutoff=4, num_rolls=4)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(45, 17, cutoff=13, num_rolls=8)
          8
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(77, 59, cutoff=15, num_rolls=7)
          7
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(48, 34, cutoff=1, num_rolls=5)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(56, 86, cutoff=1, num_rolls=7)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(68, 98, cutoff=11, num_rolls=7)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(2, 28, cutoff=10, num_rolls=6)
          6
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(42, 67, cutoff=18, num_rolls=7)
          7
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(9, 55, cutoff=11, num_rolls=6)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(10, 96, cutoff=11, num_rolls=9)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(41, 19, cutoff=5, num_rolls=3)
          3
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(90, 38, cutoff=12, num_rolls=5)
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(35, 51, cutoff=7, num_rolls=4)
          4
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(42, 52, cutoff=1, num_rolls=5)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(35, 57, cutoff=8, num_rolls=10)
          0
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from hog import *
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
