
import java.util.*;

class Array {

    private int arr[];
    private int size = 0, length;

    public Array(int[] array, int length) {
        this.arr = array;
        this.length = length;
    }

    public Array(int length) {
        this.arr = new int[length];
        this.length = length;
    }

    // void swap(int a, int b) {
    //     int temp = a;
    //     a = b;
    //     b = temp;
    // }
    void insertAtBeginning(int key) {
        for (int i = size; i > 0; i--) {
            arr[i] = arr[i - 1];
        }
        arr[0] = key;
        size++;

    }

    void insertAtEnd(int key) {
        arr[size] = key;
        size++;
    }

    void insertAtPos(int pos, int key) {
        if (pos < 0 || pos > size) {
            System.out.println("Invalid position");
            return;
        } else if (pos == 0) {
            insertAtBeginning(key);
        } else {
            for (int i = size; i >= pos; i--) {
                arr[i] = arr[i - 1];
            }
            arr[pos - 1] = key;

        }
        size++;

    }

    void deleteAtBeginning() {
        for (int i = 0; i < size; i++) {
            arr[i] = arr[i + 1];
        }
        size--;
    }

    void deleteAtEnd() {
        arr[size - 1] = arr[size];
        size--;
    }

    void deleteAtPos(int pos) {
        for (int i = pos - 1; i <= size; i++) {
            arr[i] = arr[i + 1];
        }
        size--;
    }

    void printArray() {
        for (int i = 0; i < size; i++) {
            System.out.print(arr[i] + " ");
        }
        System.out.println();
    }

}

public class ArrayDataStructure {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int arr[] = new int[100], x, pos;
        Array array = new Array(arr, 100);
        boolean t = true;
        while (t) {
            System.out.print("Enter one of the following operation\n\t1)Create Array\n\t2)Insert At beginning\n\t3)Insert At End\n\t4)Insert At a Position\n\t5)print array\n\t6)Delete at beginning\n\t7)Delete at end\n\t8)Delete at position\n\t9)Exit\nEnter:");
            x = sc.nextInt();
            switch (x) {
                case 1:
                    System.out.print("Enter the Size of the Array to be created:");
                    int length = sc.nextInt();
                    arr = new int[length];
                    array = new Array(arr, length);
                    System.out.print("Enter the element to be inserted:");
                    array.insertAtBeginning(sc.nextInt());
                    break;
                case 2:
                    System.out.print("Enter the element to be inserted at the beginning:");
                    array.insertAtBeginning(sc.nextInt());
                    break;
                case 3:
                    System.out.print("Enter the element to be inserted at the end of the array:");
                    array.insertAtEnd(sc.nextInt());
                    break;
                case 4:
                    System.out.print("Enter the position in which the element is to be inserted:");
                    pos = sc.nextInt();
                    System.out.print("Enter the element to be inserted:");
                    array.insertAtPos(pos, sc.nextInt());
                    break;
                case 5:
                    System.out.print("Array:");
                    array.printArray();
                    break;
                case 6:
                    array.deleteAtBeginning();
                    break;
                case 7:
                    array.deleteAtEnd();
                    break;
                case 8:
                    System.out.print("Enter the position of the array to be deleted:");
                    pos = sc.nextInt();
                    break;
                case 9:
                    System.out.print("Exiting....");
                    t = false;
                    break;
                default:
                    System.out.print("Enter the correct choice:");
                    break;
            }
        }
    }
}
