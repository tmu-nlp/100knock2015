import java.util.*;
import java.util.regex.*;
import java.io.*;

public class nlp29{

    public static void main(String[] args) throws Exception{
        HashMap<String,String> map = new HashMap<String,String>(); 
		map = match();
        flaglink(map);

    }

    public static void flaglink(HashMap map) throws Exception{
        String str1 = new String("略名".getBytes(),"UTF-8");
        String str2 = new String("国旗画像".getBytes(),"UTF-8");
        String country  = (String)map.get(str1);
        String filename = (String)map.get(str2);
        System.out.printf("ja.wikipedia.org/wiki/%s#/media/File:%s",country,filename);
    }

	public static HashMap match(){
        
        HashMap<String,String> map = new HashMap<String,String>(); 
		
		try{
            BufferedReader br = new BufferedReader(new InputStreamReader(
                        new FileInputStream("article.txt"),"UTF-8"));

            int flag = 0;

           	for(String line = br.readLine(); line != null; line = br.readLine()){

                String unicode_s = new String(".*基礎情報.*".getBytes(),"UTF-8");

				Pattern pattern_start  = Pattern.compile(unicode_s);
				Pattern pattern_end    = Pattern.compile("\\}\\}");
                Pattern pattern_main   = Pattern.compile("\\|(.*) = (.*)");
                Pattern pattern_emphasize = Pattern.compile("(.*?)\\'\\'+(.*?)\\'\\'+(.*?)");
                Pattern pattern_innerlink = Pattern.compile("(.*?)\\[\\[+(.*?)\\]\\]+(.*?)");
                Pattern pattern_ref1      = Pattern.compile("(.*?)<ref.*?</ref>(.*?)");
                Pattern pattern_ref2      = Pattern.compile("(.*?)<ref.*?>(.*?)");
                Pattern pattern_br        = Pattern.compile("(.*?)<br */>(.*?)");

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
                            
                        Matcher matcher_ref1 = pattern_ref1.matcher(value);
                        while(matcher_ref1.matches()){
                            value = matcher_ref1.group(1)+matcher_ref1.group(2);
                            matcher_ref1 = pattern_ref1.matcher(value);
                        }

                        Matcher matcher_ref2 = pattern_ref2.matcher(value);
                        while(matcher_ref2.matches()){
                            value = matcher_ref2.group(1)+matcher_ref2.group(2);
                            matcher_ref2 = pattern_ref2.matcher(value);
                        }

                        Matcher matcher_br = pattern_br.matcher(value);
                        while(matcher_br.matches()){
                            value = matcher_br.group(1)+matcher_br.group(2);
                            matcher_br = pattern_br.matcher(value);
                        }

                        map.put(key,value);
                    }
                }

                else if(flag == 1 && matcher_end.matches())
                    break;
			}
		}catch (Exception e){
			e.printStackTrace();
		}

        return map;
	} 
}
