from hog import play, always_roll
from dice import make_test_dice

def echo(s0, s1):
    print(s0, s1)
    return echo
s0, s1 = play(always_roll(1), always_roll(1), dice=make_test_dice(3), goal=5, say=echo)   