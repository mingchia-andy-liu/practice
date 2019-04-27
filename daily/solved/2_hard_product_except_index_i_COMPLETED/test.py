import unittest

class Answer():
  def solve(self, arr):
    if (len(arr) == 0):
      return []
    elif (len(arr) == 1):
      return [0]

    num_z = 0
    product = 1
    for el in arr:
      if (el != 0):
        product *= el
      else:
        num_z += 1

    if (num_z > 1):
      return [0] * len(arr)

    output = []
    for el in arr:
      if (el == 0):
        output.append(product)
      elif (num_z == 1 and el != 0):
        output.append(0)
      else:
        output.append(product / el)
    return output

# class Answer2():
#   def solve(self):



class TestCase(unittest.TestCase):
  # overriding the TestCase's __init__
  def __init__(self, *args, **kwargs):
    super(TestCase, self).__init__(*args, **kwargs)
    self.ans = Answer()

  def test_num_1(self):
    self.assertEqual([120, 60, 40, 30, 24], self.ans.solve([1, 2, 3, 4, 5]))
  def test_num_2(self):
    self.assertEqual([600, 1200, 120, 240, 200, 600], self.ans.solve([2, 1, 10, 5, 6, 2]))
  def test_num_3(self):
    self.assertEqual([0], self.ans.solve([1]))
  def test_num_4(self):
    self.assertEqual([1, 1, 1, 1, 1], self.ans.solve([1, 1, 1, 1, 1]))
  def test_num_5(self):
    self.assertEqual([120, -60, 40, -30, 24], self.ans.solve([-1, 2, -3, 4, -5]))
  def test_num_6(self):
    self.assertEqual([0, 0, 120, 0, 0], self.ans.solve([3, 2, 0, 4, 5]))
  def test_num_7(self):
    self.assertEqual([0, 0, 0, 0, 0], self.ans.solve([0, 2, 0, 4, 5]))
  def test_num_8(self):
    self.assertEqual([100000000000000, 100000000000000, 100000000000000], self.ans.solve([10000000, 10000000, 10000000]))
  def test_num_9(self):
    self.assertEqual([-24, -12, -8, -6], self.ans.solve([-1, -2, -3, -4]))
  def test_num_9(self):
    self.assertEqual([0, 0, -40, 0, 0], self.ans.solve([-1, -2, 0, -4, 5]))
  def test_num_10(self):
    self.assertEqual([40, 20, -40, 10, -8], self.ans.solve([-1, -2, 1, -4, 5]))



def main():
  unittest.main()

if __name__ == "__main__":
  main()
