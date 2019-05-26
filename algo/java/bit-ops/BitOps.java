
public class BitOps {
  public static void main(String[] args) {
    int A = 10;
    int B = 3;

    // === 32 singed bit here ===
    // Left Shifts "<<"
    // 0 is appended at the least significant bit
    // 0000 0000 0000 0000 0000 0000 0000 0001 --> 1
    // 1000 0000 0000 0000 0000 0000 0000 0000 --> -2147483648
    int a = 1 << 31;

    // Arithmetic Right Shifts ">>>" (unsigned)
    // Logical Right Shifts ">>" (signed)

    System.out.println("a is " + a);
    System.out.println("b is " + b);
  }
}
