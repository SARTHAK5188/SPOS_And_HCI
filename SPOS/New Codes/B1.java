import java.io.*;
import java.util.*;
class B1 {
    static {
        System.loadLibrary("B1");
    }

    private native int add(int a, int b);
    private native int sub(int a, int b);
    private native int mult(int a, int b);
    private native int div(int a, int b);

    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int a, b, ch;
        System.out.println("\nEnter value of a : ");
        a = sc.nextInt();
        System.out.println("\nEnter value of b : ");
        b = sc.nextInt();

        
        B1 obj = new B1();

        do {
            System.out.println("\nMENU:");
            System.out.println("1. Add");
            System.out.println("2. Subtract");
            System.out.println("3. Multiply");
            System.out.println("4. Divide");
            System.out.println("5. Exit");
            System.out.println("\nENTER YOUR CHOICE : ");
            ch = sc.nextInt();

            int result;
            switch(ch) {
                case 1:
                    result = obj.add(a, b);
                    System.out.printf("\nResult of addition: %d\n", result);
                    break;
                case 2:
                    result = obj.sub(a, b);
                    System.out.printf("\nResult of subtraction: %d\n", result);
                    break;
                case 3:
                    result = obj.mult(a, b);
                    System.out.printf("\nResult of multiplication: %d\n", result);
                    break;
                case 4:
                    result = obj.div(a, b);
                    System.out.printf("\nResult of division: %d\n", result);
                    break;
                case 5:
                    System.out.println("Exiting...");
                    break;
                default:
                    System.out.println("Your choice is wrong.");
            }
        } while(ch != 5);
    }
}
