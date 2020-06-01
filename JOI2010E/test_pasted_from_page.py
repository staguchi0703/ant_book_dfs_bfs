#
from resolve import resolve
####################################
####################################
# 以下にプラグインの内容をペーストする
#
import sys
from io import StringIO
import unittest


class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)

    def test_入力例_1(self):
        input = """3 3 1
S..
...
..1"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4 5 2
.X..1
....X
.XX.S
.2.X."""
        output = """12"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """10 10 9
.X...X.S.X
6..5X..X1X
...XXXX..X
X..9X...X.
8.X2X..X3X
...XX.X4..
XX....7X..
X..X..XX..
X...X.XX..
..X......."""
        output = """91"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
