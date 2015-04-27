import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Iterator;
import java.util.Comparator;

public class a18 {
    public static void main(String argv[]) throws IOException {
    	FileReader fr = new FileReader("/Users/tachibanaryuichi/Documents/workspace/100knock2015/hightemp.txt");
    	BufferedReader br = new BufferedReader(fr);
    	ArrayList<LineClass> word_list = new ArrayList<LineClass>();
    	
    	String line = br.readLine();
    	while (line != null) {
    		String[] words = line.split("	", 0);
    		word_list.add(new LineClass(words[0], words[1], words[2], words[3]));
    		line = br.readLine();
    	}
        br.close();
        
        //LineComparatorクラスの条件に従いソートする
        Collections.sort(word_list, new LineComparator());

        //結果を画面表示する
        Iterator<LineClass> it = word_list.iterator();
        while (it.hasNext()) {
        	LineClass data = it.next();
        	System.out.println(data.getprefecture() + "\t" + data.getregion() + "\t" + data.gettemperature() + "\t" + data.getdate());
        }
    }
}

class LineClass {
	private String prefecture;
	private String region;
	private String temperature;
	private String date;

	//コンストラクタ
	public LineClass(String prefecture, String region, String temperature, String date) {
		this.prefecture = prefecture;
		this.region = region;
		this.temperature = temperature;
		this.date = date;
	}
	
	public String getprefecture() {
		return this.prefecture;
	}
	
	public String getregion() {
		return this.region;
	}
	
	public String gettemperature() {
		return this.temperature;
	}
	
	public String getdate() {
		return this.date;
	}
}

class LineComparator implements Comparator<LineClass> {

    //比較メソッド(データクラスを比較して-1, 0, 1を返すように記述する)
    public int compare(LineClass a, LineClass b) {
        String no1 = a.gettemperature();
        String no2 = b.gettemperature();

        //こうすると温度の昇順でソートされる
        if (Float.parseFloat(no1) < Float.parseFloat(no2)) {
            return 1;

        } else if (no1 == no2) {
            return 0;
        } else {
            return -1;
        }
    }
}