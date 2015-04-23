import java.util.ArrayList;
import java.util.Collections;
import java.util.LinkedList;

public class a09 {
	public static void main(String[] args){
        String sent = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind .";
        LinkedList<String> result_list = new LinkedList<String>();
        for(String tok : sent.split(" ")){
        	if(tok.length() <= 4){
        		result_list.add(tok);
        		continue;
        	}
        	ArrayList<Character> t = new ArrayList<Character>();
        	StringBuffer sb = new StringBuffer();
        	for(int i=1; i<=tok.length()-2; i++){
        		t.add(tok.charAt(i));
        	}
        	Collections.shuffle(t);
        	t.add(tok.charAt(tok.length()-1));
        	t.add(0, tok.charAt(0));
        	for(Character c : t){
        		sb.append(c);
        	}
        	result_list.add(sb.toString());

        }

        System.out.println(sent);
        
        StringBuilder sb = new StringBuilder();
        for (String str : result_list) {
        	if (sb.length() > 0) {
        		sb.append(" ");
        	}
        	sb.append(str);
        }
        System.out.println(sb.toString());
    }
}