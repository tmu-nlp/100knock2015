public class a08 {
	static String input_s;
	
	public static void main(String[] args){
		input_s = "Test Stringあいうえお123.,/";
		System.out.println("Input_string");
		System.out.println(input_s);
		System.out.println("Encode");
		cipher();
		System.out.println("Decode");
		cipher();
	}
	
	public static void cipher(){
		StringBuffer sb = new StringBuffer();
		for(int i = 0;i < input_s.length();i++){
			if(Character.isLowerCase(input_s.charAt(i))){
				sb.append((char)(219 - (int)input_s.charAt(i)));
			}else{
				sb.append(input_s.charAt(i));
			}
		}
		System.out.println(sb);
		input_s = sb.toString();
	}
}
