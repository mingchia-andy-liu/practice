class TreeNode<T> {
  T val;
  TreeNode left;
  TreeNode right;

  TreeNode(T val) {this.val = val;}

  public TreeNode getLeft() { return this.left; }
  public TreeNode getRight() { return this.right; }

  public void left(TreeNode root) { this.left = root; }

  public void right(TreeNode root) { this.right = root; }
}
