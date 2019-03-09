import unittest

class Answer():
  def solve(self, arr):
    bucket = {}
    newArr = []
    for el in arr:
      if (el <= 0):
        continue
      elif (el in bucket):
        continue
      newArr.append(el)

    newArr.sort()

    # if there is no positive anymore, return first positvie number: 1
    if (len(newArr) < 1):
      return 1

    prev = newArr[0]
    if (prev != 1):
      return 1

    for i in range(1, len(newArr)):
      if (newArr[i] - prev > 1):
        return prev + 1
      prev = newArr[i]
    return newArr[-1] + 1



class TestCase(unittest.TestCase):
  def test_num_1(self):
    self.assertEqual(2, Answer().solve([3, 4, -1, 1]))
  def test_num_2(self):
    self.assertEqual(3, Answer().solve([1, 2, -1, 0]))
  def test_num_3(self):
    self.assertEqual(1, Answer().solve([-1, -2, -1, 0]))
  def test_num_4(self):
    self.assertEqual(1, Answer().solve([-1, -1, -1, -1]))
  def test_num_5(self):
    self.assertEqual(1, Answer().solve([]))
  def test_num_6(self):
    self.assertEqual(3, Answer().solve([5,6,7,8,1,2]))
  def test_num_7(self):
    self.assertEqual(4, Answer().solve([5, 10, 15, 3, -100, 1, 7,8, 2]))
  def test_num_8(self):
    self.assertEqual(4, Answer().solve([2, 2, 2, 3, 3, 3, 1, 1, 1, 10, 15, 3, -100, 1, 7]))
  def test_num_9(self):
    self.assertEqual(4, Answer().solve([ 2, 3, -7, 6, 8, 1, -10, 15 ]))
  def test_num_10(self):
    self.assertEqual(1, Answer().solve([2, 3, 7, 6, 8, -1, -10, 15]))



def main():
  unittest.main()

if __name__ == "__main__":
  main()
