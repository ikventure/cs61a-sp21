test = {
  'name': 'Question 5',
  'points': 3,
  'suites': [
    {
      'cases': [
        {
          'answer': 'While score0 and score1 are both less than goal',
          'choices': [
            'While score0 and score1 are both less than goal',
            'While at least one of score0 or score1 is less than goal',
            'While score0 is less than goal',
            'While score1 is less than goal'
          ],
          'hidden': False,
          'locked': False,
          'question': r"""
          The variables score0 and score1 are the scores for Player 0
          and Player 1, respectively. Under what conditions should the
          game continue?
          """
        },
        {
          'answer': 'A function that returns the number of dice a player will roll',
          'choices': [
            'The number of dice a player will roll',
            'A function that returns the number of dice a player will roll',
            "A player's desired turn outcome"
          ],
          'hidden': False,
          'locked': False,
          'question': 'What is a strategy in the context of this game?'
        },
        {
          'answer': 'strategy1(score1, score0)',
          'choices': [
            'strategy1(score1, score0)',
            'strategy1(score0, score1)',
            'strategy1(score1)',
            'strategy1(score0)'
          ],
          'hidden': False,
          'locked': False,
          'question': r"""
          If strategy1 is Player 1's strategy function, score0 is
          Player 0's current score, and score1 is Player 1's current
          score, then which of the following demonstrates correct
          usage of strategy1?
          """
        }
      ],
      'scored': False,
      'type': 'concept'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> #
          >>> # Play function stops at goal
          >>> s0, s1 = hog.play(always(5), always(3), score0=91, score1=10, dice=always_three)
          >>> s0
          106
          >>> s1
          10
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> #
          >>> # Goal score is not hardwired
          >>> s0, s1 = hog.play(always(5), always(5), goal=10, dice=always_three)
          >>> s0
          15
          >>> s1
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> #
          >>> # Extra turn from more boar
          >>> s0, s1 = hog.play(always(6), always(2), goal=25, dice=always_three)
          >>> s0
          36
          >>> s1
          12
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> #
          >>> # Goal score is not hardwired
          >>> s0, s1 = hog.play(always(5), always(5), goal=15, dice=always_three)
          >>> s0
          15
          >>> s1
          0
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> import hog
      >>> always_three = hog.make_test_dice(3)
      >>> always = hog.always_roll
      """,
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> #
          >>> # Use strategies
          >>> # We recommend working this out turn-by-turn on a piece of paper (use Python for difficult calculations).
          >>> strat0 = lambda score, opponent: opponent % 10
          >>> strat1 = lambda score, opponent: max((score // 10) - 4, 0)
          >>> s0, s1 = hog.play(strat0, strat1, score0=71, score1=80, dice=always_seven)
          >>> s0
          74
          >>> s1
          108
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> import hog
      >>> always_three = hog.make_test_dice(3)
      >>> always_seven = hog.make_test_dice(7)
      """,
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> #
          >>> # Player 0 win
          >>> s0, s1 = hog.play(always(4), always(4), score0=88, score1=87, dice=always_three)
          >>> s0
          100
          >>> s1
          87
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> #
          >>> # Piggy points refers to correct opponent score
          >>> s0, s1 = hog.play(always(0), always(0), score0=5, score1=96, dice=always_three)
          >>> s0
          9
          >>> s1
          100
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> #
          >>> # Handle multiple turns with stacking extra turns
          >>> s0, s1 = hog.play(always(1), always(1), goal=25, dice=hog.make_test_dice(5, 19, 2, 1, 11, 6))
          >>> s0
          19
          >>> s1
          25
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> import hog
      >>> always_one = hog.make_test_dice(1)
      >>> always_two = hog.make_test_dice(2)
      >>> always_three = hog.make_test_dice(3)
      >>> always = hog.always_roll
      """,
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=45891, score0=47, score1=53, goal=54)
          >>> print(turns[0])
          Start scores = (47, 53).
          Player 0 rolls 9 dice and gets outcomes [5, 1, 1, 2, 6, 1, 1, 1, 5].
          End scores = (48, 53)
          >>> print(turns[1])
          Start scores = (48, 53).
          Player 1 rolls 7 dice and gets outcomes [3, 2, 6, 2, 3, 2, 5].
          End scores = (48, 76)
          >>> print(turns[2])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=5192, score0=43, score1=12, goal=47)
          >>> print(turns[0])
          Start scores = (43, 12).
          Player 0 rolls 8 dice and gets outcomes [2, 1, 5, 1, 3, 3, 2, 3].
          End scores = (44, 12)
          >>> print(turns[1])
          Start scores = (44, 12).
          Player 1 rolls 8 dice and gets outcomes [5, 2, 5, 3, 5, 4, 2, 1].
          End scores = (44, 13)
          >>> print(turns[2])
          Start scores = (44, 13).
          Player 1 rolls 7 dice and gets outcomes [2, 3, 1, 1, 6, 1, 4].
          End scores = (44, 14)
          >>> print(turns[3])
          Start scores = (44, 14).
          Player 0 rolls 10 dice and gets outcomes [6, 5, 4, 5, 2, 6, 1, 1, 3, 6].
          End scores = (45, 14)
          >>> print(turns[4])
          Start scores = (45, 14).
          Player 1 rolls 4 dice and gets outcomes [6, 6, 2, 6].
          End scores = (45, 34)
          >>> print(turns[5])
          Start scores = (45, 34).
          Player 1 rolls 1 dice and gets outcomes [2].
          End scores = (45, 36)
          >>> print(turns[6])
          Start scores = (45, 36).
          Player 0 rolls 10 dice and gets outcomes [2, 6, 6, 2, 3, 1, 5, 2, 4, 2].
          End scores = (46, 36)
          >>> print(turns[7])
          Start scores = (46, 36).
          Player 1 rolls 6 dice and gets outcomes [2, 5, 2, 4, 4, 3].
          End scores = (46, 56)
          >>> print(turns[8])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=95816, score0=15, score1=45, goal=50)
          >>> print(turns[0])
          Start scores = (15, 45).
          Player 0 rolls 8 dice and gets outcomes [2, 3, 1, 6, 5, 1, 5, 6].
          End scores = (16, 45)
          >>> print(turns[1])
          Start scores = (16, 45).
          Player 1 rolls 10 dice and gets outcomes [5, 2, 4, 3, 6, 3, 4, 5, 1, 2].
          End scores = (16, 46)
          >>> print(turns[2])
          Start scores = (16, 46).
          Player 0 rolls 2 dice and gets outcomes [4, 6].
          End scores = (26, 46)
          >>> print(turns[3])
          Start scores = (26, 46).
          Player 1 rolls 1 dice and gets outcomes [2].
          End scores = (26, 48)
          >>> print(turns[4])
          Start scores = (26, 48).
          Player 0 rolls 6 dice and gets outcomes [2, 1, 4, 2, 6, 6].
          End scores = (27, 48)
          >>> print(turns[5])
          Start scores = (27, 48).
          Player 0 rolls 7 dice and gets outcomes [3, 4, 6, 5, 6, 5, 3].
          End scores = (59, 48)
          >>> print(turns[6])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=25365, score0=3, score1=8, goal=34)
          >>> print(turns[0])
          Start scores = (3, 8).
          Player 0 rolls 6 dice and gets outcomes [2, 5, 4, 6, 5, 1].
          End scores = (4, 8)
          >>> print(turns[1])
          Start scores = (4, 8).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (4, 12)
          >>> print(turns[2])
          Start scores = (4, 12).
          Player 0 rolls 5 dice and gets outcomes [2, 2, 3, 1, 1].
          End scores = (5, 12)
          >>> print(turns[3])
          Start scores = (5, 12).
          Player 1 rolls 10 dice and gets outcomes [6, 2, 6, 5, 5, 2, 4, 1, 4, 6].
          End scores = (5, 13)
          >>> print(turns[4])
          Start scores = (5, 13).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (9, 13)
          >>> print(turns[5])
          Start scores = (9, 13).
          Player 1 rolls 8 dice and gets outcomes [6, 6, 6, 4, 1, 5, 2, 5].
          End scores = (9, 14)
          >>> print(turns[6])
          Start scores = (9, 14).
          Player 0 rolls 9 dice and gets outcomes [5, 4, 6, 6, 6, 2, 6, 3, 3].
          End scores = (50, 14)
          >>> print(turns[7])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=11863, score0=55, score1=5, goal=56)
          >>> print(turns[0])
          Start scores = (55, 5).
          Player 0 rolls 6 dice and gets outcomes [5, 1, 2, 1, 3, 5].
          End scores = (56, 5)
          >>> print(turns[1])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=59465, score0=61, score1=16, goal=88)
          >>> print(turns[0])
          Start scores = (61, 16).
          Player 0 rolls 4 dice and gets outcomes [2, 2, 3, 4].
          End scores = (72, 16)
          >>> print(turns[1])
          Start scores = (72, 16).
          Player 1 rolls 2 dice and gets outcomes [2, 3].
          End scores = (72, 21)
          >>> print(turns[2])
          Start scores = (72, 21).
          Player 1 rolls 7 dice and gets outcomes [2, 6, 3, 6, 2, 1, 5].
          End scores = (72, 22)
          >>> print(turns[3])
          Start scores = (72, 22).
          Player 0 rolls 9 dice and gets outcomes [1, 3, 2, 2, 2, 2, 2, 1, 1].
          End scores = (73, 22)
          >>> print(turns[4])
          Start scores = (73, 22).
          Player 1 rolls 5 dice and gets outcomes [1, 3, 1, 5, 5].
          End scores = (73, 23)
          >>> print(turns[5])
          Start scores = (73, 23).
          Player 0 rolls 10 dice and gets outcomes [3, 1, 2, 2, 6, 3, 4, 4, 4, 5].
          End scores = (74, 23)
          >>> print(turns[6])
          Start scores = (74, 23).
          Player 1 rolls 7 dice and gets outcomes [4, 4, 2, 4, 2, 2, 3].
          End scores = (74, 44)
          >>> print(turns[7])
          Start scores = (74, 44).
          Player 0 rolls 8 dice and gets outcomes [2, 3, 6, 5, 6, 6, 3, 5].
          End scores = (110, 44)
          >>> print(turns[8])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=4714, score0=9, score1=3, goal=20)
          >>> print(turns[0])
          Start scores = (9, 3).
          Player 0 rolls 2 dice and gets outcomes [3, 2].
          End scores = (14, 3)
          >>> print(turns[1])
          Start scores = (14, 3).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (14, 7)
          >>> print(turns[2])
          Start scores = (14, 7).
          Player 0 rolls 3 dice and gets outcomes [2, 6, 4].
          End scores = (26, 7)
          >>> print(turns[3])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=10742, score0=4, score1=25, goal=57)
          >>> print(turns[0])
          Start scores = (4, 25).
          Player 0 rolls 8 dice and gets outcomes [2, 3, 1, 3, 6, 4, 3, 6].
          End scores = (5, 25)
          >>> print(turns[1])
          Start scores = (5, 25).
          Player 1 rolls 5 dice and gets outcomes [5, 3, 5, 6, 4].
          End scores = (5, 48)
          >>> print(turns[2])
          Start scores = (5, 48).
          Player 0 rolls 6 dice and gets outcomes [1, 3, 3, 2, 6, 6].
          End scores = (6, 48)
          >>> print(turns[3])
          Start scores = (6, 48).
          Player 0 rolls 8 dice and gets outcomes [4, 3, 5, 6, 1, 1, 3, 4].
          End scores = (7, 48)
          >>> print(turns[4])
          Start scores = (7, 48).
          Player 0 rolls 1 dice and gets outcomes [2].
          End scores = (9, 48)
          >>> print(turns[5])
          Start scores = (9, 48).
          Player 1 rolls 7 dice and gets outcomes [5, 6, 2, 4, 5, 1, 2].
          End scores = (9, 49)
          >>> print(turns[6])
          Start scores = (9, 49).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (12, 49)
          >>> print(turns[7])
          Start scores = (12, 49).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (15, 49)
          >>> print(turns[8])
          Start scores = (15, 49).
          Player 0 rolls 4 dice and gets outcomes [1, 2, 6, 1].
          End scores = (16, 49)
          >>> print(turns[9])
          Start scores = (16, 49).
          Player 0 rolls 10 dice and gets outcomes [3, 6, 4, 2, 5, 1, 6, 1, 4, 1].
          End scores = (17, 49)
          >>> print(turns[10])
          Start scores = (17, 49).
          Player 0 rolls 9 dice and gets outcomes [6, 4, 6, 2, 3, 5, 2, 4, 5].
          End scores = (54, 49)
          >>> print(turns[11])
          Start scores = (54, 49).
          Player 1 rolls 2 dice and gets outcomes [4, 4].
          End scores = (54, 57)
          >>> print(turns[12])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=5480, score0=5, score1=8, goal=77)
          >>> print(turns[0])
          Start scores = (5, 8).
          Player 0 rolls 7 dice and gets outcomes [3, 6, 3, 3, 4, 4, 6].
          End scores = (34, 8)
          >>> print(turns[1])
          Start scores = (34, 8).
          Player 1 rolls 2 dice and gets outcomes [1, 4].
          End scores = (34, 9)
          >>> print(turns[2])
          Start scores = (34, 9).
          Player 0 rolls 1 dice and gets outcomes [2].
          End scores = (36, 9)
          >>> print(turns[3])
          Start scores = (36, 9).
          Player 1 rolls 8 dice and gets outcomes [5, 4, 4, 4, 4, 5, 1, 1].
          End scores = (36, 10)
          >>> print(turns[4])
          Start scores = (36, 10).
          Player 1 rolls 4 dice and gets outcomes [2, 4, 5, 5].
          End scores = (36, 26)
          >>> print(turns[5])
          Start scores = (36, 26).
          Player 0 rolls 1 dice and gets outcomes [4].
          End scores = (40, 26)
          >>> print(turns[6])
          Start scores = (40, 26).
          Player 1 rolls 7 dice and gets outcomes [5, 4, 1, 1, 2, 1, 3].
          End scores = (40, 27)
          >>> print(turns[7])
          Start scores = (40, 27).
          Player 0 rolls 2 dice and gets outcomes [1, 4].
          End scores = (41, 27)
          >>> print(turns[8])
          Start scores = (41, 27).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (41, 31)
          >>> print(turns[9])
          Start scores = (41, 31).
          Player 0 rolls 7 dice and gets outcomes [3, 6, 1, 5, 2, 4, 4].
          End scores = (42, 31)
          >>> print(turns[10])
          Start scores = (42, 31).
          Player 1 rolls 9 dice and gets outcomes [6, 4, 5, 6, 5, 2, 2, 3, 5].
          End scores = (42, 69)
          >>> print(turns[11])
          Start scores = (42, 69).
          Player 0 rolls 4 dice and gets outcomes [5, 2, 3, 5].
          End scores = (57, 69)
          >>> print(turns[12])
          Start scores = (57, 69).
          Player 0 rolls 6 dice and gets outcomes [1, 1, 4, 6, 6, 2].
          End scores = (58, 69)
          >>> print(turns[13])
          Start scores = (58, 69).
          Player 0 rolls 8 dice and gets outcomes [2, 2, 6, 4, 2, 4, 2, 2].
          End scores = (82, 69)
          >>> print(turns[14])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=5014, score0=56, score1=59, goal=64)
          >>> print(turns[0])
          Start scores = (56, 59).
          Player 0 rolls 6 dice and gets outcomes [1, 3, 1, 4, 5, 1].
          End scores = (57, 59)
          >>> print(turns[1])
          Start scores = (57, 59).
          Player 1 rolls 1 dice and gets outcomes [4].
          End scores = (57, 63)
          >>> print(turns[2])
          Start scores = (57, 63).
          Player 0 rolls 8 dice and gets outcomes [5, 6, 5, 4, 2, 5, 6, 5].
          End scores = (95, 63)
          >>> print(turns[3])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=50496, score0=4, score1=15, goal=19)
          >>> print(turns[0])
          Start scores = (4, 15).
          Player 0 rolls 9 dice and gets outcomes [6, 4, 2, 6, 1, 5, 5, 2, 6].
          End scores = (5, 15)
          >>> print(turns[1])
          Start scores = (5, 15).
          Player 1 rolls 9 dice and gets outcomes [3, 1, 1, 4, 5, 1, 1, 6, 4].
          End scores = (5, 16)
          >>> print(turns[2])
          Start scores = (5, 16).
          Player 0 rolls 2 dice and gets outcomes [1, 6].
          End scores = (6, 16)
          >>> print(turns[3])
          Start scores = (6, 16).
          Player 1 rolls 9 dice and gets outcomes [6, 4, 1, 2, 5, 6, 1, 5, 6].
          End scores = (6, 17)
          >>> print(turns[4])
          Start scores = (6, 17).
          Player 0 rolls 1 dice and gets outcomes [1].
          End scores = (7, 17)
          >>> print(turns[5])
          Start scores = (7, 17).
          Player 1 rolls 2 dice and gets outcomes [5, 5].
          End scores = (7, 27)
          >>> print(turns[6])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=97617, score0=16, score1=27, goal=35)
          >>> print(turns[0])
          Start scores = (16, 27).
          Player 0 rolls 6 dice and gets outcomes [4, 3, 5, 1, 5, 2].
          End scores = (17, 27)
          >>> print(turns[1])
          Start scores = (17, 27).
          Player 1 rolls 2 dice and gets outcomes [6, 2].
          End scores = (17, 35)
          >>> print(turns[2])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=19709, score0=27, score1=6, goal=85)
          >>> print(turns[0])
          Start scores = (27, 6).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (33, 6)
          >>> print(turns[1])
          Start scores = (33, 6).
          Player 1 rolls 4 dice and gets outcomes [4, 4, 4, 1].
          End scores = (33, 7)
          >>> print(turns[2])
          Start scores = (33, 7).
          Player 0 rolls 8 dice and gets outcomes [3, 6, 2, 4, 4, 6, 3, 1].
          End scores = (34, 7)
          >>> print(turns[3])
          Start scores = (34, 7).
          Player 1 rolls 10 dice and gets outcomes [6, 2, 3, 4, 2, 4, 5, 6, 1, 1].
          End scores = (34, 8)
          >>> print(turns[4])
          Start scores = (34, 8).
          Player 0 rolls 2 dice and gets outcomes [3, 4].
          End scores = (41, 8)
          >>> print(turns[5])
          Start scores = (41, 8).
          Player 1 rolls 4 dice and gets outcomes [5, 2, 2, 2].
          End scores = (41, 19)
          >>> print(turns[6])
          Start scores = (41, 19).
          Player 0 rolls 9 dice and gets outcomes [2, 2, 4, 2, 1, 2, 5, 3, 4].
          End scores = (42, 19)
          >>> print(turns[7])
          Start scores = (42, 19).
          Player 1 rolls 2 dice and gets outcomes [2, 4].
          End scores = (42, 25)
          >>> print(turns[8])
          Start scores = (42, 25).
          Player 0 rolls 9 dice and gets outcomes [5, 4, 6, 4, 1, 6, 2, 5, 2].
          End scores = (43, 25)
          >>> print(turns[9])
          Start scores = (43, 25).
          Player 1 rolls 6 dice and gets outcomes [5, 1, 6, 1, 1, 4].
          End scores = (43, 26)
          >>> print(turns[10])
          Start scores = (43, 26).
          Player 0 rolls 8 dice and gets outcomes [1, 4, 3, 2, 6, 2, 3, 6].
          End scores = (44, 26)
          >>> print(turns[11])
          Start scores = (44, 26).
          Player 1 rolls 6 dice and gets outcomes [4, 4, 6, 2, 5, 5].
          End scores = (44, 52)
          >>> print(turns[12])
          Start scores = (44, 52).
          Player 0 rolls 10 dice and gets outcomes [4, 2, 3, 4, 2, 3, 4, 6, 3, 5].
          End scores = (80, 52)
          >>> print(turns[13])
          Start scores = (80, 52).
          Player 1 rolls 6 dice and gets outcomes [4, 2, 4, 2, 6, 6].
          End scores = (80, 76)
          >>> print(turns[14])
          Start scores = (80, 76).
          Player 0 rolls 5 dice and gets outcomes [1, 4, 5, 1, 1].
          End scores = (81, 76)
          >>> print(turns[15])
          Start scores = (81, 76).
          Player 1 rolls 7 dice and gets outcomes [5, 2, 3, 4, 2, 3, 4].
          End scores = (81, 99)
          >>> print(turns[16])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=33634, score0=48, score1=74, goal=92)
          >>> print(turns[0])
          Start scores = (48, 74).
          Player 0 rolls 8 dice and gets outcomes [3, 5, 1, 3, 3, 4, 3, 1].
          End scores = (49, 74)
          >>> print(turns[1])
          Start scores = (49, 74).
          Player 1 rolls 8 dice and gets outcomes [3, 6, 3, 3, 4, 6, 6, 2].
          End scores = (49, 107)
          >>> print(turns[2])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=22855, score0=12, score1=22, goal=98)
          >>> print(turns[0])
          Start scores = (12, 22).
          Player 0 rolls 8 dice and gets outcomes [3, 6, 5, 3, 3, 2, 5, 3].
          End scores = (42, 22)
          >>> print(turns[1])
          Start scores = (42, 22).
          Player 1 rolls 6 dice and gets outcomes [3, 5, 2, 6, 4, 6].
          End scores = (42, 48)
          >>> print(turns[2])
          Start scores = (42, 48).
          Player 0 rolls 4 dice and gets outcomes [2, 3, 1, 4].
          End scores = (43, 48)
          >>> print(turns[3])
          Start scores = (43, 48).
          Player 1 rolls 8 dice and gets outcomes [4, 1, 4, 5, 5, 3, 1, 2].
          End scores = (43, 49)
          >>> print(turns[4])
          Start scores = (43, 49).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (46, 49)
          >>> print(turns[5])
          Start scores = (46, 49).
          Player 1 rolls 3 dice and gets outcomes [6, 6, 2].
          End scores = (46, 63)
          >>> print(turns[6])
          Start scores = (46, 63).
          Player 0 rolls 10 dice and gets outcomes [3, 3, 4, 1, 3, 1, 2, 2, 5, 3].
          End scores = (47, 63)
          >>> print(turns[7])
          Start scores = (47, 63).
          Player 1 rolls 8 dice and gets outcomes [2, 4, 5, 4, 6, 6, 3, 5].
          End scores = (47, 98)
          >>> print(turns[8])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=49015, score0=12, score1=5, goal=82)
          >>> print(turns[0])
          Start scores = (12, 5).
          Player 0 rolls 8 dice and gets outcomes [1, 3, 2, 1, 5, 1, 4, 1].
          End scores = (13, 5)
          >>> print(turns[1])
          Start scores = (13, 5).
          Player 1 rolls 10 dice and gets outcomes [1, 6, 2, 5, 5, 6, 5, 4, 1, 2].
          End scores = (13, 6)
          >>> print(turns[2])
          Start scores = (13, 6).
          Player 0 rolls 6 dice and gets outcomes [2, 4, 2, 4, 2, 5].
          End scores = (32, 6)
          >>> print(turns[3])
          Start scores = (32, 6).
          Player 1 rolls 4 dice and gets outcomes [3, 5, 6, 6].
          End scores = (32, 26)
          >>> print(turns[4])
          Start scores = (32, 26).
          Player 0 rolls 7 dice and gets outcomes [3, 5, 4, 5, 3, 2, 1].
          End scores = (33, 26)
          >>> print(turns[5])
          Start scores = (33, 26).
          Player 1 rolls 5 dice and gets outcomes [6, 3, 1, 4, 1].
          End scores = (33, 27)
          >>> print(turns[6])
          Start scores = (33, 27).
          Player 0 rolls 6 dice and gets outcomes [6, 4, 6, 2, 2, 4].
          End scores = (57, 27)
          >>> print(turns[7])
          Start scores = (57, 27).
          Player 1 rolls 5 dice and gets outcomes [6, 3, 4, 6, 2].
          End scores = (57, 48)
          >>> print(turns[8])
          Start scores = (57, 48).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (60, 48)
          >>> print(turns[9])
          Start scores = (60, 48).
          Player 1 rolls 1 dice and gets outcomes [6].
          End scores = (60, 54)
          >>> print(turns[10])
          Start scores = (60, 54).
          Player 0 rolls 5 dice and gets outcomes [2, 5, 4, 4, 3].
          End scores = (78, 54)
          >>> print(turns[11])
          Start scores = (78, 54).
          Player 1 rolls 8 dice and gets outcomes [3, 3, 5, 5, 3, 6, 2, 3].
          End scores = (78, 84)
          >>> print(turns[12])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=50497, score0=46, score1=5, goal=51)
          >>> print(turns[0])
          Start scores = (46, 5).
          Player 0 rolls 6 dice and gets outcomes [3, 3, 1, 2, 5, 2].
          End scores = (47, 5)
          >>> print(turns[1])
          Start scores = (47, 5).
          Player 1 rolls 3 dice and gets outcomes [4, 5, 6].
          End scores = (47, 20)
          >>> print(turns[2])
          Start scores = (47, 20).
          Player 1 rolls 5 dice and gets outcomes [6, 2, 3, 3, 3].
          End scores = (47, 37)
          >>> print(turns[3])
          Start scores = (47, 37).
          Player 0 rolls 3 dice and gets outcomes [4, 2, 6].
          End scores = (59, 37)
          >>> print(turns[4])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=42297, score0=6, score1=22, goal=25)
          >>> print(turns[0])
          Start scores = (6, 22).
          Player 0 rolls 2 dice and gets outcomes [6, 1].
          End scores = (7, 22)
          >>> print(turns[1])
          Start scores = (7, 22).
          Player 1 rolls 8 dice and gets outcomes [1, 2, 5, 1, 2, 2, 3, 4].
          End scores = (7, 23)
          >>> print(turns[2])
          Start scores = (7, 23).
          Player 0 rolls 10 dice and gets outcomes [3, 6, 4, 2, 1, 5, 2, 1, 2, 1].
          End scores = (8, 23)
          >>> print(turns[3])
          Start scores = (8, 23).
          Player 1 rolls 10 dice and gets outcomes [1, 1, 2, 5, 6, 5, 6, 4, 6, 4].
          End scores = (8, 24)
          >>> print(turns[4])
          Start scores = (8, 24).
          Player 0 rolls 8 dice and gets outcomes [3, 1, 6, 2, 5, 4, 1, 2].
          End scores = (9, 24)
          >>> print(turns[5])
          Start scores = (9, 24).
          Player 1 rolls 4 dice and gets outcomes [1, 1, 4, 3].
          End scores = (9, 25)
          >>> print(turns[6])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=1726, score0=19, score1=5, goal=52)
          >>> print(turns[0])
          Start scores = (19, 5).
          Player 0 rolls 10 dice and gets outcomes [5, 1, 3, 4, 3, 1, 5, 1, 5, 3].
          End scores = (20, 5)
          >>> print(turns[1])
          Start scores = (20, 5).
          Player 1 rolls 1 dice and gets outcomes [2].
          End scores = (20, 7)
          >>> print(turns[2])
          Start scores = (20, 7).
          Player 0 rolls 10 dice and gets outcomes [2, 3, 3, 5, 6, 2, 6, 4, 6, 6].
          End scores = (63, 7)
          >>> print(turns[3])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=17218, score0=19, score1=10, goal=50)
          >>> print(turns[0])
          Start scores = (19, 10).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (22, 10)
          >>> print(turns[1])
          Start scores = (22, 10).
          Player 1 rolls 1 dice and gets outcomes [3].
          End scores = (22, 13)
          >>> print(turns[2])
          Start scores = (22, 13).
          Player 0 rolls 10 dice and gets outcomes [1, 5, 2, 3, 3, 5, 1, 1, 4, 6].
          End scores = (23, 13)
          >>> print(turns[3])
          Start scores = (23, 13).
          Player 1 rolls 9 dice and gets outcomes [3, 2, 6, 2, 2, 5, 3, 2, 5].
          End scores = (23, 43)
          >>> print(turns[4])
          Start scores = (23, 43).
          Player 0 rolls 1 dice and gets outcomes [3].
          End scores = (26, 43)
          >>> print(turns[5])
          Start scores = (26, 43).
          Player 1 rolls 10 dice and gets outcomes [5, 6, 1, 2, 6, 6, 5, 3, 4, 6].
          End scores = (26, 44)
          >>> print(turns[6])
          Start scores = (26, 44).
          Player 0 rolls 8 dice and gets outcomes [1, 5, 2, 2, 3, 3, 2, 2].
          End scores = (27, 44)
          >>> print(turns[7])
          Start scores = (27, 44).
          Player 1 rolls 6 dice and gets outcomes [5, 5, 5, 6, 5, 3].
          End scores = (27, 73)
          >>> print(turns[8])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=88988, score0=15, score1=95, goal=100)
          >>> print(turns[0])
          Start scores = (15, 95).
          Player 0 rolls 9 dice and gets outcomes [5, 3, 2, 4, 2, 1, 3, 2, 5].
          End scores = (16, 95)
          >>> print(turns[1])
          Start scores = (16, 95).
          Player 1 rolls 10 dice and gets outcomes [6, 4, 3, 2, 6, 4, 6, 1, 2, 1].
          End scores = (16, 96)
          >>> print(turns[2])
          Start scores = (16, 96).
          Player 0 rolls 1 dice and gets outcomes [6].
          End scores = (22, 96)
          >>> print(turns[3])
          Start scores = (22, 96).
          Player 0 rolls 9 dice and gets outcomes [5, 1, 3, 1, 5, 6, 2, 4, 2].
          End scores = (23, 96)
          >>> print(turns[4])
          Start scores = (23, 96).
          Player 0 rolls 7 dice and gets outcomes [2, 3, 6, 1, 4, 4, 1].
          End scores = (24, 96)
          >>> print(turns[5])
          Start scores = (24, 96).
          Player 0 rolls 2 dice and gets outcomes [2, 3].
          End scores = (29, 96)
          >>> print(turns[6])
          Start scores = (29, 96).
          Player 1 rolls 9 dice and gets outcomes [1, 4, 5, 6, 1, 1, 1, 6, 1].
          End scores = (29, 97)
          >>> print(turns[7])
          Start scores = (29, 97).
          Player 0 rolls 5 dice and gets outcomes [5, 6, 1, 3, 2].
          End scores = (30, 97)
          >>> print(turns[8])
          Start scores = (30, 97).
          Player 0 rolls 5 dice and gets outcomes [4, 5, 2, 1, 5].
          End scores = (31, 97)
          >>> print(turns[9])
          Start scores = (31, 97).
          Player 0 rolls 9 dice and gets outcomes [3, 2, 5, 1, 3, 6, 2, 4, 4].
          End scores = (32, 97)
          >>> print(turns[10])
          Start scores = (32, 97).
          Player 0 rolls 4 dice and gets outcomes [4, 3, 5, 3].
          End scores = (47, 97)
          >>> print(turns[11])
          Start scores = (47, 97).
          Player 1 rolls 4 dice and gets outcomes [5, 6, 2, 1].
          End scores = (47, 98)
          >>> print(turns[12])
          Start scores = (47, 98).
          Player 0 rolls 4 dice and gets outcomes [3, 3, 4, 2].
          End scores = (59, 98)
          >>> print(turns[13])
          Start scores = (59, 98).
          Player 1 rolls 8 dice and gets outcomes [3, 5, 5, 3, 1, 3, 5, 3].
          End scores = (59, 99)
          >>> print(turns[14])
          Start scores = (59, 99).
          Player 0 rolls 1 dice and gets outcomes [5].
          End scores = (64, 99)
          >>> print(turns[15])
          Start scores = (64, 99).
          Player 0 rolls 7 dice and gets outcomes [5, 2, 4, 2, 6, 1, 1].
          End scores = (65, 99)
          >>> print(turns[16])
          Start scores = (65, 99).
          Player 0 rolls 7 dice and gets outcomes [2, 2, 2, 5, 6, 5, 6].
          End scores = (93, 99)
          >>> print(turns[17])
          Start scores = (93, 99).
          Player 1 rolls 10 dice and gets outcomes [1, 6, 5, 2, 4, 4, 5, 6, 4, 1].
          End scores = (93, 100)
          >>> print(turns[18])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=8964, score0=79, score1=56, goal=83)
          >>> print(turns[0])
          Start scores = (79, 56).
          Player 0 rolls 7 dice and gets outcomes [5, 2, 3, 6, 6, 1, 6].
          End scores = (80, 56)
          >>> print(turns[1])
          Start scores = (80, 56).
          Player 1 rolls 4 dice and gets outcomes [1, 2, 5, 1].
          End scores = (80, 57)
          >>> print(turns[2])
          Start scores = (80, 57).
          Player 0 rolls 9 dice and gets outcomes [2, 5, 6, 3, 5, 6, 6, 1, 4].
          End scores = (81, 57)
          >>> print(turns[3])
          Start scores = (81, 57).
          Player 1 rolls 8 dice and gets outcomes [6, 3, 3, 3, 3, 2, 6, 3].
          End scores = (81, 86)
          >>> print(turns[4])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=24932, score0=12, score1=0, goal=14)
          >>> print(turns[0])
          Start scores = (12, 0).
          Player 0 rolls 6 dice and gets outcomes [1, 1, 1, 3, 3, 2].
          End scores = (13, 0)
          >>> print(turns[1])
          Start scores = (13, 0).
          Player 1 rolls 8 dice and gets outcomes [4, 1, 5, 4, 3, 3, 5, 1].
          End scores = (13, 1)
          >>> print(turns[2])
          Start scores = (13, 1).
          Player 1 rolls 7 dice and gets outcomes [5, 3, 2, 3, 5, 2, 1].
          End scores = (13, 2)
          >>> print(turns[3])
          Start scores = (13, 2).
          Player 1 rolls 9 dice and gets outcomes [6, 6, 3, 4, 3, 6, 2, 5, 6].
          End scores = (13, 43)
          >>> print(turns[4])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=76726, score0=40, score1=73, goal=93)
          >>> print(turns[0])
          Start scores = (40, 73).
          Player 0 rolls 5 dice and gets outcomes [6, 6, 1, 2, 5].
          End scores = (41, 73)
          >>> print(turns[1])
          Start scores = (41, 73).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (46, 73)
          >>> print(turns[2])
          Start scores = (46, 73).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (46, 77)
          >>> print(turns[3])
          Start scores = (46, 77).
          Player 0 rolls 1 dice and gets outcomes [6].
          End scores = (52, 77)
          >>> print(turns[4])
          Start scores = (52, 77).
          Player 0 rolls 8 dice and gets outcomes [1, 4, 2, 1, 6, 1, 6, 4].
          End scores = (53, 77)
          >>> print(turns[5])
          Start scores = (53, 77).
          Player 0 rolls 5 dice and gets outcomes [2, 5, 4, 1, 6].
          End scores = (54, 77)
          >>> print(turns[6])
          Start scores = (54, 77).
          Player 0 rolls 5 dice and gets outcomes [2, 5, 5, 3, 6].
          End scores = (75, 77)
          >>> print(turns[7])
          Start scores = (75, 77).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (75, 82)
          >>> print(turns[8])
          Start scores = (75, 82).
          Player 0 rolls 5 dice and gets outcomes [1, 2, 2, 5, 2].
          End scores = (76, 82)
          >>> print(turns[9])
          Start scores = (76, 82).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (76, 90)
          >>> print(turns[10])
          Start scores = (76, 90).
          Player 0 rolls 2 dice and gets outcomes [4, 5].
          End scores = (85, 90)
          >>> print(turns[11])
          Start scores = (85, 90).
          Player 1 rolls 10 dice and gets outcomes [6, 2, 5, 4, 2, 3, 3, 6, 3, 1].
          End scores = (85, 91)
          >>> print(turns[12])
          Start scores = (85, 91).
          Player 0 rolls 3 dice and gets outcomes [2, 3, 3].
          End scores = (93, 91)
          >>> print(turns[13])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=85393, score0=3, score1=0, goal=44)
          >>> print(turns[0])
          Start scores = (3, 0).
          Player 0 rolls 3 dice and gets outcomes [3, 2, 5].
          End scores = (13, 0)
          >>> print(turns[1])
          Start scores = (13, 0).
          Player 1 rolls 6 dice and gets outcomes [1, 6, 3, 2, 6, 5].
          End scores = (13, 1)
          >>> print(turns[2])
          Start scores = (13, 1).
          Player 1 rolls 1 dice and gets outcomes [3].
          End scores = (13, 4)
          >>> print(turns[3])
          Start scores = (13, 4).
          Player 0 rolls 1 dice and gets outcomes [4].
          End scores = (17, 4)
          >>> print(turns[4])
          Start scores = (17, 4).
          Player 1 rolls 6 dice and gets outcomes [2, 4, 6, 3, 2, 1].
          End scores = (17, 5)
          >>> print(turns[5])
          Start scores = (17, 5).
          Player 1 rolls 7 dice and gets outcomes [1, 2, 3, 4, 3, 2, 5].
          End scores = (17, 6)
          >>> print(turns[6])
          Start scores = (17, 6).
          Player 1 rolls 9 dice and gets outcomes [1, 6, 1, 1, 1, 1, 6, 4, 4].
          End scores = (17, 7)
          >>> print(turns[7])
          Start scores = (17, 7).
          Player 0 rolls 6 dice and gets outcomes [3, 4, 4, 1, 6, 2].
          End scores = (18, 7)
          >>> print(turns[8])
          Start scores = (18, 7).
          Player 1 rolls 10 dice and gets outcomes [3, 5, 1, 1, 4, 6, 1, 3, 4, 6].
          End scores = (18, 8)
          >>> print(turns[9])
          Start scores = (18, 8).
          Player 0 rolls 1 dice and gets outcomes [5].
          End scores = (23, 8)
          >>> print(turns[10])
          Start scores = (23, 8).
          Player 1 rolls 9 dice and gets outcomes [3, 1, 1, 2, 6, 3, 2, 4, 1].
          End scores = (23, 9)
          >>> print(turns[11])
          Start scores = (23, 9).
          Player 0 rolls 9 dice and gets outcomes [5, 4, 2, 1, 1, 1, 4, 6, 2].
          End scores = (24, 9)
          >>> print(turns[12])
          Start scores = (24, 9).
          Player 1 rolls 2 dice and gets outcomes [5, 6].
          End scores = (24, 20)
          >>> print(turns[13])
          Start scores = (24, 20).
          Player 0 rolls 5 dice and gets outcomes [4, 6, 2, 6, 6].
          End scores = (48, 20)
          >>> print(turns[14])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=35702, score0=10, score1=13, goal=14)
          >>> print(turns[0])
          Start scores = (10, 13).
          Player 0 rolls 4 dice and gets outcomes [5, 4, 6, 2].
          End scores = (27, 13)
          >>> print(turns[1])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=75713, score0=62, score1=6, goal=63)
          >>> print(turns[0])
          Start scores = (62, 6).
          Player 0 rolls 7 dice and gets outcomes [1, 6, 2, 6, 4, 4, 6].
          End scores = (63, 6)
          >>> print(turns[1])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=14879, score0=24, score1=8, goal=29)
          >>> print(turns[0])
          Start scores = (24, 8).
          Player 0 rolls 4 dice and gets outcomes [1, 1, 6, 6].
          End scores = (25, 8)
          >>> print(turns[1])
          Start scores = (25, 8).
          Player 1 rolls 8 dice and gets outcomes [2, 6, 5, 1, 4, 6, 3, 4].
          End scores = (25, 9)
          >>> print(turns[2])
          Start scores = (25, 9).
          Player 0 rolls 3 dice and gets outcomes [6, 3, 3].
          End scores = (37, 9)
          >>> print(turns[3])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=62742, score0=9, score1=5, goal=11)
          >>> print(turns[0])
          Start scores = (9, 5).
          Player 0 rolls 3 dice and gets outcomes [3, 2, 4].
          End scores = (18, 5)
          >>> print(turns[1])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=99168, score0=34, score1=40, goal=95)
          >>> print(turns[0])
          Start scores = (34, 40).
          Player 0 rolls 1 dice and gets outcomes [1].
          End scores = (35, 40)
          >>> print(turns[1])
          Start scores = (35, 40).
          Player 1 rolls 3 dice and gets outcomes [5, 2, 5].
          End scores = (35, 52)
          >>> print(turns[2])
          Start scores = (35, 52).
          Player 0 rolls 9 dice and gets outcomes [1, 5, 5, 2, 6, 4, 4, 3, 1].
          End scores = (36, 52)
          >>> print(turns[3])
          Start scores = (36, 52).
          Player 1 rolls 5 dice and gets outcomes [4, 1, 5, 4, 4].
          End scores = (36, 53)
          >>> print(turns[4])
          Start scores = (36, 53).
          Player 0 rolls 1 dice and gets outcomes [6].
          End scores = (42, 53)
          >>> print(turns[5])
          Start scores = (42, 53).
          Player 0 rolls 5 dice and gets outcomes [1, 3, 5, 5, 2].
          End scores = (43, 53)
          >>> print(turns[6])
          Start scores = (43, 53).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (43, 57)
          >>> print(turns[7])
          Start scores = (43, 57).
          Player 0 rolls 9 dice and gets outcomes [1, 5, 1, 2, 2, 4, 5, 2, 1].
          End scores = (44, 57)
          >>> print(turns[8])
          Start scores = (44, 57).
          Player 0 rolls 10 dice and gets outcomes [5, 2, 6, 1, 6, 1, 1, 5, 1, 1].
          End scores = (45, 57)
          >>> print(turns[9])
          Start scores = (45, 57).
          Player 0 rolls 4 dice and gets outcomes [5, 3, 6, 3].
          End scores = (62, 57)
          >>> print(turns[10])
          Start scores = (62, 57).
          Player 1 rolls 1 dice and gets outcomes [6].
          End scores = (62, 63)
          >>> print(turns[11])
          Start scores = (62, 63).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (68, 63)
          >>> print(turns[12])
          Start scores = (68, 63).
          Player 1 rolls 7 dice and gets outcomes [1, 3, 2, 2, 3, 2, 4].
          End scores = (68, 64)
          >>> print(turns[13])
          Start scores = (68, 64).
          Player 0 rolls 8 dice and gets outcomes [6, 2, 4, 1, 3, 2, 3, 3].
          End scores = (69, 64)
          >>> print(turns[14])
          Start scores = (69, 64).
          Player 1 rolls 6 dice and gets outcomes [3, 5, 2, 3, 1, 3].
          End scores = (69, 65)
          >>> print(turns[15])
          Start scores = (69, 65).
          Player 0 rolls 6 dice and gets outcomes [1, 1, 1, 6, 5, 3].
          End scores = (70, 65)
          >>> print(turns[16])
          Start scores = (70, 65).
          Player 1 rolls 7 dice and gets outcomes [2, 1, 1, 1, 2, 4, 1].
          End scores = (70, 66)
          >>> print(turns[17])
          Start scores = (70, 66).
          Player 0 rolls 3 dice and gets outcomes [5, 1, 6].
          End scores = (71, 66)
          >>> print(turns[18])
          Start scores = (71, 66).
          Player 1 rolls 9 dice and gets outcomes [1, 5, 6, 5, 2, 2, 4, 3, 6].
          End scores = (71, 67)
          >>> print(turns[19])
          Start scores = (71, 67).
          Player 0 rolls 10 dice and gets outcomes [5, 1, 5, 6, 5, 1, 2, 5, 2, 3].
          End scores = (72, 67)
          >>> print(turns[20])
          Start scores = (72, 67).
          Player 1 rolls 2 dice and gets outcomes [6, 4].
          End scores = (72, 77)
          >>> print(turns[21])
          Start scores = (72, 77).
          Player 0 rolls 10 dice and gets outcomes [4, 5, 3, 5, 2, 4, 2, 6, 2, 2].
          End scores = (107, 77)
          >>> print(turns[22])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=98804, score0=37, score1=45, goal=47)
          >>> print(turns[0])
          Start scores = (37, 45).
          Player 0 rolls 4 dice and gets outcomes [1, 3, 3, 2].
          End scores = (38, 45)
          >>> print(turns[1])
          Start scores = (38, 45).
          Player 1 rolls 8 dice and gets outcomes [6, 5, 5, 3, 5, 5, 4, 3].
          End scores = (38, 81)
          >>> print(turns[2])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=27518, score0=87, score1=16, goal=92)
          >>> print(turns[0])
          Start scores = (87, 16).
          Player 0 rolls 7 dice and gets outcomes [6, 1, 6, 6, 1, 5, 2].
          End scores = (88, 16)
          >>> print(turns[1])
          Start scores = (88, 16).
          Player 1 rolls 2 dice and gets outcomes [6, 1].
          End scores = (88, 17)
          >>> print(turns[2])
          Start scores = (88, 17).
          Player 1 rolls 8 dice and gets outcomes [6, 5, 4, 2, 4, 5, 5, 4].
          End scores = (88, 52)
          >>> print(turns[3])
          Start scores = (88, 52).
          Player 1 rolls 9 dice and gets outcomes [2, 1, 1, 1, 6, 2, 2, 2, 2].
          End scores = (88, 53)
          >>> print(turns[4])
          Start scores = (88, 53).
          Player 1 rolls 1 dice and gets outcomes [3].
          End scores = (88, 56)
          >>> print(turns[5])
          Start scores = (88, 56).
          Player 1 rolls 10 dice and gets outcomes [2, 2, 6, 5, 1, 2, 5, 1, 2, 2].
          End scores = (88, 57)
          >>> print(turns[6])
          Start scores = (88, 57).
          Player 1 rolls 6 dice and gets outcomes [1, 3, 1, 3, 5, 4].
          End scores = (88, 58)
          >>> print(turns[7])
          Start scores = (88, 58).
          Player 0 rolls 3 dice and gets outcomes [2, 6, 1].
          End scores = (89, 58)
          >>> print(turns[8])
          Start scores = (89, 58).
          Player 1 rolls 8 dice and gets outcomes [6, 4, 1, 4, 5, 6, 6, 3].
          End scores = (89, 59)
          >>> print(turns[9])
          Start scores = (89, 59).
          Player 0 rolls 4 dice and gets outcomes [5, 5, 5, 5].
          End scores = (109, 59)
          >>> print(turns[10])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=75062, score0=43, score1=5, goal=97)
          >>> print(turns[0])
          Start scores = (43, 5).
          Player 0 rolls 8 dice and gets outcomes [6, 1, 4, 5, 6, 6, 5, 3].
          End scores = (44, 5)
          >>> print(turns[1])
          Start scores = (44, 5).
          Player 1 rolls 4 dice and gets outcomes [5, 5, 2, 4].
          End scores = (44, 21)
          >>> print(turns[2])
          Start scores = (44, 21).
          Player 1 rolls 2 dice and gets outcomes [6, 2].
          End scores = (44, 29)
          >>> print(turns[3])
          Start scores = (44, 29).
          Player 0 rolls 7 dice and gets outcomes [1, 1, 5, 3, 3, 4, 5].
          End scores = (45, 29)
          >>> print(turns[4])
          Start scores = (45, 29).
          Player 1 rolls 6 dice and gets outcomes [5, 4, 6, 1, 6, 6].
          End scores = (45, 30)
          >>> print(turns[5])
          Start scores = (45, 30).
          Player 1 rolls 10 dice and gets outcomes [6, 5, 3, 2, 5, 2, 5, 3, 2, 6].
          End scores = (45, 69)
          >>> print(turns[6])
          Start scores = (45, 69).
          Player 0 rolls 3 dice and gets outcomes [1, 1, 5].
          End scores = (46, 69)
          >>> print(turns[7])
          Start scores = (46, 69).
          Player 0 rolls 5 dice and gets outcomes [1, 4, 6, 5, 5].
          End scores = (47, 69)
          >>> print(turns[8])
          Start scores = (47, 69).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (51, 69)
          >>> print(turns[9])
          Start scores = (51, 69).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (55, 69)
          >>> print(turns[10])
          Start scores = (55, 69).
          Player 0 rolls 2 dice and gets outcomes [1, 1].
          End scores = (56, 69)
          >>> print(turns[11])
          Start scores = (56, 69).
          Player 0 rolls 8 dice and gets outcomes [4, 1, 2, 5, 6, 6, 3, 6].
          End scores = (57, 69)
          >>> print(turns[12])
          Start scores = (57, 69).
          Player 0 rolls 1 dice and gets outcomes [2].
          End scores = (59, 69)
          >>> print(turns[13])
          Start scores = (59, 69).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (59, 73)
          >>> print(turns[14])
          Start scores = (59, 73).
          Player 0 rolls 9 dice and gets outcomes [2, 5, 1, 4, 5, 4, 5, 5, 2].
          End scores = (60, 73)
          >>> print(turns[15])
          Start scores = (60, 73).
          Player 0 rolls 1 dice and gets outcomes [1].
          End scores = (61, 73)
          >>> print(turns[16])
          Start scores = (61, 73).
          Player 0 rolls 8 dice and gets outcomes [6, 5, 1, 4, 2, 4, 5, 6].
          End scores = (62, 73)
          >>> print(turns[17])
          Start scores = (62, 73).
          Player 0 rolls 7 dice and gets outcomes [2, 2, 5, 3, 6, 5, 1].
          End scores = (63, 73)
          >>> print(turns[18])
          Start scores = (63, 73).
          Player 1 rolls 5 dice and gets outcomes [3, 1, 3, 2, 3].
          End scores = (63, 74)
          >>> print(turns[19])
          Start scores = (63, 74).
          Player 0 rolls 6 dice and gets outcomes [6, 1, 6, 3, 1, 2].
          End scores = (64, 74)
          >>> print(turns[20])
          Start scores = (64, 74).
          Player 1 rolls 5 dice and gets outcomes [3, 1, 1, 5, 2].
          End scores = (64, 75)
          >>> print(turns[21])
          Start scores = (64, 75).
          Player 0 rolls 7 dice and gets outcomes [3, 5, 5, 5, 2, 3, 4].
          End scores = (91, 75)
          >>> print(turns[22])
          Start scores = (91, 75).
          Player 1 rolls 7 dice and gets outcomes [4, 3, 3, 4, 5, 3, 1].
          End scores = (91, 76)
          >>> print(turns[23])
          Start scores = (91, 76).
          Player 0 rolls 4 dice and gets outcomes [3, 5, 5, 2].
          End scores = (106, 76)
          >>> print(turns[24])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=578, score0=7, score1=24, goal=30)
          >>> print(turns[0])
          Start scores = (7, 24).
          Player 0 rolls 10 dice and gets outcomes [1, 1, 3, 2, 5, 2, 5, 6, 6, 2].
          End scores = (8, 24)
          >>> print(turns[1])
          Start scores = (8, 24).
          Player 1 rolls 2 dice and gets outcomes [6, 3].
          End scores = (8, 33)
          >>> print(turns[2])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=93942, score0=42, score1=41, goal=43)
          >>> print(turns[0])
          Start scores = (42, 41).
          Player 0 rolls 7 dice and gets outcomes [3, 6, 3, 3, 2, 6, 1].
          End scores = (43, 41)
          >>> print(turns[1])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=48161, score0=15, score1=55, goal=83)
          >>> print(turns[0])
          Start scores = (15, 55).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (18, 55)
          >>> print(turns[1])
          Start scores = (18, 55).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (18, 60)
          >>> print(turns[2])
          Start scores = (18, 60).
          Player 0 rolls 9 dice and gets outcomes [1, 4, 5, 6, 3, 6, 5, 4, 2].
          End scores = (19, 60)
          >>> print(turns[3])
          Start scores = (19, 60).
          Player 1 rolls 1 dice and gets outcomes [5].
          End scores = (19, 65)
          >>> print(turns[4])
          Start scores = (19, 65).
          Player 0 rolls 5 dice and gets outcomes [3, 1, 3, 4, 3].
          End scores = (20, 65)
          >>> print(turns[5])
          Start scores = (20, 65).
          Player 0 rolls 8 dice and gets outcomes [1, 6, 6, 1, 3, 2, 2, 5].
          End scores = (21, 65)
          >>> print(turns[6])
          Start scores = (21, 65).
          Player 0 rolls 9 dice and gets outcomes [3, 6, 1, 3, 1, 2, 5, 4, 5].
          End scores = (22, 65)
          >>> print(turns[7])
          Start scores = (22, 65).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (27, 65)
          >>> print(turns[8])
          Start scores = (27, 65).
          Player 1 rolls 1 dice and gets outcomes [4].
          End scores = (27, 69)
          >>> print(turns[9])
          Start scores = (27, 69).
          Player 0 rolls 1 dice and gets outcomes [5].
          End scores = (32, 69)
          >>> print(turns[10])
          Start scores = (32, 69).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (36, 69)
          >>> print(turns[11])
          Start scores = (36, 69).
          Player 0 rolls 1 dice and gets outcomes [4].
          End scores = (40, 69)
          >>> print(turns[12])
          Start scores = (40, 69).
          Player 0 rolls 3 dice and gets outcomes [4, 2, 1].
          End scores = (41, 69)
          >>> print(turns[13])
          Start scores = (41, 69).
          Player 0 rolls 7 dice and gets outcomes [3, 3, 3, 3, 6, 3, 2].
          End scores = (64, 69)
          >>> print(turns[14])
          Start scores = (64, 69).
          Player 1 rolls 1 dice and gets outcomes [2].
          End scores = (64, 71)
          >>> print(turns[15])
          Start scores = (64, 71).
          Player 0 rolls 1 dice and gets outcomes [6].
          End scores = (70, 71)
          >>> print(turns[16])
          Start scores = (70, 71).
          Player 1 rolls 3 dice and gets outcomes [4, 3, 2].
          End scores = (70, 80)
          >>> print(turns[17])
          Start scores = (70, 80).
          Player 0 rolls 3 dice and gets outcomes [1, 5, 4].
          End scores = (71, 80)
          >>> print(turns[18])
          Start scores = (71, 80).
          Player 1 rolls 8 dice and gets outcomes [1, 1, 6, 3, 4, 3, 1, 6].
          End scores = (71, 81)
          >>> print(turns[19])
          Start scores = (71, 81).
          Player 0 rolls 6 dice and gets outcomes [4, 2, 3, 1, 6, 2].
          End scores = (72, 81)
          >>> print(turns[20])
          Start scores = (72, 81).
          Player 1 rolls 6 dice and gets outcomes [5, 1, 2, 2, 6, 5].
          End scores = (72, 82)
          >>> print(turns[21])
          Start scores = (72, 82).
          Player 0 rolls 5 dice and gets outcomes [2, 1, 5, 3, 1].
          End scores = (73, 82)
          >>> print(turns[22])
          Start scores = (73, 82).
          Player 1 rolls 2 dice and gets outcomes [4, 2].
          End scores = (73, 88)
          >>> print(turns[23])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=52136, score0=2, score1=14, goal=15)
          >>> print(turns[0])
          Start scores = (2, 14).
          Player 0 rolls 4 dice and gets outcomes [3, 3, 1, 5].
          End scores = (3, 14)
          >>> print(turns[1])
          Start scores = (3, 14).
          Player 0 rolls 3 dice and gets outcomes [1, 5, 2].
          End scores = (4, 14)
          >>> print(turns[2])
          Start scores = (4, 14).
          Player 1 rolls 3 dice and gets outcomes [4, 6, 6].
          End scores = (4, 30)
          >>> print(turns[3])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=30971, score0=11, score1=12, goal=25)
          >>> print(turns[0])
          Start scores = (11, 12).
          Player 0 rolls 9 dice and gets outcomes [2, 2, 1, 2, 6, 5, 4, 6, 3].
          End scores = (12, 12)
          >>> print(turns[1])
          Start scores = (12, 12).
          Player 1 rolls 4 dice and gets outcomes [3, 6, 4, 1].
          End scores = (12, 13)
          >>> print(turns[2])
          Start scores = (12, 13).
          Player 0 rolls 6 dice and gets outcomes [3, 3, 6, 5, 3, 5].
          End scores = (37, 13)
          >>> print(turns[3])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=69948, score0=11, score1=19, goal=43)
          >>> print(turns[0])
          Start scores = (11, 19).
          Player 0 rolls 9 dice and gets outcomes [1, 5, 6, 6, 2, 6, 1, 6, 4].
          End scores = (12, 19)
          >>> print(turns[1])
          Start scores = (12, 19).
          Player 1 rolls 6 dice and gets outcomes [2, 3, 5, 6, 1, 3].
          End scores = (12, 20)
          >>> print(turns[2])
          Start scores = (12, 20).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (15, 20)
          >>> print(turns[3])
          Start scores = (15, 20).
          Player 1 rolls 10 dice and gets outcomes [1, 6, 4, 5, 6, 6, 5, 6, 2, 3].
          End scores = (15, 21)
          >>> print(turns[4])
          Start scores = (15, 21).
          Player 0 rolls 9 dice and gets outcomes [5, 4, 6, 5, 5, 2, 3, 3, 4].
          End scores = (52, 21)
          >>> print(turns[5])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=33856, score0=9, score1=9, goal=19)
          >>> print(turns[0])
          Start scores = (9, 9).
          Player 0 rolls 1 dice and gets outcomes [3].
          End scores = (12, 9)
          >>> print(turns[1])
          Start scores = (12, 9).
          Player 1 rolls 3 dice and gets outcomes [5, 5, 6].
          End scores = (12, 25)
          >>> print(turns[2])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=93176, score0=7, score1=37, goal=80)
          >>> print(turns[0])
          Start scores = (7, 37).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (11, 37)
          >>> print(turns[1])
          Start scores = (11, 37).
          Player 0 rolls 2 dice and gets outcomes [6, 6].
          End scores = (23, 37)
          >>> print(turns[2])
          Start scores = (23, 37).
          Player 0 rolls 6 dice and gets outcomes [6, 6, 3, 6, 4, 6].
          End scores = (54, 37)
          >>> print(turns[3])
          Start scores = (54, 37).
          Player 1 rolls 5 dice and gets outcomes [4, 1, 3, 2, 6].
          End scores = (54, 38)
          >>> print(turns[4])
          Start scores = (54, 38).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (58, 38)
          >>> print(turns[5])
          Start scores = (58, 38).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (58, 44)
          >>> print(turns[6])
          Start scores = (58, 44).
          Player 1 rolls 2 dice and gets outcomes [4, 6].
          End scores = (58, 54)
          >>> print(turns[7])
          Start scores = (58, 54).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (62, 54)
          >>> print(turns[8])
          Start scores = (62, 54).
          Player 1 rolls 5 dice and gets outcomes [1, 4, 4, 5, 5].
          End scores = (62, 55)
          >>> print(turns[9])
          Start scores = (62, 55).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (65, 55)
          >>> print(turns[10])
          Start scores = (65, 55).
          Player 1 rolls 8 dice and gets outcomes [3, 1, 5, 1, 2, 1, 2, 3].
          End scores = (65, 56)
          >>> print(turns[11])
          Start scores = (65, 56).
          Player 0 rolls 8 dice and gets outcomes [6, 1, 4, 5, 4, 4, 4, 6].
          End scores = (66, 56)
          >>> print(turns[12])
          Start scores = (66, 56).
          Player 1 rolls 5 dice and gets outcomes [4, 1, 1, 1, 5].
          End scores = (66, 57)
          >>> print(turns[13])
          Start scores = (66, 57).
          Player 0 rolls 1 dice and gets outcomes [5].
          End scores = (71, 57)
          >>> print(turns[14])
          Start scores = (71, 57).
          Player 1 rolls 10 dice and gets outcomes [3, 1, 2, 4, 2, 1, 5, 3, 4, 5].
          End scores = (71, 58)
          >>> print(turns[15])
          Start scores = (71, 58).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (77, 58)
          >>> print(turns[16])
          Start scores = (77, 58).
          Player 1 rolls 6 dice and gets outcomes [2, 6, 4, 5, 2, 6].
          End scores = (77, 83)
          >>> print(turns[17])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=85986, score0=35, score1=12, goal=74)
          >>> print(turns[0])
          Start scores = (35, 12).
          Player 0 rolls 10 dice and gets outcomes [6, 2, 3, 4, 3, 3, 6, 5, 1, 2].
          End scores = (36, 12)
          >>> print(turns[1])
          Start scores = (36, 12).
          Player 1 rolls 4 dice and gets outcomes [5, 3, 6, 1].
          End scores = (36, 13)
          >>> print(turns[2])
          Start scores = (36, 13).
          Player 1 rolls 8 dice and gets outcomes [2, 3, 3, 6, 4, 2, 5, 1].
          End scores = (36, 14)
          >>> print(turns[3])
          Start scores = (36, 14).
          Player 1 rolls 1 dice and gets outcomes [6].
          End scores = (36, 20)
          >>> print(turns[4])
          Start scores = (36, 20).
          Player 1 rolls 2 dice and gets outcomes [3, 6].
          End scores = (36, 29)
          >>> print(turns[5])
          Start scores = (36, 29).
          Player 0 rolls 5 dice and gets outcomes [4, 3, 3, 5, 2].
          End scores = (53, 29)
          >>> print(turns[6])
          Start scores = (53, 29).
          Player 1 rolls 3 dice and gets outcomes [2, 3, 4].
          End scores = (53, 38)
          >>> print(turns[7])
          Start scores = (53, 38).
          Player 0 rolls 9 dice and gets outcomes [5, 6, 3, 6, 5, 5, 5, 3, 5].
          End scores = (96, 38)
          >>> print(turns[8])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=76820, score0=28, score1=14, goal=61)
          >>> print(turns[0])
          Start scores = (28, 14).
          Player 0 rolls 4 dice and gets outcomes [2, 6, 4, 1].
          End scores = (29, 14)
          >>> print(turns[1])
          Start scores = (29, 14).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (29, 18)
          >>> print(turns[2])
          Start scores = (29, 18).
          Player 1 rolls 3 dice and gets outcomes [1, 1, 1].
          End scores = (29, 19)
          >>> print(turns[3])
          Start scores = (29, 19).
          Player 0 rolls 10 dice and gets outcomes [3, 3, 6, 6, 6, 4, 2, 5, 4, 1].
          End scores = (30, 19)
          >>> print(turns[4])
          Start scores = (30, 19).
          Player 1 rolls 6 dice and gets outcomes [5, 5, 3, 6, 5, 4].
          End scores = (30, 47)
          >>> print(turns[5])
          Start scores = (30, 47).
          Player 0 rolls 7 dice and gets outcomes [4, 5, 3, 5, 6, 5, 4].
          End scores = (62, 47)
          >>> print(turns[6])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=83984, score0=64, score1=49, goal=78)
          >>> print(turns[0])
          Start scores = (64, 49).
          Player 0 rolls 7 dice and gets outcomes [3, 5, 3, 5, 6, 3, 4].
          End scores = (93, 49)
          >>> print(turns[1])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=25773, score0=3, score1=17, goal=30)
          >>> print(turns[0])
          Start scores = (3, 17).
          Player 0 rolls 5 dice and gets outcomes [3, 4, 5, 4, 6].
          End scores = (25, 17)
          >>> print(turns[1])
          Start scores = (25, 17).
          Player 1 rolls 3 dice and gets outcomes [2, 1, 4].
          End scores = (25, 18)
          >>> print(turns[2])
          Start scores = (25, 18).
          Player 0 rolls 4 dice and gets outcomes [5, 1, 5, 3].
          End scores = (26, 18)
          >>> print(turns[3])
          Start scores = (26, 18).
          Player 1 rolls 8 dice and gets outcomes [1, 4, 3, 2, 1, 5, 6, 2].
          End scores = (26, 19)
          >>> print(turns[4])
          Start scores = (26, 19).
          Player 0 rolls 9 dice and gets outcomes [6, 5, 6, 2, 1, 5, 2, 1, 1].
          End scores = (27, 19)
          >>> print(turns[5])
          Start scores = (27, 19).
          Player 1 rolls 10 dice and gets outcomes [5, 6, 6, 4, 2, 5, 3, 3, 2, 4].
          End scores = (27, 59)
          >>> print(turns[6])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=6012, score0=30, score1=3, goal=85)
          >>> print(turns[0])
          Start scores = (30, 3).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (42, 3)
          >>> print(turns[1])
          Start scores = (42, 3).
          Player 1 rolls 5 dice and gets outcomes [1, 4, 6, 2, 4].
          End scores = (42, 4)
          >>> print(turns[2])
          Start scores = (42, 4).
          Player 0 rolls 3 dice and gets outcomes [2, 4, 2].
          End scores = (50, 4)
          >>> print(turns[3])
          Start scores = (50, 4).
          Player 1 rolls 8 dice and gets outcomes [4, 3, 3, 4, 6, 4, 4, 6].
          End scores = (50, 38)
          >>> print(turns[4])
          Start scores = (50, 38).
          Player 0 rolls 9 dice and gets outcomes [6, 6, 5, 5, 1, 1, 4, 2, 4].
          End scores = (51, 38)
          >>> print(turns[5])
          Start scores = (51, 38).
          Player 1 rolls 4 dice and gets outcomes [5, 3, 3, 4].
          End scores = (51, 53)
          >>> print(turns[6])
          Start scores = (51, 53).
          Player 0 rolls 3 dice and gets outcomes [1, 1, 5].
          End scores = (52, 53)
          >>> print(turns[7])
          Start scores = (52, 53).
          Player 1 rolls 5 dice and gets outcomes [6, 1, 1, 6, 1].
          End scores = (52, 54)
          >>> print(turns[8])
          Start scores = (52, 54).
          Player 0 rolls 9 dice and gets outcomes [6, 1, 6, 1, 1, 3, 2, 2, 6].
          End scores = (53, 54)
          >>> print(turns[9])
          Start scores = (53, 54).
          Player 1 rolls 4 dice and gets outcomes [3, 6, 5, 1].
          End scores = (53, 55)
          >>> print(turns[10])
          Start scores = (53, 55).
          Player 0 rolls 2 dice and gets outcomes [4, 4].
          End scores = (61, 55)
          >>> print(turns[11])
          Start scores = (61, 55).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (61, 59)
          >>> print(turns[12])
          Start scores = (61, 59).
          Player 0 rolls 4 dice and gets outcomes [1, 4, 6, 4].
          End scores = (62, 59)
          >>> print(turns[13])
          Start scores = (62, 59).
          Player 1 rolls 2 dice and gets outcomes [4, 2].
          End scores = (62, 65)
          >>> print(turns[14])
          Start scores = (62, 65).
          Player 0 rolls 5 dice and gets outcomes [3, 2, 3, 6, 2].
          End scores = (78, 65)
          >>> print(turns[15])
          Start scores = (78, 65).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (78, 68)
          >>> print(turns[16])
          Start scores = (78, 68).
          Player 0 rolls 1 dice and gets outcomes [1].
          End scores = (79, 68)
          >>> print(turns[17])
          Start scores = (79, 68).
          Player 1 rolls 6 dice and gets outcomes [1, 4, 5, 6, 6, 2].
          End scores = (79, 69)
          >>> print(turns[18])
          Start scores = (79, 69).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (83, 69)
          >>> print(turns[19])
          Start scores = (83, 69).
          Player 1 rolls 10 dice and gets outcomes [5, 2, 1, 3, 4, 6, 1, 4, 6, 4].
          End scores = (83, 70)
          >>> print(turns[20])
          Start scores = (83, 70).
          Player 1 rolls 2 dice and gets outcomes [1, 3].
          End scores = (83, 71)
          >>> print(turns[21])
          Start scores = (83, 71).
          Player 1 rolls 1 dice and gets outcomes [1].
          End scores = (83, 72)
          >>> print(turns[22])
          Start scores = (83, 72).
          Player 1 rolls 9 dice and gets outcomes [6, 4, 4, 3, 5, 6, 3, 1, 4].
          End scores = (83, 73)
          >>> print(turns[23])
          Start scores = (83, 73).
          Player 0 rolls 5 dice and gets outcomes [6, 5, 2, 5, 3].
          End scores = (104, 73)
          >>> print(turns[24])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=56692, score0=69, score1=40, goal=71)
          >>> print(turns[0])
          Start scores = (69, 40).
          Player 0 rolls 6 dice and gets outcomes [6, 4, 6, 4, 4, 1].
          End scores = (70, 40)
          >>> print(turns[1])
          Start scores = (70, 40).
          Player 1 rolls 3 dice and gets outcomes [3, 3, 4].
          End scores = (70, 50)
          >>> print(turns[2])
          Start scores = (70, 50).
          Player 0 rolls 4 dice and gets outcomes [5, 5, 6, 2].
          End scores = (88, 50)
          >>> print(turns[3])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=11528, score0=6, score1=7, goal=17)
          >>> print(turns[0])
          Start scores = (6, 7).
          Player 0 rolls 3 dice and gets outcomes [2, 6, 2].
          End scores = (16, 7)
          >>> print(turns[1])
          Start scores = (16, 7).
          Player 1 rolls 8 dice and gets outcomes [6, 3, 1, 5, 2, 6, 5, 5].
          End scores = (16, 8)
          >>> print(turns[2])
          Start scores = (16, 8).
          Player 0 rolls 4 dice and gets outcomes [5, 2, 2, 1].
          End scores = (17, 8)
          >>> print(turns[3])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=95684, score0=3, score1=1, goal=10)
          >>> print(turns[0])
          Start scores = (3, 1).
          Player 0 rolls 1 dice and gets outcomes [3].
          End scores = (6, 1)
          >>> print(turns[1])
          Start scores = (6, 1).
          Player 1 rolls 8 dice and gets outcomes [4, 1, 3, 5, 1, 6, 2, 6].
          End scores = (6, 2)
          >>> print(turns[2])
          Start scores = (6, 2).
          Player 0 rolls 5 dice and gets outcomes [1, 4, 5, 5, 4].
          End scores = (7, 2)
          >>> print(turns[3])
          Start scores = (7, 2).
          Player 1 rolls 2 dice and gets outcomes [3, 3].
          End scores = (7, 8)
          >>> print(turns[4])
          Start scores = (7, 8).
          Player 0 rolls 3 dice and gets outcomes [2, 2, 5].
          End scores = (16, 8)
          >>> print(turns[5])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=81397, score0=45, score1=40, goal=52)
          >>> print(turns[0])
          Start scores = (45, 40).
          Player 0 rolls 3 dice and gets outcomes [6, 5, 3].
          End scores = (59, 40)
          >>> print(turns[1])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=22637, score0=32, score1=11, goal=58)
          >>> print(turns[0])
          Start scores = (32, 11).
          Player 0 rolls 5 dice and gets outcomes [6, 6, 5, 5, 5].
          End scores = (59, 11)
          >>> print(turns[1])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=11998, score0=16, score1=21, goal=67)
          >>> print(turns[0])
          Start scores = (16, 21).
          Player 0 rolls 1 dice and gets outcomes [4].
          End scores = (20, 21)
          >>> print(turns[1])
          Start scores = (20, 21).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (20, 24)
          >>> print(turns[2])
          Start scores = (20, 24).
          Player 0 rolls 8 dice and gets outcomes [2, 3, 5, 6, 3, 3, 6, 2].
          End scores = (50, 24)
          >>> print(turns[3])
          Start scores = (50, 24).
          Player 1 rolls 7 dice and gets outcomes [1, 6, 4, 5, 3, 4, 6].
          End scores = (50, 25)
          >>> print(turns[4])
          Start scores = (50, 25).
          Player 0 rolls 8 dice and gets outcomes [2, 3, 4, 2, 3, 4, 3, 6].
          End scores = (77, 25)
          >>> print(turns[5])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=69783, score0=11, score1=13, goal=38)
          >>> print(turns[0])
          Start scores = (11, 13).
          Player 0 rolls 2 dice and gets outcomes [4, 6].
          End scores = (21, 13)
          >>> print(turns[1])
          Start scores = (21, 13).
          Player 1 rolls 1 dice and gets outcomes [6].
          End scores = (21, 19)
          >>> print(turns[2])
          Start scores = (21, 19).
          Player 0 rolls 8 dice and gets outcomes [4, 4, 5, 6, 4, 3, 5, 1].
          End scores = (22, 19)
          >>> print(turns[3])
          Start scores = (22, 19).
          Player 1 rolls 7 dice and gets outcomes [1, 1, 6, 6, 3, 6, 5].
          End scores = (22, 20)
          >>> print(turns[4])
          Start scores = (22, 20).
          Player 0 rolls 8 dice and gets outcomes [5, 4, 3, 6, 5, 3, 1, 2].
          End scores = (23, 20)
          >>> print(turns[5])
          Start scores = (23, 20).
          Player 1 rolls 1 dice and gets outcomes [2].
          End scores = (23, 22)
          >>> print(turns[6])
          Start scores = (23, 22).
          Player 0 rolls 7 dice and gets outcomes [4, 5, 2, 4, 1, 4, 5].
          End scores = (24, 22)
          >>> print(turns[7])
          Start scores = (24, 22).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (24, 30)
          >>> print(turns[8])
          Start scores = (24, 30).
          Player 0 rolls 10 dice and gets outcomes [1, 5, 4, 1, 3, 4, 3, 3, 5, 2].
          End scores = (25, 30)
          >>> print(turns[9])
          Start scores = (25, 30).
          Player 1 rolls 4 dice and gets outcomes [6, 2, 1, 3].
          End scores = (25, 31)
          >>> print(turns[10])
          Start scores = (25, 31).
          Player 0 rolls 3 dice and gets outcomes [3, 1, 2].
          End scores = (26, 31)
          >>> print(turns[11])
          Start scores = (26, 31).
          Player 1 rolls 3 dice and gets outcomes [6, 5, 3].
          End scores = (26, 45)
          >>> print(turns[12])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=37364, score0=29, score1=22, goal=35)
          >>> print(turns[0])
          Start scores = (29, 22).
          Player 0 rolls 4 dice and gets outcomes [1, 6, 1, 6].
          End scores = (30, 22)
          >>> print(turns[1])
          Start scores = (30, 22).
          Player 1 rolls 3 dice and gets outcomes [5, 6, 6].
          End scores = (30, 39)
          >>> print(turns[2])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=5143, score0=2, score1=15, goal=79)
          >>> print(turns[0])
          Start scores = (2, 15).
          Player 0 rolls 5 dice and gets outcomes [4, 6, 6, 6, 4].
          End scores = (28, 15)
          >>> print(turns[1])
          Start scores = (28, 15).
          Player 1 rolls 1 dice and gets outcomes [4].
          End scores = (28, 19)
          >>> print(turns[2])
          Start scores = (28, 19).
          Player 0 rolls 5 dice and gets outcomes [3, 3, 2, 3, 4].
          End scores = (43, 19)
          >>> print(turns[3])
          Start scores = (43, 19).
          Player 1 rolls 6 dice and gets outcomes [6, 2, 2, 2, 4, 3].
          End scores = (43, 38)
          >>> print(turns[4])
          Start scores = (43, 38).
          Player 0 rolls 4 dice and gets outcomes [3, 3, 6, 1].
          End scores = (44, 38)
          >>> print(turns[5])
          Start scores = (44, 38).
          Player 1 rolls 3 dice and gets outcomes [4, 5, 1].
          End scores = (44, 39)
          >>> print(turns[6])
          Start scores = (44, 39).
          Player 0 rolls 1 dice and gets outcomes [5].
          End scores = (49, 39)
          >>> print(turns[7])
          Start scores = (49, 39).
          Player 1 rolls 3 dice and gets outcomes [5, 3, 2].
          End scores = (49, 49)
          >>> print(turns[8])
          Start scores = (49, 49).
          Player 0 rolls 7 dice and gets outcomes [1, 2, 6, 2, 1, 5, 2].
          End scores = (50, 49)
          >>> print(turns[9])
          Start scores = (50, 49).
          Player 1 rolls 1 dice and gets outcomes [5].
          End scores = (50, 54)
          >>> print(turns[10])
          Start scores = (50, 54).
          Player 0 rolls 9 dice and gets outcomes [3, 3, 2, 4, 4, 4, 2, 4, 6].
          End scores = (82, 54)
          >>> print(turns[11])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=82888, score0=26, score1=39, goal=87)
          >>> print(turns[0])
          Start scores = (26, 39).
          Player 0 rolls 9 dice and gets outcomes [4, 4, 3, 4, 3, 6, 5, 2, 6].
          End scores = (63, 39)
          >>> print(turns[1])
          Start scores = (63, 39).
          Player 1 rolls 2 dice and gets outcomes [6, 6].
          End scores = (63, 51)
          >>> print(turns[2])
          Start scores = (63, 51).
          Player 1 rolls 7 dice and gets outcomes [3, 1, 2, 4, 4, 5, 5].
          End scores = (63, 52)
          >>> print(turns[3])
          Start scores = (63, 52).
          Player 1 rolls 6 dice and gets outcomes [4, 4, 2, 2, 5, 3].
          End scores = (63, 72)
          >>> print(turns[4])
          Start scores = (63, 72).
          Player 0 rolls 10 dice and gets outcomes [3, 4, 1, 2, 6, 1, 6, 2, 1, 4].
          End scores = (64, 72)
          >>> print(turns[5])
          Start scores = (64, 72).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (64, 75)
          >>> print(turns[6])
          Start scores = (64, 75).
          Player 0 rolls 5 dice and gets outcomes [3, 1, 4, 1, 1].
          End scores = (65, 75)
          >>> print(turns[7])
          Start scores = (65, 75).
          Player 1 rolls 9 dice and gets outcomes [6, 3, 2, 5, 5, 2, 1, 2, 4].
          End scores = (65, 76)
          >>> print(turns[8])
          Start scores = (65, 76).
          Player 0 rolls 7 dice and gets outcomes [2, 3, 6, 6, 5, 6, 1].
          End scores = (66, 76)
          >>> print(turns[9])
          Start scores = (66, 76).
          Player 1 rolls 5 dice and gets outcomes [5, 5, 2, 6, 6].
          End scores = (66, 100)
          >>> print(turns[10])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=25835, score0=15, score1=64, goal=95)
          >>> print(turns[0])
          Start scores = (15, 64).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (18, 64)
          >>> print(turns[1])
          Start scores = (18, 64).
          Player 1 rolls 8 dice and gets outcomes [3, 2, 3, 4, 3, 1, 2, 1].
          End scores = (18, 65)
          >>> print(turns[2])
          Start scores = (18, 65).
          Player 0 rolls 8 dice and gets outcomes [3, 1, 6, 6, 4, 4, 2, 3].
          End scores = (19, 65)
          >>> print(turns[3])
          Start scores = (19, 65).
          Player 1 rolls 9 dice and gets outcomes [4, 2, 5, 3, 1, 6, 6, 4, 5].
          End scores = (19, 66)
          >>> print(turns[4])
          Start scores = (19, 66).
          Player 0 rolls 6 dice and gets outcomes [5, 4, 2, 2, 1, 3].
          End scores = (20, 66)
          >>> print(turns[5])
          Start scores = (20, 66).
          Player 0 rolls 4 dice and gets outcomes [5, 2, 1, 6].
          End scores = (21, 66)
          >>> print(turns[6])
          Start scores = (21, 66).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (27, 66)
          >>> print(turns[7])
          Start scores = (27, 66).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (27, 71)
          >>> print(turns[8])
          Start scores = (27, 71).
          Player 0 rolls 6 dice and gets outcomes [3, 5, 2, 2, 4, 1].
          End scores = (28, 71)
          >>> print(turns[9])
          Start scores = (28, 71).
          Player 1 rolls 5 dice and gets outcomes [3, 5, 3, 4, 5].
          End scores = (28, 91)
          >>> print(turns[10])
          Start scores = (28, 91).
          Player 0 rolls 1 dice and gets outcomes [5].
          End scores = (33, 91)
          >>> print(turns[11])
          Start scores = (33, 91).
          Player 1 rolls 6 dice and gets outcomes [2, 6, 3, 5, 2, 2].
          End scores = (33, 111)
          >>> print(turns[12])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=85071, score0=86, score1=5, goal=89)
          >>> print(turns[0])
          Start scores = (86, 5).
          Player 0 rolls 7 dice and gets outcomes [1, 3, 2, 6, 4, 5, 6].
          End scores = (87, 5)
          >>> print(turns[1])
          Start scores = (87, 5).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (87, 13)
          >>> print(turns[2])
          Start scores = (87, 13).
          Player 1 rolls 3 dice and gets outcomes [6, 6, 1].
          End scores = (87, 14)
          >>> print(turns[3])
          Start scores = (87, 14).
          Player 1 rolls 1 dice and gets outcomes [3].
          End scores = (87, 17)
          >>> print(turns[4])
          Start scores = (87, 17).
          Player 0 rolls 10 dice and gets outcomes [5, 6, 6, 5, 5, 3, 4, 4, 2, 5].
          End scores = (132, 17)
          >>> print(turns[5])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=23577, score0=32, score1=23, goal=45)
          >>> print(turns[0])
          Start scores = (32, 23).
          Player 0 rolls 7 dice and gets outcomes [1, 4, 6, 5, 3, 6, 4].
          End scores = (33, 23)
          >>> print(turns[1])
          Start scores = (33, 23).
          Player 1 rolls 8 dice and gets outcomes [2, 1, 3, 5, 3, 6, 6, 5].
          End scores = (33, 24)
          >>> print(turns[2])
          Start scores = (33, 24).
          Player 0 rolls 1 dice and gets outcomes [1].
          End scores = (34, 24)
          >>> print(turns[3])
          Start scores = (34, 24).
          Player 1 rolls 7 dice and gets outcomes [4, 4, 5, 2, 6, 4, 2].
          End scores = (34, 51)
          >>> print(turns[4])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=663, score0=44, score1=13, goal=59)
          >>> print(turns[0])
          Start scores = (44, 13).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (48, 13)
          >>> print(turns[1])
          Start scores = (48, 13).
          Player 1 rolls 1 dice and gets outcomes [5].
          End scores = (48, 18)
          >>> print(turns[2])
          Start scores = (48, 18).
          Player 0 rolls 7 dice and gets outcomes [6, 6, 4, 5, 3, 5, 5].
          End scores = (82, 18)
          >>> print(turns[3])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=6543, score0=65, score1=70, goal=87)
          >>> print(turns[0])
          Start scores = (65, 70).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (68, 70)
          >>> print(turns[1])
          Start scores = (68, 70).
          Player 1 rolls 9 dice and gets outcomes [5, 3, 3, 3, 2, 3, 6, 6, 2].
          End scores = (68, 103)
          >>> print(turns[2])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=31919, score0=2, score1=16, goal=28)
          >>> print(turns[0])
          Start scores = (2, 16).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (7, 16)
          >>> print(turns[1])
          Start scores = (7, 16).
          Player 1 rolls 6 dice and gets outcomes [5, 6, 2, 2, 3, 2].
          End scores = (7, 36)
          >>> print(turns[2])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=67699, score0=24, score1=17, goal=28)
          >>> print(turns[0])
          Start scores = (24, 17).
          Player 0 rolls 5 dice and gets outcomes [2, 1, 3, 6, 6].
          End scores = (25, 17)
          >>> print(turns[1])
          Start scores = (25, 17).
          Player 1 rolls 2 dice and gets outcomes [4, 3].
          End scores = (25, 24)
          >>> print(turns[2])
          Start scores = (25, 24).
          Player 0 rolls 1 dice and gets outcomes [5].
          End scores = (30, 24)
          >>> print(turns[3])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=25815, score0=52, score1=11, goal=54)
          >>> print(turns[0])
          Start scores = (52, 11).
          Player 0 rolls 9 dice and gets outcomes [5, 5, 5, 4, 2, 4, 3, 1, 5].
          End scores = (53, 11)
          >>> print(turns[1])
          Start scores = (53, 11).
          Player 1 rolls 5 dice and gets outcomes [1, 2, 1, 2, 6].
          End scores = (53, 12)
          >>> print(turns[2])
          Start scores = (53, 12).
          Player 1 rolls 7 dice and gets outcomes [4, 5, 6, 3, 1, 4, 4].
          End scores = (53, 13)
          >>> print(turns[3])
          Start scores = (53, 13).
          Player 0 rolls 2 dice and gets outcomes [1, 3].
          End scores = (54, 13)
          >>> print(turns[4])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=41969, score0=38, score1=54, goal=78)
          >>> print(turns[0])
          Start scores = (38, 54).
          Player 0 rolls 1 dice and gets outcomes [1].
          End scores = (39, 54)
          >>> print(turns[1])
          Start scores = (39, 54).
          Player 1 rolls 4 dice and gets outcomes [1, 2, 5, 6].
          End scores = (39, 55)
          >>> print(turns[2])
          Start scores = (39, 55).
          Player 0 rolls 3 dice and gets outcomes [2, 4, 1].
          End scores = (40, 55)
          >>> print(turns[3])
          Start scores = (40, 55).
          Player 0 rolls 2 dice and gets outcomes [4, 5].
          End scores = (49, 55)
          >>> print(turns[4])
          Start scores = (49, 55).
          Player 1 rolls 4 dice and gets outcomes [6, 4, 2, 2].
          End scores = (49, 69)
          >>> print(turns[5])
          Start scores = (49, 69).
          Player 0 rolls 2 dice and gets outcomes [5, 2].
          End scores = (56, 69)
          >>> print(turns[6])
          Start scores = (56, 69).
          Player 0 rolls 5 dice and gets outcomes [3, 5, 3, 1, 6].
          End scores = (57, 69)
          >>> print(turns[7])
          Start scores = (57, 69).
          Player 0 rolls 9 dice and gets outcomes [5, 5, 1, 6, 6, 1, 1, 3, 3].
          End scores = (58, 69)
          >>> print(turns[8])
          Start scores = (58, 69).
          Player 0 rolls 10 dice and gets outcomes [3, 1, 5, 2, 4, 6, 3, 4, 3, 4].
          End scores = (59, 69)
          >>> print(turns[9])
          Start scores = (59, 69).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (59, 73)
          >>> print(turns[10])
          Start scores = (59, 73).
          Player 0 rolls 9 dice and gets outcomes [4, 2, 2, 5, 1, 4, 5, 2, 3].
          End scores = (60, 73)
          >>> print(turns[11])
          Start scores = (60, 73).
          Player 0 rolls 5 dice and gets outcomes [2, 5, 3, 3, 3].
          End scores = (76, 73)
          >>> print(turns[12])
          Start scores = (76, 73).
          Player 1 rolls 7 dice and gets outcomes [6, 4, 2, 6, 2, 3, 6].
          End scores = (76, 102)
          >>> print(turns[13])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=68309, score0=53, score1=40, goal=56)
          >>> print(turns[0])
          Start scores = (53, 40).
          Player 0 rolls 7 dice and gets outcomes [2, 4, 3, 5, 6, 2, 2].
          End scores = (77, 40)
          >>> print(turns[1])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=8243, score0=28, score1=23, goal=30)
          >>> print(turns[0])
          Start scores = (28, 23).
          Player 0 rolls 6 dice and gets outcomes [4, 2, 5, 2, 6, 5].
          End scores = (52, 23)
          >>> print(turns[1])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=43015, score0=53, score1=74, goal=77)
          >>> print(turns[0])
          Start scores = (53, 74).
          Player 0 rolls 10 dice and gets outcomes [5, 6, 6, 6, 1, 4, 3, 5, 3, 2].
          End scores = (54, 74)
          >>> print(turns[1])
          Start scores = (54, 74).
          Player 1 rolls 5 dice and gets outcomes [1, 6, 5, 4, 6].
          End scores = (54, 75)
          >>> print(turns[2])
          Start scores = (54, 75).
          Player 0 rolls 9 dice and gets outcomes [2, 3, 2, 4, 4, 6, 4, 5, 3].
          End scores = (87, 75)
          >>> print(turns[3])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=76012, score0=39, score1=36, goal=73)
          >>> print(turns[0])
          Start scores = (39, 36).
          Player 0 rolls 2 dice and gets outcomes [1, 4].
          End scores = (40, 36)
          >>> print(turns[1])
          Start scores = (40, 36).
          Player 1 rolls 2 dice and gets outcomes [6, 6].
          End scores = (40, 48)
          >>> print(turns[2])
          Start scores = (40, 48).
          Player 0 rolls 4 dice and gets outcomes [6, 6, 6, 2].
          End scores = (60, 48)
          >>> print(turns[3])
          Start scores = (60, 48).
          Player 1 rolls 8 dice and gets outcomes [1, 3, 3, 2, 3, 5, 3, 6].
          End scores = (60, 49)
          >>> print(turns[4])
          Start scores = (60, 49).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (63, 49)
          >>> print(turns[5])
          Start scores = (63, 49).
          Player 1 rolls 3 dice and gets outcomes [2, 6, 3].
          End scores = (63, 60)
          >>> print(turns[6])
          Start scores = (63, 60).
          Player 0 rolls 2 dice and gets outcomes [5, 1].
          End scores = (64, 60)
          >>> print(turns[7])
          Start scores = (64, 60).
          Player 1 rolls 8 dice and gets outcomes [1, 5, 1, 6, 6, 6, 2, 1].
          End scores = (64, 61)
          >>> print(turns[8])
          Start scores = (64, 61).
          Player 0 rolls 5 dice and gets outcomes [2, 4, 4, 4, 5].
          End scores = (83, 61)
          >>> print(turns[9])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=9818, score0=11, score1=9, goal=64)
          >>> print(turns[0])
          Start scores = (11, 9).
          Player 0 rolls 10 dice and gets outcomes [2, 5, 3, 3, 6, 6, 4, 1, 1, 2].
          End scores = (12, 9)
          >>> print(turns[1])
          Start scores = (12, 9).
          Player 1 rolls 4 dice and gets outcomes [4, 1, 2, 6].
          End scores = (12, 10)
          >>> print(turns[2])
          Start scores = (12, 10).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (15, 10)
          >>> print(turns[3])
          Start scores = (15, 10).
          Player 1 rolls 9 dice and gets outcomes [3, 4, 2, 6, 5, 5, 4, 2, 3].
          End scores = (15, 44)
          >>> print(turns[4])
          Start scores = (15, 44).
          Player 0 rolls 8 dice and gets outcomes [3, 6, 6, 3, 1, 5, 3, 3].
          End scores = (16, 44)
          >>> print(turns[5])
          Start scores = (16, 44).
          Player 1 rolls 2 dice and gets outcomes [3, 2].
          End scores = (16, 49)
          >>> print(turns[6])
          Start scores = (16, 49).
          Player 0 rolls 2 dice and gets outcomes [6, 3].
          End scores = (25, 49)
          >>> print(turns[7])
          Start scores = (25, 49).
          Player 0 rolls 3 dice and gets outcomes [2, 5, 4].
          End scores = (36, 49)
          >>> print(turns[8])
          Start scores = (36, 49).
          Player 0 rolls 5 dice and gets outcomes [4, 4, 5, 4, 2].
          End scores = (55, 49)
          >>> print(turns[9])
          Start scores = (55, 49).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (55, 52)
          >>> print(turns[10])
          Start scores = (55, 52).
          Player 0 rolls 5 dice and gets outcomes [3, 1, 1, 4, 4].
          End scores = (56, 52)
          >>> print(turns[11])
          Start scores = (56, 52).
          Player 1 rolls 3 dice and gets outcomes [6, 3, 2].
          End scores = (56, 63)
          >>> print(turns[12])
          Start scores = (56, 63).
          Player 0 rolls 5 dice and gets outcomes [1, 6, 4, 3, 3].
          End scores = (57, 63)
          >>> print(turns[13])
          Start scores = (57, 63).
          Player 1 rolls 7 dice and gets outcomes [5, 3, 5, 3, 6, 3, 4].
          End scores = (57, 92)
          >>> print(turns[14])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=25916, score0=86, score1=24, goal=88)
          >>> print(turns[0])
          Start scores = (86, 24).
          Player 0 rolls 5 dice and gets outcomes [4, 1, 5, 5, 1].
          End scores = (87, 24)
          >>> print(turns[1])
          Start scores = (87, 24).
          Player 1 rolls 8 dice and gets outcomes [5, 4, 4, 2, 5, 2, 2, 2].
          End scores = (87, 50)
          >>> print(turns[2])
          Start scores = (87, 50).
          Player 1 rolls 5 dice and gets outcomes [1, 2, 4, 1, 6].
          End scores = (87, 51)
          >>> print(turns[3])
          Start scores = (87, 51).
          Player 1 rolls 6 dice and gets outcomes [4, 2, 4, 6, 2, 6].
          End scores = (87, 75)
          >>> print(turns[4])
          Start scores = (87, 75).
          Player 1 rolls 6 dice and gets outcomes [2, 5, 4, 6, 6, 4].
          End scores = (87, 102)
          >>> print(turns[5])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=15583, score0=11, score1=40, goal=55)
          >>> print(turns[0])
          Start scores = (11, 40).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (14, 40)
          >>> print(turns[1])
          Start scores = (14, 40).
          Player 1 rolls 2 dice and gets outcomes [1, 2].
          End scores = (14, 41)
          >>> print(turns[2])
          Start scores = (14, 41).
          Player 0 rolls 3 dice and gets outcomes [3, 5, 4].
          End scores = (26, 41)
          >>> print(turns[3])
          Start scores = (26, 41).
          Player 1 rolls 1 dice and gets outcomes [4].
          End scores = (26, 45)
          >>> print(turns[4])
          Start scores = (26, 45).
          Player 0 rolls 4 dice and gets outcomes [2, 5, 1, 2].
          End scores = (27, 45)
          >>> print(turns[5])
          Start scores = (27, 45).
          Player 1 rolls 9 dice and gets outcomes [1, 2, 1, 4, 6, 4, 2, 1, 3].
          End scores = (27, 46)
          >>> print(turns[6])
          Start scores = (27, 46).
          Player 0 rolls 6 dice and gets outcomes [3, 5, 4, 3, 4, 1].
          End scores = (28, 46)
          >>> print(turns[7])
          Start scores = (28, 46).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (28, 53)
          >>> print(turns[8])
          Start scores = (28, 53).
          Player 0 rolls 2 dice and gets outcomes [3, 5].
          End scores = (36, 53)
          >>> print(turns[9])
          Start scores = (36, 53).
          Player 1 rolls 7 dice and gets outcomes [2, 2, 2, 5, 4, 1, 4].
          End scores = (36, 54)
          >>> print(turns[10])
          Start scores = (36, 54).
          Player 0 rolls 5 dice and gets outcomes [4, 4, 3, 5, 1].
          End scores = (37, 54)
          >>> print(turns[11])
          Start scores = (37, 54).
          Player 1 rolls 8 dice and gets outcomes [3, 5, 2, 4, 1, 6, 5, 3].
          End scores = (37, 55)
          >>> print(turns[12])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=7242, score0=19, score1=46, goal=98)
          >>> print(turns[0])
          Start scores = (19, 46).
          Player 0 rolls 8 dice and gets outcomes [2, 2, 3, 5, 4, 1, 1, 3].
          End scores = (20, 46)
          >>> print(turns[1])
          Start scores = (20, 46).
          Player 0 rolls 9 dice and gets outcomes [1, 1, 6, 6, 5, 3, 1, 4, 4].
          End scores = (21, 46)
          >>> print(turns[2])
          Start scores = (21, 46).
          Player 0 rolls 6 dice and gets outcomes [5, 4, 6, 1, 1, 6].
          End scores = (22, 46)
          >>> print(turns[3])
          Start scores = (22, 46).
          Player 0 rolls 7 dice and gets outcomes [2, 3, 1, 1, 5, 4, 4].
          End scores = (23, 46)
          >>> print(turns[4])
          Start scores = (23, 46).
          Player 0 rolls 8 dice and gets outcomes [5, 3, 2, 2, 1, 1, 1, 1].
          End scores = (24, 46)
          >>> print(turns[5])
          Start scores = (24, 46).
          Player 0 rolls 6 dice and gets outcomes [1, 6, 6, 3, 5, 3].
          End scores = (25, 46)
          >>> print(turns[6])
          Start scores = (25, 46).
          Player 0 rolls 7 dice and gets outcomes [2, 2, 3, 4, 5, 3, 1].
          End scores = (26, 46)
          >>> print(turns[7])
          Start scores = (26, 46).
          Player 1 rolls 5 dice and gets outcomes [6, 1, 6, 6, 3].
          End scores = (26, 47)
          >>> print(turns[8])
          Start scores = (26, 47).
          Player 0 rolls 1 dice and gets outcomes [2].
          End scores = (28, 47)
          >>> print(turns[9])
          Start scores = (28, 47).
          Player 1 rolls 10 dice and gets outcomes [1, 1, 3, 6, 3, 1, 6, 3, 2, 2].
          End scores = (28, 48)
          >>> print(turns[10])
          Start scores = (28, 48).
          Player 0 rolls 6 dice and gets outcomes [5, 6, 2, 6, 3, 3].
          End scores = (53, 48)
          >>> print(turns[11])
          Start scores = (53, 48).
          Player 1 rolls 3 dice and gets outcomes [6, 4, 4].
          End scores = (53, 62)
          >>> print(turns[12])
          Start scores = (53, 62).
          Player 0 rolls 5 dice and gets outcomes [4, 1, 4, 2, 5].
          End scores = (54, 62)
          >>> print(turns[13])
          Start scores = (54, 62).
          Player 1 rolls 8 dice and gets outcomes [5, 1, 3, 4, 1, 2, 1, 5].
          End scores = (54, 63)
          >>> print(turns[14])
          Start scores = (54, 63).
          Player 0 rolls 4 dice and gets outcomes [3, 1, 2, 3].
          End scores = (55, 63)
          >>> print(turns[15])
          Start scores = (55, 63).
          Player 1 rolls 3 dice and gets outcomes [3, 1, 5].
          End scores = (55, 64)
          >>> print(turns[16])
          Start scores = (55, 64).
          Player 0 rolls 1 dice and gets outcomes [4].
          End scores = (59, 64)
          >>> print(turns[17])
          Start scores = (59, 64).
          Player 1 rolls 8 dice and gets outcomes [3, 2, 1, 6, 3, 6, 5, 5].
          End scores = (59, 65)
          >>> print(turns[18])
          Start scores = (59, 65).
          Player 0 rolls 2 dice and gets outcomes [6, 2].
          End scores = (67, 65)
          >>> print(turns[19])
          Start scores = (67, 65).
          Player 1 rolls 6 dice and gets outcomes [4, 5, 6, 3, 3, 6].
          End scores = (67, 92)
          >>> print(turns[20])
          Start scores = (67, 92).
          Player 0 rolls 3 dice and gets outcomes [5, 4, 4].
          End scores = (80, 92)
          >>> print(turns[21])
          Start scores = (80, 92).
          Player 0 rolls 5 dice and gets outcomes [1, 4, 1, 4, 4].
          End scores = (81, 92)
          >>> print(turns[22])
          Start scores = (81, 92).
          Player 0 rolls 8 dice and gets outcomes [6, 5, 3, 6, 6, 4, 5, 2].
          End scores = (118, 92)
          >>> print(turns[23])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=74122, score0=18, score1=14, goal=32)
          >>> print(turns[0])
          Start scores = (18, 14).
          Player 0 rolls 7 dice and gets outcomes [3, 2, 5, 2, 2, 6, 1].
          End scores = (19, 14)
          >>> print(turns[1])
          Start scores = (19, 14).
          Player 1 rolls 3 dice and gets outcomes [1, 3, 3].
          End scores = (19, 15)
          >>> print(turns[2])
          Start scores = (19, 15).
          Player 0 rolls 9 dice and gets outcomes [5, 3, 4, 3, 6, 3, 2, 5, 6].
          End scores = (56, 15)
          >>> print(turns[3])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=59593, score0=27, score1=9, goal=40)
          >>> print(turns[0])
          Start scores = (27, 9).
          Player 0 rolls 1 dice and gets outcomes [5].
          End scores = (32, 9)
          >>> print(turns[1])
          Start scores = (32, 9).
          Player 1 rolls 4 dice and gets outcomes [4, 4, 2, 2].
          End scores = (32, 21)
          >>> print(turns[2])
          Start scores = (32, 21).
          Player 1 rolls 3 dice and gets outcomes [5, 4, 6].
          End scores = (32, 36)
          >>> print(turns[3])
          Start scores = (32, 36).
          Player 0 rolls 5 dice and gets outcomes [2, 2, 4, 4, 1].
          End scores = (33, 36)
          >>> print(turns[4])
          Start scores = (33, 36).
          Player 1 rolls 1 dice and gets outcomes [6].
          End scores = (33, 42)
          >>> print(turns[5])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=8128, score0=17, score1=8, goal=29)
          >>> print(turns[0])
          Start scores = (17, 8).
          Player 0 rolls 4 dice and gets outcomes [4, 2, 4, 5].
          End scores = (32, 8)
          >>> print(turns[1])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=22810, score0=7, score1=0, goal=43)
          >>> print(turns[0])
          Start scores = (7, 0).
          Player 0 rolls 2 dice and gets outcomes [5, 3].
          End scores = (15, 0)
          >>> print(turns[1])
          Start scores = (15, 0).
          Player 1 rolls 2 dice and gets outcomes [2, 1].
          End scores = (15, 1)
          >>> print(turns[2])
          Start scores = (15, 1).
          Player 1 rolls 3 dice and gets outcomes [4, 1, 1].
          End scores = (15, 2)
          >>> print(turns[3])
          Start scores = (15, 2).
          Player 1 rolls 1 dice and gets outcomes [3].
          End scores = (15, 5)
          >>> print(turns[4])
          Start scores = (15, 5).
          Player 0 rolls 3 dice and gets outcomes [1, 4, 3].
          End scores = (16, 5)
          >>> print(turns[5])
          Start scores = (16, 5).
          Player 1 rolls 6 dice and gets outcomes [5, 3, 5, 1, 6, 3].
          End scores = (16, 6)
          >>> print(turns[6])
          Start scores = (16, 6).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (22, 6)
          >>> print(turns[7])
          Start scores = (22, 6).
          Player 1 rolls 4 dice and gets outcomes [1, 5, 4, 3].
          End scores = (22, 7)
          >>> print(turns[8])
          Start scores = (22, 7).
          Player 0 rolls 1 dice and gets outcomes [1].
          End scores = (23, 7)
          >>> print(turns[9])
          Start scores = (23, 7).
          Player 1 rolls 8 dice and gets outcomes [2, 6, 5, 5, 4, 6, 6, 6].
          End scores = (23, 47)
          >>> print(turns[10])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=59348, score0=95, score1=84, goal=97)
          >>> print(turns[0])
          Start scores = (95, 84).
          Player 0 rolls 1 dice and gets outcomes [2].
          End scores = (97, 84)
          >>> print(turns[1])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=88169, score0=23, score1=40, goal=79)
          >>> print(turns[0])
          Start scores = (23, 40).
          Player 0 rolls 3 dice and gets outcomes [1, 5, 6].
          End scores = (24, 40)
          >>> print(turns[1])
          Start scores = (24, 40).
          Player 1 rolls 7 dice and gets outcomes [2, 6, 6, 6, 2, 3, 3].
          End scores = (24, 68)
          >>> print(turns[2])
          Start scores = (24, 68).
          Player 0 rolls 3 dice and gets outcomes [6, 5, 4].
          End scores = (39, 68)
          >>> print(turns[3])
          Start scores = (39, 68).
          Player 1 rolls 5 dice and gets outcomes [2, 3, 5, 1, 6].
          End scores = (39, 69)
          >>> print(turns[4])
          Start scores = (39, 69).
          Player 0 rolls 3 dice and gets outcomes [3, 2, 5].
          End scores = (49, 69)
          >>> print(turns[5])
          Start scores = (49, 69).
          Player 1 rolls 5 dice and gets outcomes [6, 6, 4, 5, 3].
          End scores = (49, 93)
          >>> print(turns[6])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=70467, score0=61, score1=74, goal=97)
          >>> print(turns[0])
          Start scores = (61, 74).
          Player 0 rolls 2 dice and gets outcomes [4, 4].
          End scores = (69, 74)
          >>> print(turns[1])
          Start scores = (69, 74).
          Player 1 rolls 8 dice and gets outcomes [6, 4, 3, 1, 5, 1, 5, 6].
          End scores = (69, 75)
          >>> print(turns[2])
          Start scores = (69, 75).
          Player 0 rolls 6 dice and gets outcomes [5, 3, 4, 1, 5, 6].
          End scores = (70, 75)
          >>> print(turns[3])
          Start scores = (70, 75).
          Player 1 rolls 6 dice and gets outcomes [6, 4, 6, 1, 5, 3].
          End scores = (70, 76)
          >>> print(turns[4])
          Start scores = (70, 76).
          Player 0 rolls 7 dice and gets outcomes [2, 2, 1, 3, 3, 6, 1].
          End scores = (71, 76)
          >>> print(turns[5])
          Start scores = (71, 76).
          Player 1 rolls 7 dice and gets outcomes [6, 3, 6, 4, 5, 3, 1].
          End scores = (71, 77)
          >>> print(turns[6])
          Start scores = (71, 77).
          Player 0 rolls 4 dice and gets outcomes [2, 6, 4, 4].
          End scores = (87, 77)
          >>> print(turns[7])
          Start scores = (87, 77).
          Player 1 rolls 5 dice and gets outcomes [2, 6, 3, 3, 4].
          End scores = (87, 95)
          >>> print(turns[8])
          Start scores = (87, 95).
          Player 0 rolls 1 dice and gets outcomes [1].
          End scores = (88, 95)
          >>> print(turns[9])
          Start scores = (88, 95).
          Player 1 rolls 6 dice and gets outcomes [2, 4, 2, 2, 6, 4].
          End scores = (88, 115)
          >>> print(turns[10])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=8714, score0=38, score1=19, goal=57)
          >>> print(turns[0])
          Start scores = (38, 19).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (42, 19)
          >>> print(turns[1])
          Start scores = (42, 19).
          Player 1 rolls 1 dice and gets outcomes [5].
          End scores = (42, 24)
          >>> print(turns[2])
          Start scores = (42, 24).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (50, 24)
          >>> print(turns[3])
          Start scores = (50, 24).
          Player 1 rolls 6 dice and gets outcomes [1, 1, 1, 4, 5, 5].
          End scores = (50, 25)
          >>> print(turns[4])
          Start scores = (50, 25).
          Player 0 rolls 10 dice and gets outcomes [4, 6, 5, 6, 3, 4, 3, 5, 1, 5].
          End scores = (51, 25)
          >>> print(turns[5])
          Start scores = (51, 25).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (51, 28)
          >>> print(turns[6])
          Start scores = (51, 28).
          Player 0 rolls 1 dice and gets outcomes [4].
          End scores = (55, 28)
          >>> print(turns[7])
          Start scores = (55, 28).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (55, 31)
          >>> print(turns[8])
          Start scores = (55, 31).
          Player 1 rolls 5 dice and gets outcomes [2, 5, 5, 5, 4].
          End scores = (55, 52)
          >>> print(turns[9])
          Start scores = (55, 52).
          Player 0 rolls 3 dice and gets outcomes [2, 1, 5].
          End scores = (56, 52)
          >>> print(turns[10])
          Start scores = (56, 52).
          Player 1 rolls 2 dice and gets outcomes [4, 3].
          End scores = (56, 59)
          >>> print(turns[11])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=13230, score0=65, score1=56, goal=77)
          >>> print(turns[0])
          Start scores = (65, 56).
          Player 0 rolls 6 dice and gets outcomes [2, 5, 2, 1, 3, 4].
          End scores = (66, 56)
          >>> print(turns[1])
          Start scores = (66, 56).
          Player 1 rolls 2 dice and gets outcomes [2, 5].
          End scores = (66, 63)
          >>> print(turns[2])
          Start scores = (66, 63).
          Player 0 rolls 3 dice and gets outcomes [4, 1, 1].
          End scores = (67, 63)
          >>> print(turns[3])
          Start scores = (67, 63).
          Player 1 rolls 3 dice and gets outcomes [5, 3, 6].
          End scores = (67, 77)
          >>> print(turns[4])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=96667, score0=2, score1=3, goal=13)
          >>> print(turns[0])
          Start scores = (2, 3).
          Player 0 rolls 9 dice and gets outcomes [1, 1, 3, 5, 3, 6, 6, 4, 1].
          End scores = (3, 3)
          >>> print(turns[1])
          Start scores = (3, 3).
          Player 1 rolls 3 dice and gets outcomes [2, 3, 5].
          End scores = (3, 13)
          >>> print(turns[2])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=27904, score0=23, score1=39, goal=92)
          >>> print(turns[0])
          Start scores = (23, 39).
          Player 0 rolls 9 dice and gets outcomes [6, 6, 2, 6, 1, 4, 3, 4, 3].
          End scores = (24, 39)
          >>> print(turns[1])
          Start scores = (24, 39).
          Player 0 rolls 7 dice and gets outcomes [4, 3, 3, 4, 5, 5, 6].
          End scores = (54, 39)
          >>> print(turns[2])
          Start scores = (54, 39).
          Player 1 rolls 10 dice and gets outcomes [2, 4, 1, 3, 5, 4, 5, 2, 2, 4].
          End scores = (54, 40)
          >>> print(turns[3])
          Start scores = (54, 40).
          Player 1 rolls 6 dice and gets outcomes [1, 1, 5, 5, 6, 1].
          End scores = (54, 41)
          >>> print(turns[4])
          Start scores = (54, 41).
          Player 1 rolls 6 dice and gets outcomes [6, 1, 1, 2, 5, 2].
          End scores = (54, 42)
          >>> print(turns[5])
          Start scores = (54, 42).
          Player 1 rolls 10 dice and gets outcomes [2, 5, 2, 6, 6, 2, 3, 5, 3, 4].
          End scores = (54, 80)
          >>> print(turns[6])
          Start scores = (54, 80).
          Player 0 rolls 1 dice and gets outcomes [5].
          End scores = (59, 80)
          >>> print(turns[7])
          Start scores = (59, 80).
          Player 1 rolls 8 dice and gets outcomes [2, 1, 5, 5, 3, 6, 6, 2].
          End scores = (59, 81)
          >>> print(turns[8])
          Start scores = (59, 81).
          Player 0 rolls 2 dice and gets outcomes [2, 6].
          End scores = (67, 81)
          >>> print(turns[9])
          Start scores = (67, 81).
          Player 1 rolls 10 dice and gets outcomes [1, 1, 6, 5, 2, 3, 2, 2, 2, 4].
          End scores = (67, 82)
          >>> print(turns[10])
          Start scores = (67, 82).
          Player 0 rolls 4 dice and gets outcomes [4, 6, 1, 5].
          End scores = (68, 82)
          >>> print(turns[11])
          Start scores = (68, 82).
          Player 1 rolls 6 dice and gets outcomes [4, 6, 5, 5, 4, 6].
          End scores = (68, 112)
          >>> print(turns[12])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=36152, score0=49, score1=25, goal=52)
          >>> print(turns[0])
          Start scores = (49, 25).
          Player 0 rolls 5 dice and gets outcomes [1, 5, 6, 1, 3].
          End scores = (50, 25)
          >>> print(turns[1])
          Start scores = (50, 25).
          Player 1 rolls 5 dice and gets outcomes [3, 1, 2, 2, 2].
          End scores = (50, 26)
          >>> print(turns[2])
          Start scores = (50, 26).
          Player 0 rolls 6 dice and gets outcomes [2, 3, 1, 5, 5, 3].
          End scores = (51, 26)
          >>> print(turns[3])
          Start scores = (51, 26).
          Player 1 rolls 8 dice and gets outcomes [2, 2, 3, 1, 5, 3, 2, 2].
          End scores = (51, 27)
          >>> print(turns[4])
          Start scores = (51, 27).
          Player 0 rolls 9 dice and gets outcomes [4, 3, 5, 6, 4, 2, 3, 2, 1].
          End scores = (52, 27)
          >>> print(turns[5])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=97165, score0=13, score1=4, goal=42)
          >>> print(turns[0])
          Start scores = (13, 4).
          Player 0 rolls 4 dice and gets outcomes [1, 3, 1, 4].
          End scores = (14, 4)
          >>> print(turns[1])
          Start scores = (14, 4).
          Player 1 rolls 6 dice and gets outcomes [5, 4, 5, 3, 3, 5].
          End scores = (14, 29)
          >>> print(turns[2])
          Start scores = (14, 29).
          Player 0 rolls 7 dice and gets outcomes [4, 6, 1, 2, 4, 1, 5].
          End scores = (15, 29)
          >>> print(turns[3])
          Start scores = (15, 29).
          Player 0 rolls 7 dice and gets outcomes [5, 6, 1, 1, 3, 3, 3].
          End scores = (16, 29)
          >>> print(turns[4])
          Start scores = (16, 29).
          Player 0 rolls 8 dice and gets outcomes [6, 3, 4, 4, 5, 2, 6, 4].
          End scores = (50, 29)
          >>> print(turns[5])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=7964, score0=0, score1=12, goal=30)
          >>> print(turns[0])
          Start scores = (0, 12).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (4, 12)
          >>> print(turns[1])
          Start scores = (4, 12).
          Player 1 rolls 4 dice and gets outcomes [2, 5, 5, 4].
          End scores = (4, 28)
          >>> print(turns[2])
          Start scores = (4, 28).
          Player 0 rolls 5 dice and gets outcomes [6, 3, 3, 2, 4].
          End scores = (22, 28)
          >>> print(turns[3])
          Start scores = (22, 28).
          Player 1 rolls 6 dice and gets outcomes [2, 2, 1, 1, 2, 4].
          End scores = (22, 29)
          >>> print(turns[4])
          Start scores = (22, 29).
          Player 0 rolls 4 dice and gets outcomes [1, 2, 5, 5].
          End scores = (23, 29)
          >>> print(turns[5])
          Start scores = (23, 29).
          Player 1 rolls 5 dice and gets outcomes [5, 5, 3, 5, 3].
          End scores = (23, 50)
          >>> print(turns[6])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=87291, score0=59, score1=15, goal=87)
          >>> print(turns[0])
          Start scores = (59, 15).
          Player 0 rolls 3 dice and gets outcomes [2, 2, 1].
          End scores = (60, 15)
          >>> print(turns[1])
          Start scores = (60, 15).
          Player 1 rolls 9 dice and gets outcomes [6, 2, 4, 4, 4, 3, 5, 2, 3].
          End scores = (60, 48)
          >>> print(turns[2])
          Start scores = (60, 48).
          Player 0 rolls 8 dice and gets outcomes [3, 5, 1, 6, 6, 2, 3, 4].
          End scores = (61, 48)
          >>> print(turns[3])
          Start scores = (61, 48).
          Player 1 rolls 5 dice and gets outcomes [6, 2, 5, 6, 3].
          End scores = (61, 70)
          >>> print(turns[4])
          Start scores = (61, 70).
          Player 0 rolls 4 dice and gets outcomes [2, 5, 4, 4].
          End scores = (76, 70)
          >>> print(turns[5])
          Start scores = (76, 70).
          Player 1 rolls 8 dice and gets outcomes [2, 6, 4, 1, 6, 1, 2, 4].
          End scores = (76, 71)
          >>> print(turns[6])
          Start scores = (76, 71).
          Player 0 rolls 4 dice and gets outcomes [4, 2, 2, 1].
          End scores = (77, 71)
          >>> print(turns[7])
          Start scores = (77, 71).
          Player 1 rolls 4 dice and gets outcomes [1, 3, 3, 6].
          End scores = (77, 72)
          >>> print(turns[8])
          Start scores = (77, 72).
          Player 0 rolls 4 dice and gets outcomes [6, 2, 6, 2].
          End scores = (93, 72)
          >>> print(turns[9])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=2481, score0=32, score1=79, goal=98)
          >>> print(turns[0])
          Start scores = (32, 79).
          Player 0 rolls 10 dice and gets outcomes [2, 4, 4, 5, 2, 5, 3, 1, 2, 5].
          End scores = (33, 79)
          >>> print(turns[1])
          Start scores = (33, 79).
          Player 0 rolls 4 dice and gets outcomes [2, 2, 5, 5].
          End scores = (47, 79)
          >>> print(turns[2])
          Start scores = (47, 79).
          Player 0 rolls 4 dice and gets outcomes [1, 6, 3, 1].
          End scores = (48, 79)
          >>> print(turns[3])
          Start scores = (48, 79).
          Player 0 rolls 5 dice and gets outcomes [2, 4, 6, 2, 2].
          End scores = (64, 79)
          >>> print(turns[4])
          Start scores = (64, 79).
          Player 0 rolls 9 dice and gets outcomes [3, 6, 1, 3, 6, 4, 2, 3, 6].
          End scores = (65, 79)
          >>> print(turns[5])
          Start scores = (65, 79).
          Player 0 rolls 5 dice and gets outcomes [1, 4, 2, 2, 3].
          End scores = (66, 79)
          >>> print(turns[6])
          Start scores = (66, 79).
          Player 0 rolls 3 dice and gets outcomes [2, 1, 1].
          End scores = (67, 79)
          >>> print(turns[7])
          Start scores = (67, 79).
          Player 0 rolls 7 dice and gets outcomes [4, 6, 3, 1, 6, 5, 4].
          End scores = (68, 79)
          >>> print(turns[8])
          Start scores = (68, 79).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (72, 79)
          >>> print(turns[9])
          Start scores = (72, 79).
          Player 1 rolls 2 dice and gets outcomes [3, 6].
          End scores = (72, 88)
          >>> print(turns[10])
          Start scores = (72, 88).
          Player 0 rolls 5 dice and gets outcomes [2, 5, 2, 1, 5].
          End scores = (73, 88)
          >>> print(turns[11])
          Start scores = (73, 88).
          Player 0 rolls 5 dice and gets outcomes [3, 6, 1, 2, 4].
          End scores = (74, 88)
          >>> print(turns[12])
          Start scores = (74, 88).
          Player 0 rolls 9 dice and gets outcomes [2, 6, 2, 1, 4, 1, 3, 1, 3].
          End scores = (75, 88)
          >>> print(turns[13])
          Start scores = (75, 88).
          Player 0 rolls 9 dice and gets outcomes [4, 4, 5, 3, 6, 5, 4, 2, 4].
          End scores = (112, 88)
          >>> print(turns[14])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=57878, score0=4, score1=13, goal=29)
          >>> print(turns[0])
          Start scores = (4, 13).
          Player 0 rolls 5 dice and gets outcomes [2, 3, 1, 6, 3].
          End scores = (5, 13)
          >>> print(turns[1])
          Start scores = (5, 13).
          Player 1 rolls 9 dice and gets outcomes [3, 4, 2, 3, 3, 4, 1, 4, 3].
          End scores = (5, 14)
          >>> print(turns[2])
          Start scores = (5, 14).
          Player 0 rolls 5 dice and gets outcomes [1, 5, 2, 3, 1].
          End scores = (6, 14)
          >>> print(turns[3])
          Start scores = (6, 14).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (6, 20)
          >>> print(turns[4])
          Start scores = (6, 20).
          Player 0 rolls 4 dice and gets outcomes [5, 1, 3, 6].
          End scores = (7, 20)
          >>> print(turns[5])
          Start scores = (7, 20).
          Player 1 rolls 9 dice and gets outcomes [6, 1, 1, 6, 4, 5, 3, 4, 4].
          End scores = (7, 21)
          >>> print(turns[6])
          Start scores = (7, 21).
          Player 0 rolls 10 dice and gets outcomes [2, 2, 3, 2, 1, 6, 3, 1, 4, 4].
          End scores = (8, 21)
          >>> print(turns[7])
          Start scores = (8, 21).
          Player 1 rolls 9 dice and gets outcomes [3, 6, 4, 3, 5, 1, 6, 2, 5].
          End scores = (8, 22)
          >>> print(turns[8])
          Start scores = (8, 22).
          Player 0 rolls 10 dice and gets outcomes [2, 3, 1, 3, 6, 6, 2, 2, 3, 4].
          End scores = (9, 22)
          >>> print(turns[9])
          Start scores = (9, 22).
          Player 1 rolls 3 dice and gets outcomes [6, 2, 2].
          End scores = (9, 32)
          >>> print(turns[10])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=27303, score0=31, score1=3, goal=39)
          >>> print(turns[0])
          Start scores = (31, 3).
          Player 0 rolls 9 dice and gets outcomes [6, 5, 6, 1, 6, 2, 2, 2, 6].
          End scores = (32, 3)
          >>> print(turns[1])
          Start scores = (32, 3).
          Player 1 rolls 9 dice and gets outcomes [1, 6, 1, 1, 5, 5, 2, 1, 6].
          End scores = (32, 4)
          >>> print(turns[2])
          Start scores = (32, 4).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (36, 4)
          >>> print(turns[3])
          Start scores = (36, 4).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (36, 8)
          >>> print(turns[4])
          Start scores = (36, 8).
          Player 0 rolls 5 dice and gets outcomes [3, 6, 6, 6, 6].
          End scores = (63, 8)
          >>> print(turns[5])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=98514, score0=46, score1=42, goal=60)
          >>> print(turns[0])
          Start scores = (46, 42).
          Player 0 rolls 5 dice and gets outcomes [5, 1, 3, 3, 5].
          End scores = (47, 42)
          >>> print(turns[1])
          Start scores = (47, 42).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (47, 45)
          >>> print(turns[2])
          Start scores = (47, 45).
          Player 0 rolls 9 dice and gets outcomes [6, 3, 4, 4, 5, 1, 4, 6, 4].
          End scores = (48, 45)
          >>> print(turns[3])
          Start scores = (48, 45).
          Player 1 rolls 3 dice and gets outcomes [5, 6, 3].
          End scores = (48, 59)
          >>> print(turns[4])
          Start scores = (48, 59).
          Player 0 rolls 6 dice and gets outcomes [2, 2, 6, 5, 4, 3].
          End scores = (70, 59)
          >>> print(turns[5])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=64395, score0=3, score1=18, goal=52)
          >>> print(turns[0])
          Start scores = (3, 18).
          Player 0 rolls 9 dice and gets outcomes [4, 4, 6, 3, 2, 6, 3, 3, 2].
          End scores = (36, 18)
          >>> print(turns[1])
          Start scores = (36, 18).
          Player 1 rolls 3 dice and gets outcomes [2, 1, 2].
          End scores = (36, 19)
          >>> print(turns[2])
          Start scores = (36, 19).
          Player 0 rolls 8 dice and gets outcomes [6, 5, 6, 3, 3, 2, 6, 4].
          End scores = (71, 19)
          >>> print(turns[3])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=13464, score0=27, score1=4, goal=47)
          >>> print(turns[0])
          Start scores = (27, 4).
          Player 0 rolls 4 dice and gets outcomes [3, 1, 5, 4].
          End scores = (28, 4)
          >>> print(turns[1])
          Start scores = (28, 4).
          Player 1 rolls 7 dice and gets outcomes [5, 3, 2, 5, 4, 5, 3].
          End scores = (28, 31)
          >>> print(turns[2])
          Start scores = (28, 31).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (32, 31)
          >>> print(turns[3])
          Start scores = (32, 31).
          Player 1 rolls 10 dice and gets outcomes [6, 4, 1, 2, 6, 2, 3, 4, 5, 3].
          End scores = (32, 32)
          >>> print(turns[4])
          Start scores = (32, 32).
          Player 0 rolls 5 dice and gets outcomes [3, 1, 4, 5, 6].
          End scores = (33, 32)
          >>> print(turns[5])
          Start scores = (33, 32).
          Player 1 rolls 2 dice and gets outcomes [1, 6].
          End scores = (33, 33)
          >>> print(turns[6])
          Start scores = (33, 33).
          Player 0 rolls 7 dice and gets outcomes [6, 1, 2, 5, 2, 6, 4].
          End scores = (34, 33)
          >>> print(turns[7])
          Start scores = (34, 33).
          Player 1 rolls 10 dice and gets outcomes [4, 6, 4, 2, 4, 5, 5, 5, 3, 2].
          End scores = (34, 73)
          >>> print(turns[8])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=92338, score0=64, score1=67, goal=69)
          >>> print(turns[0])
          Start scores = (64, 67).
          Player 0 rolls 10 dice and gets outcomes [6, 2, 4, 4, 6, 4, 4, 6, 3, 4].
          End scores = (107, 67)
          >>> print(turns[1])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=55414, score0=9, score1=19, goal=32)
          >>> print(turns[0])
          Start scores = (9, 19).
          Player 0 rolls 8 dice and gets outcomes [1, 3, 2, 6, 1, 2, 5, 3].
          End scores = (10, 19)
          >>> print(turns[1])
          Start scores = (10, 19).
          Player 1 rolls 10 dice and gets outcomes [4, 2, 4, 6, 1, 5, 1, 3, 2, 1].
          End scores = (10, 20)
          >>> print(turns[2])
          Start scores = (10, 20).
          Player 0 rolls 3 dice and gets outcomes [3, 4, 2].
          End scores = (19, 20)
          >>> print(turns[3])
          Start scores = (19, 20).
          Player 1 rolls 4 dice and gets outcomes [6, 6, 6, 2].
          End scores = (19, 40)
          >>> print(turns[4])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=2412, score0=90, score1=38, goal=94)
          >>> print(turns[0])
          Start scores = (90, 38).
          Player 0 rolls 7 dice and gets outcomes [5, 3, 2, 6, 4, 1, 5].
          End scores = (91, 38)
          >>> print(turns[1])
          Start scores = (91, 38).
          Player 1 rolls 6 dice and gets outcomes [2, 3, 3, 5, 1, 6].
          End scores = (91, 39)
          >>> print(turns[2])
          Start scores = (91, 39).
          Player 0 rolls 3 dice and gets outcomes [1, 1, 5].
          End scores = (92, 39)
          >>> print(turns[3])
          Start scores = (92, 39).
          Player 1 rolls 8 dice and gets outcomes [1, 2, 6, 3, 1, 6, 5, 6].
          End scores = (92, 40)
          >>> print(turns[4])
          Start scores = (92, 40).
          Player 1 rolls 7 dice and gets outcomes [1, 3, 1, 5, 6, 5, 4].
          End scores = (92, 41)
          >>> print(turns[5])
          Start scores = (92, 41).
          Player 1 rolls 5 dice and gets outcomes [6, 3, 1, 5, 6].
          End scores = (92, 42)
          >>> print(turns[6])
          Start scores = (92, 42).
          Player 0 rolls 8 dice and gets outcomes [5, 3, 5, 2, 4, 3, 1, 1].
          End scores = (93, 42)
          >>> print(turns[7])
          Start scores = (93, 42).
          Player 1 rolls 4 dice and gets outcomes [5, 2, 5, 2].
          End scores = (93, 56)
          >>> print(turns[8])
          Start scores = (93, 56).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (97, 56)
          >>> print(turns[9])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=43957, score0=35, score1=51, goal=100)
          >>> print(turns[0])
          Start scores = (35, 51).
          Player 0 rolls 6 dice and gets outcomes [2, 3, 4, 6, 3, 2].
          End scores = (55, 51)
          >>> print(turns[1])
          Start scores = (55, 51).
          Player 1 rolls 4 dice and gets outcomes [5, 3, 1, 1].
          End scores = (55, 52)
          >>> print(turns[2])
          Start scores = (55, 52).
          Player 0 rolls 1 dice and gets outcomes [3].
          End scores = (58, 52)
          >>> print(turns[3])
          Start scores = (58, 52).
          Player 1 rolls 4 dice and gets outcomes [5, 1, 1, 4].
          End scores = (58, 53)
          >>> print(turns[4])
          Start scores = (58, 53).
          Player 0 rolls 10 dice and gets outcomes [2, 5, 3, 3, 4, 5, 5, 3, 6, 6].
          End scores = (100, 53)
          >>> print(turns[5])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=36287, score0=42, score1=52, goal=100)
          >>> print(turns[0])
          Start scores = (42, 52).
          Player 0 rolls 10 dice and gets outcomes [5, 4, 1, 5, 6, 4, 2, 3, 4, 4].
          End scores = (43, 52)
          >>> print(turns[1])
          Start scores = (43, 52).
          Player 1 rolls 10 dice and gets outcomes [3, 4, 6, 2, 4, 2, 4, 6, 4, 3].
          End scores = (43, 90)
          >>> print(turns[2])
          Start scores = (43, 90).
          Player 0 rolls 7 dice and gets outcomes [6, 4, 4, 6, 6, 4, 4].
          End scores = (77, 90)
          >>> print(turns[3])
          Start scores = (77, 90).
          Player 1 rolls 5 dice and gets outcomes [4, 4, 1, 6, 1].
          End scores = (77, 91)
          >>> print(turns[4])
          Start scores = (77, 91).
          Player 0 rolls 7 dice and gets outcomes [6, 2, 6, 5, 4, 1, 3].
          End scores = (78, 91)
          >>> print(turns[5])
          Start scores = (78, 91).
          Player 1 rolls 6 dice and gets outcomes [1, 3, 1, 1, 2, 2].
          End scores = (78, 92)
          >>> print(turns[6])
          Start scores = (78, 92).
          Player 0 rolls 3 dice and gets outcomes [2, 2, 2].
          End scores = (84, 92)
          >>> print(turns[7])
          Start scores = (84, 92).
          Player 1 rolls 6 dice and gets outcomes [1, 5, 4, 5, 2, 3].
          End scores = (84, 93)
          >>> print(turns[8])
          Start scores = (84, 93).
          Player 0 rolls 5 dice and gets outcomes [4, 1, 5, 4, 6].
          End scores = (85, 93)
          >>> print(turns[9])
          Start scores = (85, 93).
          Player 1 rolls 6 dice and gets outcomes [6, 5, 3, 5, 1, 3].
          End scores = (85, 94)
          >>> print(turns[10])
          Start scores = (85, 94).
          Player 0 rolls 3 dice and gets outcomes [2, 5, 1].
          End scores = (86, 94)
          >>> print(turns[11])
          Start scores = (86, 94).
          Player 1 rolls 2 dice and gets outcomes [2, 3].
          End scores = (86, 99)
          >>> print(turns[12])
          Start scores = (86, 99).
          Player 0 rolls 4 dice and gets outcomes [1, 4, 4, 1].
          End scores = (87, 99)
          >>> print(turns[13])
          Start scores = (87, 99).
          Player 0 rolls 6 dice and gets outcomes [4, 1, 3, 2, 6, 2].
          End scores = (88, 99)
          >>> print(turns[14])
          Start scores = (88, 99).
          Player 0 rolls 5 dice and gets outcomes [1, 6, 4, 4, 4].
          End scores = (89, 99)
          >>> print(turns[15])
          Start scores = (89, 99).
          Player 1 rolls 3 dice and gets outcomes [2, 1, 1].
          End scores = (89, 100)
          >>> print(turns[16])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=36008, score0=3, score1=9, goal=11)
          >>> print(turns[0])
          Start scores = (3, 9).
          Player 0 rolls 10 dice and gets outcomes [3, 3, 4, 3, 2, 1, 6, 5, 6, 5].
          End scores = (4, 9)
          >>> print(turns[1])
          Start scores = (4, 9).
          Player 1 rolls 10 dice and gets outcomes [1, 3, 5, 1, 3, 1, 3, 5, 6, 6].
          End scores = (4, 10)
          >>> print(turns[2])
          Start scores = (4, 10).
          Player 0 rolls 2 dice and gets outcomes [1, 4].
          End scores = (5, 10)
          >>> print(turns[3])
          Start scores = (5, 10).
          Player 1 rolls 8 dice and gets outcomes [6, 2, 3, 1, 6, 4, 4, 5].
          End scores = (5, 11)
          >>> print(turns[4])
          Game Over
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> # Fuzz Testing
      >>> # Plays a lot of random games, and calculates a secret value.
      >>> # Failing this test means something is wrong, but you should
      >>> # look at other tests to see where the problem might be.
      >>> # Hint: make sure you're only calling take_turn once per turn!
      >>> #
      >>> import hog, importlib
      >>> # importlib.reload(hog)
      >>> import tests.play_utils
      """,
      'teardown': r"""
      
      """,
      'type': 'doctest'
    }
  ]
}
