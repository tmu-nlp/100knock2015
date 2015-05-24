import java.util.*;
import java.util.regex.*;
import java.io.*;

public class nlp21{

    public static void main(String[] args){
		match();

    }

	public static void match(){
		
		String output = "";
		try{
            BufferedReader br = new BufferedReader(new InputStreamReader(
                        new FileInputStream("article.txt"),"UTF-8"));
           	for(String line = br.readLine(); line != null; line = br.readLine()){
				Pattern pattern = Pattern.compile(".*Category.*");
				Matcher matcher = pattern.matcher(line);
				if(matcher.matches())
					System.out.println(line);
			}
		}catch (Exception e){
			e.printStackTrace();
		}
	} 
}
