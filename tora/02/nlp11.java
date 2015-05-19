import java.util.*;
import java.io.*;
//unix command: sed 's/\t/\ /g' file
public class nlp11{
    public static void main(String[] args){
        try{
            BufferedReader br = new BufferedReader(new InputStreamReader(
                        new FileInputStream(args[0]),"UTF-8"));

			String line = br.readLine(); 
            while(line!=null){
			line = line.replace("\t"," ");
			System.out.println(line);
			line = br.readLine();
			}

        }catch (Exception e){
            e.printStackTrace();
        }
    }
}
