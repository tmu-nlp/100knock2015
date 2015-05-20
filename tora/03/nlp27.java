import java.util.*;
import java.util.regex.*;
import java.io.*;

public class nlp27{

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

				Pattern pattern_start  = Pattern.compile(unicode_s);
				Pattern pattern_end    = Pattern.compile("\\}\\}");
                Pattern pattern_emphasize = Pattern.compile("(.*?)\\'\\'+(.*?)\\'\\'+(.*?)");
                Pattern pattern_innerlink = Pattern.compile("(.*?)\\[\\[+(.*?)\\]\\]+(.*?)");
                Pattern pattern_main   = Pattern.compile("\\|(.*) = (.*)");

                Matcher matcher_start = pattern_start.matcher(line);
                Matcher matcher_end   = pattern_end.matcher(line);

                if(matcher_start.matches()) flag = 1;

                if(flag == 1){
                    Matcher matcher_main = pattern_main.matcher(line);
                    if(matcher_main.matches()){
                        String key   = matcher_main.group(1);
                        String value = matcher_main.group(2);
                       
                        Matcher matcher_emphasize = pattern_emphasize.matcher(value);
                        while(matcher_emphasize.matches()){
                            value = matcher_emphasize.group(1)+matcher_emphasize.group(2)+matcher_emphasize.group(3);
                            matcher_emphasize = pattern_emphasize.matcher(value);
                        }

                        Matcher matcher_innerlink = pattern_innerlink.matcher(value);
                        while(matcher_innerlink.matches()){
                            value = matcher_innerlink.group(1)+matcher_innerlink.group(2)+matcher_innerlink.group(3);
                            matcher_innerlink = pattern_innerlink.matcher(value);
                        }
                            

                        map.put(key,value);
                        System.out.printf("%s:%s\n",key,value);
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
