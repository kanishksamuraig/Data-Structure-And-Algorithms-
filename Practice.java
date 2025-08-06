
import java.util.*;

public class Practice {

    public static void main(String[] args) {
        //System.out.print("Enter your hubby's name:");
        Scanner sc = new Scanner(System.in);
        StringBuilder str = new StringBuilder("Samurai");
        //System.out.print("Enter your name:");
        StringBuilder str2 = new StringBuilder("Shruthi");
        str2.append(str);
        str2.insert(7, " ");
        str2.replace(8, 15, "Kanishk Samurai");
        System.out.println("Your new name:" + str2);

        str2.reverse();
        System.out.println("Your name but reversed:" + str2 + " " + str2.capacity());
        str2.reverse();
        System.out.println(str2.charAt(10));
        for (int i = 0; i < str2.length(); i++) {
            System.out.print(str2.charAt(i) + " ");
        }
        str2.deleteCharAt(10);
        System.out.println(str2);
        System.out.println(str2.indexOf("Samurai"));
        System.out.println(str2);
        String str3 = str2.toString();
        System.out.println(str3);
        for (int i = 0; i < 3 - 1; i++) {
            System.out.print(i + " ");
        }
    }
}
