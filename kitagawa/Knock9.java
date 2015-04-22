/**
 * 
 */
package java_new100knock;

/**
 * @author kitagawayoshiaki
 *
 */
import java.util.Random;

public class Knock9 {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		String sentence = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind .";
		String[] sentence_array = sentence.split(" ", 0);
		//Randomクラスのインスタンス化
        Random rnd = new Random();
        int ran = rnd.nextInt(10);
        System.out.println(ran);
	}

}
