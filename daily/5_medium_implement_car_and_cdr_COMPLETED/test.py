import unittest


def cons(a, b):
  '''Provided'''
  def pair(f):
    return f(a, b)
  return pair

def car(pair):
  def first(a, b):
    return a
  return pair(first)

def cdr(pair):
  def last(a, b):
    return b
  return pair(last)

class TestCase(unittest.TestCase):
  def test_num_1(self):
    self.assertEqual(3, car(cons(3, 4)))
    self.assertEqual(4, cdr(cons(3, 4)))


def main():
  unittest.main()


if __name__ == "__main__":
  main()
