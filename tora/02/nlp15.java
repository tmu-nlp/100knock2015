import java.util.*;
import java.io.*;

//unix command: tail -n file
public class nlp15{
    public static void main(String[] args){
        try{
            BufferedReader br = new BufferedReader(new InputStreamReader(
                        new FileInputStream(args[0]),"UTF-8"));


			String[] lines = new String[100];
			int i=0;
			for(String line = br.readLine(); line!=null;
					line = br.readLine()){
				lines[i] = line;
				i++;
			}
			
			int n = Integer.parseInt(args[1]);
			int j = i - n + 1;
			for(; j<i; j++)
				System.out.println(lines[j]);

        }catch (Exception e){
            e.printStackTrace();
        }
    }
}
