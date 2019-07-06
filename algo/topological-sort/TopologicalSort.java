import java.util.*;

public class TopologicalSort {
  public class Graph {
    // No. of vertices
    public int V;
    // Adjacency List
    public List<List<Integer>> adj;

    Graph(int v) {
      this.V = v;
      this.adj = new ArrayList<List<Integer>>(v);
      for (int i = 0; i < v; i++) {
          adj.add(i, new ArrayList<Integer>());
      }
    }

    public void addEdge(int u, int v) {
        this.adj.get(u).add(v);
    }
  }


  public boolean isCyclicUtil(Graph g, int node, boolean[] visited, boolean[] stack) {
    // if it's already of the stack
    if (stack[node]) { return true; }

    // if it has been visited, ignore this node
    if (visited[node]) { return false; }

    visited[node] = true;
    stack[node] = true;

    List<Integer> adjacency = g.adj.get(node);

    for (Integer a: adjacency) {
      if (isCyclicUtil(g, a, visited, stack)) {
        return true;
      }
    }

    stack[node] = false;
    return false;
  }

  public boolean isCyclic(Graph g) {
    // for each node, to verify has it been visited before
    boolean[] visited = new boolean[g.V];
    // for each node, to verify is it part of the DFS per iteration
    boolean[] stack = new boolean[g.V];

    for (int i = 0; i < g.V; i++) {
      if (isCyclicUtil(g, i, visited, stack)) {
        return true;
      }
    }

    return false;
  }


  //
  /**
   * A util function to perform Depth First Search on the adjacency nodes
   *
   * @param g
   * @param node
   * @param visited
   * @param stack
   * @return true if solution cannot be found
   */
  public boolean TopSortUtil(Graph g, int node, int[] visited, Stack<Integer> stack) {
    if (visited[node] == 1) {
      System.out.println("there is a cycle. current node: " + node);
      return true;
    }

    if (visited[node] == 2) { return false; }
    // mark the value to be visiting
    visited[node] = 1;

    List<Integer> adjacency = g.adj.get(node);
    // DFS
    for (Integer a: adjacency) {
      if (TopSortUtil(g, a, visited, stack)) {
        return true;
      }
    }

    // Add the current value "at", If Only IF, all its dependencies are in the stack.
    stack.push((Integer)node);
    visited[node] = 2;
    return false;
  }

  // Finds a topological ordering of the nodes in a Directed Acyclic Graph (DAG)
  public int[] TopSort(Graph g) {
    int[] res = new int[g.V];

    // 0 means has not visited
    // 1 meaning visiting (in stack)
    // 2 means visited
    int[] visited = new int[g.V];
    Stack<Integer> stack = new Stack<Integer>();

    for (int i = 0; i < g.V; i++) {
      if (visited[i] == 0 && TopSortUtil(g, i, visited, stack)) {
        return new int[0];
      }
    }

    for (int i = g.V - 1; i >= 0; i--) {
      res[i] = stack.pop();
    }

    return res;
  }

  public void start() {
    Graph cycle = new Graph(2);

    cycle.addEdge(0, 1);
    cycle.addEdge(1, 0);
    boolean hasCycle = isCyclic(cycle);
    System.out.println("Graph a: should have a cycle has a cycle: " + hasCycle);

    Graph g = new Graph(10);
    g.addEdge(0, 2);
    g.addEdge(1, 2);
    g.addEdge(1, 3);
    g.addEdge(3, 5);
    g.addEdge(4, 5);
    g.addEdge(6, 8);
    g.addEdge(7, 8);
    g.addEdge(8, 9);

    int[] ordering = TopSort(g);
    // [2, 0, 5, 3, 1, 4, 9, 8, 6, 7]
    System.out.println(Arrays.toString(ordering));
  }

  public static void main(String[] args) {
    TopologicalSort tsort = new TopologicalSort();
    tsort.start();
  }
}

