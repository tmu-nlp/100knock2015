import java.util.*;
import java.io.*;
import org.json.*;

public class nlp21{

    public static void main(String[] args){
		try{
		    String output = readjson("jawiki-country.json");
		    JSONObject jsonObj = new JSONObject(output);

            String title = jsonObj.getString("title");
            String title_unicode = new String(title.getBytes(),"UTF-8")
            String text  = jsonObj.getString("text");
            
            
            if(title_unicode.equals("イギリス"))
                System.out.println(text);

		}catch (JSONException e){}
    }

	public static String readjson(String json_file){
		
		String output = "";
		try{
            BufferedReader br = new BufferedReader(new InputStreamReader(
                        new FileInputStream(json_file),"UTF-8"));
           	for(String line = br.readLine(); line != null; line = br.readLine())
				output += line;
		}catch (Exception e){
			e.printStackTrace();
		}

		return output;
	} 
}
