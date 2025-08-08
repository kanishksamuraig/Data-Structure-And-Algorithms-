
import java.util.Scanner;
//stack using linked list mate.

public class StackLL {

    Node head;
    int size;

    StackLL() {
        head = null;
        size = 0;
    }

    class Node {

        int data;
        Node next;

        Node(int data) {
            this.data = data;
            this.next = null;
        }
    }

    public boolean isEmpty() {
        return head == null;
    }

    public void push(int data) {
        Node newNode = new Node(data);
        size++;
        if (isEmpty()) {
            head = newNode;

            return;
        }
        newNode.next = head;
        head = newNode;
    }

    public int pop() {
        if (isEmpty()) {
            return -1;
        }
        int data = head.data;
        head = head.next;
        return data;
    }

    public int peek() {
        if (isEmpty()) {
            return -1;
        }
        int data = head.data;
        return data;
    }

    public void display() {
        Node currNode = head;
        while (currNode != null) {
            System.out.print(currNode.data + " ");
            currNode = currNode.next;
        }

    }

    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        StackLL stack = new StackLL();
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
