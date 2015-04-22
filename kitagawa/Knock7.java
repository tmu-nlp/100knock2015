/**
 * 
 */
package java_new100knock;

/**
 * @author kitagawayoshiaki
 *
 */
public class Knock7 {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		int x = 12;
		String y = "気温" ;
		double z = 22.4;
		String result = gettemp(x,y,z); //関数の呼出
		System.out.println(result);


	}
	public static String gettemp(int x, String y, double z)  //関数
	{
		  String temp= y;
		  String s = String.valueOf(x);
		  String u = String.valueOf(z);
		  temp = s+"時の"+temp+"は"+u;
		  return temp;
	}

}
