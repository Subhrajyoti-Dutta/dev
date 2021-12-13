import java.util.*;

class h {
    public void show() {
        System.out.println("Hello");
    }
}

class g {
    public void show(){
        System.out.println("Jelo");
    }
}

class s extends h {

}

class s extends g {
    
}
public class rough2{
    public static void main(String[] args){
        /*Start Your Code Here*/
        s std = new s();
        std.show();
    }
}