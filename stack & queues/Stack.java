
public class Stack {

    Node head;

    Stack() {
        this.head = null;
    }

    class Node {

        Node next;
        int data;

        Node(int data) {
            this.next = null;
            this.data = data;
        }
    }

    public Boolean isEmpty() {
        return head == null;
    }

    public void push(int data) {
        Node newNode = new Node(data);
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
        return head.data;
    }

    public static void main(String args[]) {
        Stack s = new Stack();
        s.push(10);
        s.push(20);
        s.push(30);
        while (!s.isEmpty()) {
            System.out.println(s.pop() + " ");
        }

    }

}
