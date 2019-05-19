import java.util.List;
import java.util.ArrayList;
import java.util.Stack;

public class Test {
  public static void main(String[] args) {
    Test test = new Test();
    test.testcase();
  }

  public void testcase() {
    Traversal tr = new Traversal();
    tr.testcase();
  }


  public class Traversal {
    public void testcase() {
      TreeNode<Integer> root = new TreeNode<Integer>(2);
      TreeNode<Integer> left = new TreeNode<Integer>(1);
      TreeNode<Integer> right = new TreeNode<Integer>(3);
      root.left(left);
      root.right(right);

      List<Integer> recursive = this.inOrderRecursive(root);
      System.out.println("recursive " + recursive);
      List<Integer> iterative = this.inOrderIterative(root);
      System.out.println("iterative " + iterative);
    }

    public List<Integer> inOrderRecursive(TreeNode root) {
      List<Integer> list = new ArrayList<>();
      return this.inOrderRecursiveHelper(root, list);
    }

    private List<Integer> inOrderRecursiveHelper(TreeNode<Integer> root, List<Integer> list) {
      if (root == null) {
        return null;
      }

      this.inOrderRecursiveHelper(root.left, list);
      list.add(root.val);
      this.inOrderRecursiveHelper(root.right, list);
      return list;
    }

    public List<Integer> inOrderIterative(TreeNode<Integer> root) {
      List<Integer> list = new ArrayList<>();
      Stack<TreeNode> st = new Stack<>();

      TreeNode<Integer> ptr = root;

      while(ptr != null || !st.empty()) {
        while (ptr != null) {
          st.push(ptr);
          ptr = ptr.left;
        }

        // ptr is null;
        ptr = st.pop();
        list.add(ptr.val);
        ptr = ptr.right;
      }

      return list;
    }
  }
}
