import java.util.*;

class Random {
    int i;
    Random rand;

    void increase(int ip) {
        i += ip;
    }

    int get() {
        return i;
    }
}

public class rough1{
    public static void main(String[] args){
        Random a;
        Random b = new Random();
        Random c = b.rand;
        // System.out.println(a.get());
        // a.increase(2);
        // System.out.println(a.i);
        System.out.println(c);
    }
}