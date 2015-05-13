import java.util.*;
import java.io.*;

//unix command: cut -f n file 
public class nlp13{
    public static void main(String[] args){
        try{
            BufferedReader br1 = new BufferedReader(new InputStreamReader(
                        new FileInputStream(args[0]),"UTF-8"));

            BufferedReader br2 = new BufferedReader(new InputStreamReader(
                        new FileInputStream(args[1]),"UTF-8"));

			OutputStreamWriter out = new OutputStreamWriter(
					new FileOutputStream("merge.txt"),"UTF-8");

			String cell1 = br1.readLine(); 
			String cell2 = br2.readLine(); 
            while(cell1!=null && cell2!=null){

				String merge = cell1 + "\t" + cell2;
				System.out.println(merge);
				out.write(merge);
				out.write("\n");
				out.flush();

				cell1 = br1.readLine(); 
				cell2 = br2.readLine(); 
			}

        }catch (Exception e){
            e.printStackTrace();
        }
    }
}
