import java.util.*;
import java.util.regex.*;
import java.io.*;

public class nlp23{

    public static void main(String[] args){
		match();

    }

	public static void match(){
		
		String output = "";
		try{
            BufferedReader br = new BufferedReader(new InputStreamReader(
                        new FileInputStream("article.txt"),"UTF-8"));
           	for(String line = br.readLine(); line != null; line = br.readLine()){
				Pattern pattern = Pattern.compile("(=+)(.*?)(=+)");
				Matcher matcher = pattern.matcher(line);
				if(matcher.matches()){
					int level = matcher.group(1).length()-1;
					System.out.printf("%s\t%d\n",matcher.group(2),level);
				}
			}
		}catch (Exception e){
			e.printStackTrace();
		}
	} 
}
