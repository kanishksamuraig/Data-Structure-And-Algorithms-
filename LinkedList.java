
public class LinkedList {

    Node head;

    class Node {

        private int data;
        private Node next;

        Node(int data) {
            this.data = data;
            this.next = null;
        }
    }

    public void insertAtBeginning(int data) {
        if (head == null) {
            head = new Node(data);
            return;
        }
        Node newNode = new Node(data);
        newNode.next = head;
        head = newNode;
    }

    public void insertAtEnd(int data) {
        if (head == null) {
            head = new Node(data);
            return;
        }
        Node currNode = head;
        Node newNode = new Node(data);
        while (currNode.next != null) {
            currNode = currNode.next;
        }
        currNode.next = newNode;
    }

    public void insertAtPosition(int data, int pos) {
        Node currNode = head;
        int length = 0;
        while (currNode != null) {
            currNode = currNode.next;
            length++;
        }
        length++;
        if (pos < 1 || pos > length) {
            System.out.println("Enter a Valid Position");
            return;
        }
        Node newNode = new Node(data);
        currNode = head;
        for (int i = 1; i < pos - 1; i++) {
            currNode = currNode.next;
        }
        newNode.next = currNode.next;
        currNode.next = newNode;

    }

    public void printList() {
        Node currNode = head;
        while (currNode != null) {
            System.out.print(currNode.data + "->");
            currNode = currNode.next;
        }
        System.err.println("null");
    }

    public static void main(String[] args) {
        LinkedList list = new LinkedList();
        list.insertAtBeginning(1);
        list.insertAtEnd(2);
        list.insertAtEnd(3);
        list.insertAtEnd(4);
        list.insertAtPosition(5, 3);
        list.printList();

    }
}
