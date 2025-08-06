
public class MergeSort {

    public static void mergeSort(int arr[], int n) {
        if (n <= 1) {
            return;
        }
        int leftarr[] = new int[n / 2];
        int rightarr[] = new int[n - n / 2];
        int middle = n / 2, j = 0;
        for (int i = 0; i < n; i++) {
            if (i < middle) {
                leftarr[i] = arr[i];
            } else {
                rightarr[j] = arr[i];
                j++;
            }
        }
        mergeSort(leftarr, middle);
        mergeSort(rightarr, n - middle);
        merge(leftarr, rightarr, arr, n);

    }

    public static void merge(int left[], int right[], int arr[], int n) {
        int middle = n / 2;
        int leftsize = middle, rightsize = n - middle;
        int l = 0, r = 0, i = 0;
        while (l < leftsize && r < rightsize) {
            if (left[l] < right[r]) {
                arr[i] = left[l];
                i++;
                l++;
            } else {
                arr[i] = right[r];
                i++;
                r++;
            }
        }
        while (r < rightsize) {

            arr[i] = right[r];
            i++;
            r++;
        }
        while (l < leftsize) {

            arr[i] = left[l];
            i++;
            l++;

        }

    }

    public static void main(String[] args) {
        int a[] = {30, 20, 10};
        mergeSort(a, a.length);
        for (int i = 0; i < a.length; i++) {
            System.out.print(a[i] + " ");
        }
    }
}
