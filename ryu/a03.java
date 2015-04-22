public class a03 {
	public static void main(String[] args){
        String s1 = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.";
        String[] words = s1.split(" ", 0);
        
        for (int n = 0; n < words.length; n = n + 1) {
        	System.out.println(words[n].length());
    	}
    }
}