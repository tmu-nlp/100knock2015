import java.util.Arrays;
import java.util.Iterator;
import java.util.TreeSet;

public class a06 {
	public static void main(String[] args){
        String s1 = "paraparaparadise";
        String s2 = "paragraph";
        String[] s1bigrams = new String[s1.length() - 1];
        String[] s2bigrams = new String[s2.length() - 1];
        TreeSet<String> union = new TreeSet<String>();
        TreeSet<String> setdifference = new TreeSet<String>(); //s2 - s1ÇÃï˚ÇÃç∑èWçá
        TreeSet<String> intersection = new TreeSet<String>();
                
        for (int n = 0; n < s1.length() - 1; n = n + 1) {
        	s1bigrams[n] = s1.substring(n, n + 2);
        	union.add(s1.substring(n, n + 2));
        } 
        
        for (int n = 0; n < s2.length() - 1; n = n + 1) {
        	s2bigrams[n] = s2.substring(n, n + 2);
        	union.add(s2.substring(n, n + 2));
        	if(Arrays.asList(s1bigrams).contains(s2bigrams[n])){
        		intersection.add(s2.substring(n, n + 2));
        	} else{
        		setdifference.add(s2.substring(n, n + 2));
            }
        }
        
        Iterator<String> it = union.iterator();
        while (it.hasNext()) {
            System.out.println(it.next());
        }
        
        System.out.println("");
        
        it = setdifference.iterator();
        while (it.hasNext()) {
            System.out.println(it.next());
        }
        
        System.out.println("");
        
        it = intersection.iterator();
        while (it.hasNext()) {
            System.out.println(it.next());
        }
        
        System.out.println("");
        
        if(Arrays.asList(s1bigrams).contains("se")){
            System.out.println("paraparaparadise have se");
        } else{
            System.out.println("paraparaparadise don't have se");
        }
        if(Arrays.asList(s2bigrams).contains("se")){
            System.out.println("paragraph have se");
        } else{
            System.out.println("paragraph don't have se");
        }
    }
}