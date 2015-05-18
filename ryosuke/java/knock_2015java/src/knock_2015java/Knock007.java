/**
 * 
 */
package knock_2015java;

/**
 * @author ryosuke
 *
 */
public class Knock007 extends Knock {

	/**
	 * 
	 */
	public Knock007() {
		// TODO 自動生成されたコンストラクター・スタブ
	}

	/* (非 Javadoc)
	 * @see knock_2015java.Knock#start()
	 */
	@Override
	public void start() {
		System.out.println(template("12", "気温", "22.4"));
	}

	public String template(String x, String y, String z){
		return String.format("%s時の%sは%s", x, y, z);
	}
}
