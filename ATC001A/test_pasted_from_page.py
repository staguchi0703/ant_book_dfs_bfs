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
        print('------------')
        print(out)
        print('------------')
        self.assertEqual(out, output)
    def test_入力例1(self):
        input = """4 5
s####
....#
#####
#...g"""
        output = """No"""
        self.assertIO(input, output)
    def test_入力例2(self):
        input = """4 4
...s
....
....
.g.."""
        output = """Yes"""
        self.assertIO(input, output)
    def test_入力例3(self):
        input = """10 10
s.........
#########.
#.......#.
#..####.#.
##....#.#.
#####.#.#.
g.#.#.#.#.
#.#.#.#.#.
###.#.#.#.
#.....#..."""
        output = """No"""
        self.assertIO(input, output)
    def test_入力例4(self):
        input = """10 10
s.........
#########.
#.......#.
#..####.#.
##....#.#.
#####.#.#.
g.#.#.#.#.
#.#.#.#.#.
#.#.#.#.#.
#.....#..."""
        output = """Yes"""
        self.assertIO(input, output)
    def test_入力例5(self):
        input = """1 10
s..####..g"""
        output = """No"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()