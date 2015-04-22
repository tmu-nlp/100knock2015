import java.util.*;
import java.io.*;

public class nlp02{
    public static void main(String[] args){
        String str1 = "¥Ñ¥È¥«©`";
        String str2 = "¥¿¥¯¥·©`";
        char[] chars1 = str1.toCharArray();
        char[] chars2 = str2.toCharArray();
        if(chars1.length == chars2.length){
		for(int i=0; i<chars1.length; i++){
                System.out.print(chars1[i]);
	        System.out.print(chars2[i]);
	}
        }
    } 
}
