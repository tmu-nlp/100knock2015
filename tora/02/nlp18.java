import java.util.*;
import java.io.*;
import org.apache.commons.lang.StringUtils;

//unix command: sort -k 2 -k 1 file
public class nlp18{
    public static void main(String[] args){
        try{
            BufferedReader br = new BufferedReader(new InputStreamReader(
                        new FileInputStream(args[0]),"UTF-8"));

			List<String[]> lines = new LinkedList<String[]>();
			for(String line=br.readLine(); line!=null; line=br.readLine()){
				String[] cells = line.split("\t");
				lines.add(cells);
			}

			sort(lines);
			//for(Iterator i=dict.keySet().iterator(); i.hasNext();){
			//	int cell = (Integer)i.next();
			//	System.out.printf("%d\t%s",cell,dict.get(cell));
			//	System.out.println();
			//}

        }catch (Exception e){
            e.printStackTrace();
        }
    }
	public static void sort(List list){
		Collections.sort(list, new Comparator<String[]>() {
			public int compare(String[] obj1, String[] obj2){
				return (-1)*obj1[2].compareTo(obj2[2]);
			}
		});
		for(Iterator<String[]> ite = list.iterator();ite.hasNext();){
			String[] cells = ite.next();
			System.out.println(StringUtils.join(cells,"\t"));
		}
	}

}
