import java.util.*;
import java.io.*;

//unix command: wc file
public class nlp10{
    public static void main(String[] args){
        try{
            BufferedReader br = new BufferedReader(new InputStreamReader(
                        new FileInputStream(args[0]),"UTF-8"));

            int i = 0;
            while(br.readLine()!=null) i++ ;
			System.out.println(i);

        }catch (Exception e){
            e.printStackTrace();
        }
    }
}
