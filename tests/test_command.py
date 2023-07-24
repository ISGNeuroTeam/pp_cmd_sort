"""Module for testing sort command"""
import subprocess
from unittest import TestCase

SAMPLE_HEAD = [["alpha", "beta", "gamma", "delta"]]
SAMPLE = [["1", "AAA", "12AB", "Frog"],
          ["1", "CCC", "BB13", "Drain"],
          ["1", "AAA", "J7", "Bed"],
          ["2", "AAA", "10001", "Gravity"],
          ["2", "CCC", "10002", "Hour"],
          ["2", "BBB", "1000001", "Cherry"],
          ["3", "CCC", "3", "I_word"],
          ["3", "BBB", "15", "Apple"],
          ["3", "BBB", "2365", "Egg"]]


def capture(s):
    """Captures the output of postprocessing
    command s and turns it into a list"""
    x = subprocess.run(["pp", s],
                       check=False,
                       capture_output=True).stdout.decode()
    x = [n.split() for n in x[:-1].split("\n")]
    x = [x[0]] + [lst[1:] for lst in x[1:]]
    return x


def draw_nd(n: int, ol: list):
    """Creates a list that contains every
    nd element of each sublist of list ol"""
    nl = []
    for sublist in ol:
        elem_i = sublist[n]
        nl.append(elem_i)
    return nl


class TestCommand(TestCase):
    """Class for testing sort command"""

    def test(self):
        for i in range(0, 4):
            for j in ["asc", "des"]:
                test_string = f"| readFile example_003.csv " \
                              f"type=csv storage=pp_storage " \
                              f"| sort '{j}' by {SAMPLE_HEAD[0][i]}"
                result = capture(test_string)
                r = j == "des"
                sample = SAMPLE_HEAD + \
                    sorted(SAMPLE, key=lambda k: k[i], reverse=r)
                sample = draw_nd(i, sample)
                result = draw_nd(i, result)
                self.assertEqual(result, sample)
