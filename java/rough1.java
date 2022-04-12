import java.util.*;

class Main {
    static int firstFalse(boolean arr[], int start) {
        for (int i = start; i < arr.length; i++) {
            if (arr[i] == false) {
                return i;
            }
        }
        return -1;
    }
    public static void main(String[] args) {
        int N = 5;
        int X[] = { 3, 2, 5, 6, 4 };
        boolean coloured[] = new boolean[5];
        Arrays.fill(coloured, false);
        int count = 0;
        int leastFalse = 0;
        do {
            count++;
            int lastColoured = leastFalse;
            coloured[leastFalse] = true;
            for (int i = leastFalse; i < N; i++) {
                if (coloured[i] == false && X[i] > X[lastColoured]) {
                    coloured[i] = true;
                    lastColoured = i;
                }
            }
            leastFalse = firstFalse(coloured,leastFalse);
        } while(leastFalse != -1);
        System.out.println(count);
    }
}