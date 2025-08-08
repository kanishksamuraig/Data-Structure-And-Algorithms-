
import java.util.*;

public class StackArrayImplementation {

    static class Stack {

        static ArrayList<Integer> stack = new ArrayList<>();

        static public boolean isEmpty() {
            return stack.size() == 0;
        }

        static public void push(int data) {
            stack.add(data);
        }

        static public int pop() {
            if (isEmpty()) {
                return -1;
            }
            int top = stack.get(stack.size() - 1);
            stack.remove(stack.size() - 1);
            return top;
        }

        static public int peek() {
            if (isEmpty()) {
                return -1;
            }
            return stack.get(stack.size() - 1);
        }

        static public void display() {
            if (isEmpty()) {
                System.out.println("Stack empty");
                return;
            }
            for (int i : stack) {
                System.out.print(i + " ");
            }
            System.out.println();
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Stack stack = new Stack();
        int x = 0, data = 0;
        boolean i = true;
        while (i) {
            System.out.print("Enter the following choices:\n1)push\n2)pop\n3)peek\n4)display\n5)exit");

            x = sc.nextInt();
            switch (x) {
                case 1:
                    System.out.print("Enter the data to be inserted:");
                    data = sc.nextInt();
                    stack.push(data);
                    break;
                case 2:
                    data = stack.pop();
                    System.out.println(data == -1 ? "Empty stack" : data);
                    break;
                case 3:
                    data = stack.peek();
                    System.out.println(data == -1 ? "Empty stack" : data);
                    break;
                case 4:
                    stack.display();
                    break;
                case 5:
                    System.out.println("exiting...");
                    i = false;
                    break;
                default:
                    System.out.println("enter correct choice...");
                    break;

            }
        }
    }
}
