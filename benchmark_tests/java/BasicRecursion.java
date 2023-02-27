public class BasicRecursion {

  public static int fib(int n) {
    if (n <= 1) {
      return n;
    } else {
      return fib(n - 1) + fib(n - 2);
    }
  }

  public static void main(String[] args) {
    for (int i = 0; i < 30; i++) {
      long startTime = System.currentTimeMillis();
      fib(40);
      long endTime = System.currentTimeMillis();

      long duration = endTime - startTime;

      System.out.printf("%dms\n", duration);
    }
  }
}
