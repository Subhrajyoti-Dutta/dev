import java.util.*;

public class Main {
    public static void main(String[] args){
        Scanner scan = new Scanner( System.in );
        HashMap<String, Integer> numbers = new HashMap<String, Integer>();
        numbers.put("zero", 0);
        numbers.put("one",  1);
        numbers.put("two",  2);
        numbers.put("three",3);
        numbers.put("four", 4);
        numbers.put("five", 5);
        numbers.put("six",  6);
        numbers.put("seven",7);
        numbers.put("eight",8);
        numbers.put("nine", 9);
        StringBuffer numDigits = new StringBuffer();
        String numWords = scan.next();
        String[] numDigitsWord = numWords.split(" ");
        int i = -1;
        while (++i < numDigitsWord.length) {
            if (numDigitsWord[i].equals("double")) {
                numDigits.append(numbers.get(numDigitsWord[++i]));
                numDigits.append(numbers.get(numDigitsWord[i]));
            } else if (numDigitsWord[i].equals("triple")) {
                numDigits.append(numbers.get(numDigitsWord[++i]));
                numDigits.append(numbers.get(numDigitsWord[i]));
                numDigits.append(numbers.get(numDigitsWord[i]));
            } else {
                numDigits.append(numbers.get(numDigitsWord[i]));
            }
        }
        System.out.println(numDigits.toString());
    }
}