import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Thing {
    public static void main(String[] args) {
        int[] myarr = new int[5];
        for (int i = 0; i < 5; i++) {
            myarr[i] = i;
        }

        int i=1;
        for (i++; i<myarr.length; i++){
            System.out.println(i);
        }

        System.out.println(Arrays.toString(myarr));
    }
}