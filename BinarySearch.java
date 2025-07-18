
import java.util.*;

public class BinarySearch {

    public static final Scanner sc = new Scanner(System.in);

    public static void inputarr(int[] arr) {
        int len = arr.length;
        System.out.println("Enter the elements of the array");
        for (int i = 0; i < len; i++) {
            arr[i] = sc.nextInt();
        }
    }

    public static void main(String[] args) {
        //input stuffs
        Scanner sc = new Scanner(System.in);
        System.out.print("Length of the Array:");
        int n = sc.nextInt();
        int arr[] = new int[n];
        inputarr(arr);
        System.out.print("Number to Search:");
        int x = sc.nextInt();

        //Binary Search
        int high = n;
        int low = 0;

        while (low <= high - 1) {
            int mid = low + (high - low) / 2;
            if (arr[mid] == x) {
                System.out.println("The element is in position:" + (mid + 1));
                break;
            } else if (x < arr[mid] && low < mid) {
                high = mid;
            } else if (x > arr[mid] && high > mid) {
                low = mid;
            }
        }

    }
}
