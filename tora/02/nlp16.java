import java.util.*;
import java.io.*;

//unix command: tail -n file
public class nlp16{
    public static void main(String[] args){
        try{
            BufferedReader br = new BufferedReader(new InputStreamReader(
                        new FileInputStream(args[0]),"UTF-8"));


            int len = 0;
            while(br.readLine()!=null) len++ ;
			br.close();
			int N = Integer.parseInt(args[1]);
			int[] num = new int[N];

			for(int i=0; i<num.length;i++)
				num[i] = len/N;
			int comp = len%N;
			for(int i=0; i<comp; i++)
				num[i]++; 

            br = new BufferedReader(new InputStreamReader(
                        new FileInputStream(args[0]),"UTF-8"));
			for(int i=0; i<num.length; i++){
				for(int j=0; j<num[i]; j++)
					System.out.println(br.readLine());
				System.out.println();
			}
			

        }catch (Exception e){
            e.printStackTrace();
        }
    }
}
