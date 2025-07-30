
public class Patterns {

    public static void main(String[] args) {
        /* 
            * * * * * * * * * 
            * * * * * * * * * 
            * * * * * * * * * 
            * * * * * * * * * 
            * * * * * * * * * 
            * * * * * * * * * 
            * * * * * * * * * 
            * * * * * * * * * 
            * * * * * * * * *
         */
        //Rectangle
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                System.out.print("* ");
            }
            System.out.println();
        }
        //hollow rectangle
        for (int i = 1; i <= 5; i++) {
            for (int j = 1; j <= 5; j++) {
                if (i == 1 || i == 5 || j == 1 || j == 5) {
                    System.out.print("* ");
                } else {
                    System.out.print("  ");
                }

            }
            System.out.println();
        }
        //half pyramid
        for (int i = 1; i <= 4; i++) {
            for (int j = 1; j <= i; j++) {
                System.out.print("* ");
            }

            System.out.println();
        }
        //inverted half pyramid
        int n = 4;
        for (int i = n; i >= 1; i--) {
            for (int j = 1; j <= i; j++) {
                System.out.print("* ");
            }
            System.out.println();
        }
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n - i; j++) {
                System.out.print("  ");
            }
            for (int j = 1; j <= i; j++) {
                System.err.print("* ");
            }
            System.out.println();
        }

    }
}
