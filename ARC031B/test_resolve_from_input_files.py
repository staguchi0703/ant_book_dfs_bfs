
import sys
from io import StringIO
import unittest

from resolve import resolve

class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)

    def test_from_io_txt(self):

        file_path = __file__.rsplit('/',1)[0]

        with open(file_path + '/input.txt') as f:
            input = f.read()

        with open(file_path + '/output.txt') as g:
            output = g.read()

        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()