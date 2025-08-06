
import java.util.Scanner;

public class DoublyLinkedList {

    Node head;
    int length;

    public DoublyLinkedList() {
        this.head = null;
        this.length = 0;
    }

    class Node {

        Node next;
        Node prev;
        int data;

        Node(int data) {
            this.next = null;
            this.prev = null;
            this.data = data;
        }
    }

    public void insertAtBeginning(int data) {
        length++;
        if (head == null) {
            head = new Node(data);
            return;
        }
        Node newNode = new Node(data);
        newNode.next = head;
        head.prev = newNode;
        head = newNode;
    }

    public void insertAtEnd(int data) {
        length++;
        if (head == null) {
            head = new Node(data);
            return;
        }
        Node currNode = head;
        while (currNode.next != null) {
            currNode = currNode.next;
        }
        Node newNode = new Node(data);
        currNode.next = newNode;
        newNode.prev = currNode;
    }

    public void insertAtPos(int data, int pos) {
        if (pos == 1) {
            insertAtBeginning(data);
            return;
        }
        if (pos <= 0 || pos > length) {
            System.out.println("Invalid position");
            return;
        }
        length++;
        if (pos == length) {
            insertAtEnd(data);
            return;
        }
        Node currNode = head;
        for (int i = 0; i < pos - 2; i++) {
            currNode = currNode.next;
        }
        Node newNode = new Node(data);
        newNode.next = currNode.next;
        newNode.prev = currNode;
        currNode.next.prev = newNode;
        currNode.next = newNode;

    }

    public void printList() {
        Node currNode = head;
        while (currNode != null) {
            System.out.print(currNode.data + "<->");
            currNode = currNode.next;
        }
        System.out.println("null");
    }

    public void deleteAtBeginning() {
        if (head == null) {
            System.out.println("List is empty..");
            return;
        }
        length--;
        head = head.next;
        head.prev = null;
    }

    public void deleteAtEnd() {
        if (head == null) {
            System.out.println("List is empty..");
            return;
        }

        length--;
        if (head.next == null) {
            head = head.next;
            return;
        }

        Node currNode = head;
        while (currNode.next.next != null) {
            currNode = currNode.next;
        }
        currNode.next = null;
    }

    public void deleteAtpos(int pos) {

        if (pos < 0 && pos >= length) {
            System.out.println("Invalid position!!");
            return;
        }
        if (pos == 1) {
            deleteAtBeginning();
            return;
        } else if (pos == length - 1) {
            deleteAtEnd();
            return;
        }
        length--;
        Node currNode = head;
        for (int i = 0; i < pos - 2; i++) {
            currNode = currNode.next;
        }
        currNode.next = currNode.next.next;
        currNode.next.prev = currNode;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        DoublyLinkedList list = new DoublyLinkedList();
        int x = 0, data = 0;
        boolean i = true;
        while (i) {
            System.out.print("Enter the following choices:\n1)Insert at beginning\n2)Insert at end\n3)Insert at position\n4)delete at beginning\n5)delete at end\n6)delete at pos\n7)display\n8)exit\nEnter:");

            x = sc.nextInt();
            switch (x) {
                case 1:
                    System.out.print("Enter the data to be inserted:");
                    data = sc.nextInt();
                    list.insertAtBeginning(data);
                    break;
                case 2:
                    System.out.print("Enter the data to be inserted:");
                    data = sc.nextInt();
                    list.insertAtEnd(data);
                    break;
                case 3:
                    System.out.print("Enter the data to be inserted:");
                    data = sc.nextInt();
                    System.out.print("Enter the position in which the data is to be inserted:");
                    int pos = sc.nextInt();
                    list.insertAtPos(data, pos);
                    break;
                case 4:
                    list.deleteAtBeginning();
                    break;
                case 5:
                    list.deleteAtEnd();
                    break;
                case 6:
                    System.out.print("Enter the position to delete:");
                    pos = sc.nextInt();
                    list.deleteAtpos(pos);
                    break;
                case 7:
                    list.printList();
                    break;
                case 8:
                    System.out.println("Exiting..........");
                    i = false;
                default:
                    System.out.println("Enter the correct option..");
                    break;
            }
        }

    }
}
