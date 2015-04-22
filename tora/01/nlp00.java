import java.util.*;
import java.io.*;

public class nlp00{
    public static void main(String[] args){
        String str = "stressed";
        char[] chars = str.toCharArray();
        int len = chars.length;
        for(int i=len-1; i>=0; i--){
            System.out.print(chars[i]);
        }
    } 
}
