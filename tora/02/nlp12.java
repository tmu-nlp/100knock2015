import java.util.*;
import java.io.*;

//unix command: cut -f n file 
public class nlp12{
    public static void main(String[] args){
        try{
            BufferedReader br = new BufferedReader(new InputStreamReader(
                        new FileInputStream(args[0]),"UTF-8"));

			OutputStreamWriter out1 = new OutputStreamWriter(
					new FileOutputStream("col1.txt"),"UTF-8");
			OutputStreamWriter out2 = new OutputStreamWriter(
					new FileOutputStream("col2.txt"),"UTF-8");

			String line = br.readLine(); 
            while(line!=null){
				String[] cells = line.split("\t");

				System.out.println(cells[0] + "\t" + cells[1]);
				out1.write(cells[0]);
				out1.write("\n");
				out1.flush();

				out2.write(cells[1]);
				out2.write("\n");
				out2.flush();

				line = br.readLine(); 
			}
			out1.close();
			out2.close();

        }catch (Exception e){
            e.printStackTrace();
        }
    }
}
