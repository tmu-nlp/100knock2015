import java.util.*;
import java.io.*;

//unix command: head -n file
public class nlp14{
    public static void main(String[] args){
        try{
            BufferedReader br = new BufferedReader(new InputStreamReader(
                        new FileInputStream(args[0]),"UTF-8"));


            int i = Integer.parseInt(args[1]);
            while(i>0){
				System.out.println(br.readLine());
				i--;
			}

        }catch (Exception e){
            e.printStackTrace();
        }
    }
}
