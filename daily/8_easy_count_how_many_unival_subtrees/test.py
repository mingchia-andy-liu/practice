import unittest

# Copied from somehwere
class Node:
  def __init__(self, data):
    self.left = None
    self.right = None
    self.data = data

  def val(self):
    return self.data

  def insertLeft(self, tree):
    self.left = tree

  def insertRight(self, tree):
    self.right = tree

  def PrintTree(self):
    if self.left:
        self.left.PrintTree()
    print( self.data),
    if self.right:
        self.right.PrintTree()

def Solution(root: Node):
  if (root is None):
    return 0

  leftCount = Solution(root.left)
  rightCount = Solution(root.right)

  rootCount = 0
  rootVal = root.val()
  if (root.left is not None and root.left.val() == rootVal and root.right is not None and root.right.val() == rootVal):
    rootCount = 1

  if (root.left is None and root.right is None):
    rootCount += 1

  return leftCount + rightCount + rootCount


class TestCase(unittest.TestCase):
  def test_num_1(self):
    root = Node(0)
    left = Node(1)
    right = Node(0)
    rigthRight = Node(0)

    rigthLeft = Node(1)
    rigthLeftLeft = Node(1)
    rigthLeftRight = Node(1)
    rigthLeft.insertLeft(rigthLeftLeft)
    rigthLeft.insertRight(rigthLeftRight)

    right.insertLeft(rigthLeft)
    right.insertRight(rigthRight)

    root.insertLeft(left)
    root.insertRight(right)

    sol = Solution(root)
    self.assertEqual(sol, 5)
  def test_num_2(self):
    root = Node(0)
    sol = Solution(root)
    self.assertEqual(sol, 1)
  def test_num_3(self):
    root = Node(0)
    left = Node(1)
    right = Node(0)
    rigthRight = Node(0)
    right.insertRight(rigthRight)

    root.insertLeft(left)
    root.insertRight(right)

    sol = Solution(root)
    self.assertEqual(sol, 2)

def main():
  unittest.main()


if __name__ == "__main__":
  main()
