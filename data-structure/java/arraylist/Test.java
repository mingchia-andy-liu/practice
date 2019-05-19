import java.util.List;
import java.util.Arrays;
import java.util.stream.Collectors;

public class Test {
  public static void main(String[] args) {
    Test test = new Test();
    test.testCase();
  }

  public void testCase() {
    int[] array = {1, 2, 3, 4, 5};
    List<Integer> list = convertArrayToList(array);

    for (Integer i : list) {
      System.out.println("i is : " + i);
    }
  }

  /**
   * @params {int[]} input array
   */
  public List<Integer> convertArrayToList(int[] input) {
    // === METHOD 1 ===
    // This does not work. Because List<int> is not possible. int is not a primitive
    // `Arrays.asList` does not deal with boxing and will just create a List<int[]>
    // List<Integer> list = new ArrayList<Integer>(Arrays.asList(input));
    List lst = Arrays.asList(input);
    System.out.println(lst.size()); // prints one
    System.out.println(lst.get(0)); // references to the array


    // === METHOD 2 ===
    // Java 8 - Use stream and boxed method
    List<Integer> list = Arrays.stream(input).boxed().collect(Collectors.toList());

    return list;
  }
}
