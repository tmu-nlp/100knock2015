import java.util.*;
import java.util.regex.*;
import java.io.*;

public class nlp25{

    public static void main(String[] args){
		match();

    }

	public static void match(){
		
		try{
            BufferedReader br = new BufferedReader(new InputStreamReader(
                        new FileInputStream("article.txt"),"UTF-8"));

            int flag = 0;
            HashMap<String,String> map = new HashMap<String,String>(); 

           	for(String line = br.readLine(); line != null; line = br.readLine()){

                String unicode_s = new String(".*基礎情報.*".getBytes(),"UTF-8");

				Pattern pattern_start = Pattern.compile(unicode_s);
				Pattern pattern_end   = Pattern.compile("\\}\\}");
                Pattern pattern       = Pattern.compile("\\|(.*) = (.*)");

                Matcher matcher_start = pattern_start.matcher(line);
                Matcher matcher_end   = pattern_end.matcher(line);

                if(matcher_start.matches()) flag = 1;

                if(flag == 1){
                    Matcher matcher = pattern.matcher(line);
                    if(matcher.matches()){
                        map.put(matcher.group(1),matcher.group(2));
                        System.out.printf("%s:%s\n",matcher.group(1),matcher.group(2));
                    }
                }

                else if(flag == 1 && matcher_end.matches())
                    break;
			}
		}catch (Exception e){
			e.printStackTrace();
		}
	} 
}
