public class a05 {
	public static void main(String[] args){
        String sent = "I am an NLPer";
        String[] words = sent.split(" ", 0);
        
        for (int a = 2; a < 20 ; a++) {
        	getbigram(sent, a);
        	System.out.println("");
        	getbigram(words, a);
        	System.out.println("");
        }
    }

	private static void getbigram(String sent, Integer a) {
		for (int n = 0; n < sent.length() - a + 1; n++) {
    		System.out.println(sent.substring(n, n + a));
       	}
	}

	private static void getbigram(String[] words, Integer a) {
		for (int n = 0; n < words.length - a + 1; n++) {
			for (int i = 0; i < a; i++) {
				System.out.printf("%s ", words[n + i]);
			}
			System.out.println("");
		}
	}	
}
