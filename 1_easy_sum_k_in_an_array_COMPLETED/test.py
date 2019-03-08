import unittest

class Answer():
  def __init__(self, k, arr):
    self.k = k
    self.arr = arr
    self.dict = {}

  def solve(self):
    if (len(self.arr) < 2):
      return False
    for element in self.arr:
      diff = self.k - element
      self.dict[diff] = True

    for element in self.arr:
      if (element in self.dict):
        return True
    return False

class Answer2():
  def __init__(self, k, arr):
    self.k = k
    self.arr = arr
    self.add = {}
    self.minus = {}

  def solve(self):
    if (len(self.arr) < 2):
      return False
    for element in self.arr:
      diff = self.k - element
      # diff in add for matching up with actual element in the array
      if (diff in self.add):
        return True
      # element in minus for matching current element with the diff of previous elements
      if (element in self.minus):
        return True

      self.minus[diff] = True
      self.add[element] = True
    return False


class TestCase(unittest.TestCase):
  def test_num_1(self):
    ans = Answer(1, [])
    self.assertEqual(False, ans.solve())
  def test_num_2(self):
    ans = Answer(5, [2, 1, 10, 5, 6, 2])
    self.assertEqual(False, ans.solve())
  def test_num_3(self):
    ans = Answer(1, [1, 1, 1, 1, 1])
    self.assertEqual(False, ans.solve())
  def test_num_4(self):
    ans = Answer(2, [2, 1, 2, 1, 2, 1])
    self.assertEqual(True, ans.solve())
  def test_num_4(self):
    ans = Answer(17, [10, 5, 2, 3, 7])
    self.assertEqual(True, ans.solve())
  def test_num_5(self):
    ans = Answer(1, [2, -1, 0, 1])
    self.assertEqual(True, ans.solve())
  def test_num_6(self):
    ans = Answer(-1, [-2, 1, 0, 1, 2, 3, 4, 5])
    self.assertEqual(True, ans.solve())
  def test_num_7(self):
    ans = Answer(1, [1])
    self.assertEqual(False, ans.solve())
  def test_num_8(self):
    ans = Answer(-5, [1, 10, 2, 4, 5, 61, 2, -2, -5])
    self.assertEqual(False, ans.solve())
  def test_num_9(self):
    ans = Answer(0, [0, 0, 0, 0, 0])
    self.assertEqual(True, ans.solve())
  def test_num_10(self):
    ans = Answer(5, [1, 2, 3, 4, 5, 6, 7, -1, -2, -3, -5, 10])
    self.assertEqual(True, ans.solve())

class TestCase2(unittest.TestCase):
  def test_num_1(self):
    ans = Answer2(1, [])
    self.assertEqual(False, ans.solve())
  def test_num_2(self):
    ans = Answer2(5, [2, 1, 10, 5, 6, 2])
    self.assertEqual(False, ans.solve())
  def test_num_3(self):
    ans = Answer2(1, [1, 1, 1, 1, 1])
    self.assertEqual(False, ans.solve())
  def test_num_4(self):
    ans = Answer2(2, [2, 1, 2, 1, 2, 1])
    self.assertEqual(True, ans.solve())
  def test_num_4(self):
    ans = Answer2(17, [10, 5, 2, 3, 7])
    self.assertEqual(True, ans.solve())
  def test_num_5(self):
    ans = Answer2(1, [2, -1, 0, 1])
    self.assertEqual(True, ans.solve())
  def test_num_6(self):
    ans = Answer2(-1, [-2, 1, 0, 1, 2, 3, 4, 5])
    self.assertEqual(True, ans.solve())
  def test_num_7(self):
    ans = Answer2(1, [1])
    self.assertEqual(False, ans.solve())
  def test_num_8(self):
    ans = Answer2(-5, [1, 10, 2, 4, 5, 61, 2, -2, -5])
    self.assertEqual(False, ans.solve())
  def test_num_9(self):
    ans = Answer2(0, [0, 0, 0, 0, 0])
    self.assertEqual(True, ans.solve())
  def test_num_10(self):
    ans = Answer2(5, [1, 2, 3, 4, 5, 6, 7, -1, -2, -3, -5, 10])
    self.assertEqual(True, ans.solve())



def main():
  unittest.main()

if __name__ == "__main__":
  main()
