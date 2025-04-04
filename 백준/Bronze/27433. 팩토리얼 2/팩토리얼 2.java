
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        System.out.println(func(N));
    }
    public static long func(int num){

        if(num ==0 || num == 1){
            return 1;
        }
        return num * func(num-1);
    }
}
