public class a00 {
	public static void main(String[] args){
        String s = new String("stressed");

        for (int n = s.length(); n > 0; n--) {
        System.out.print(s.substring(n - 1, n));
    	}
    	System.out.println();
    }
}