import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;

public class a04 {
	public static void main(String[] args){
        String s1 = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.";
        String[] words = s1.split(" ", 0);
        ArrayList<Integer> number_list = new ArrayList<Integer>(Arrays.asList(1, 5, 6, 7, 8, 9, 15, 16, 19));
        HashMap<Integer, String> chemical_symbol_map = new HashMap<Integer, String>();
        
        for (int n = 0; n < words.length; n = n + 1) {
        	if (number_list.contains(n + 1)) {
//        		System.out.print(words[n].substring(0, 1));
        		chemical_symbol_map.put(n, words[n].substring(0, 1));
            } else {
//                System.out.print(words[n].substring(0, 2));
                chemical_symbol_map.put(n, words[n].substring(0, 2));
            }
        	System.out.println(chemical_symbol_map.get(n));
    	}
    }
}