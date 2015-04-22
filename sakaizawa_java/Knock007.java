/**
07. テンプレートによる文生成
引数x, y, zを受け取り「x時のyはz」という文字列を返す関数を実装せよ．さらに，x=12, y="気温", z=22.4として，実行結果を確認せよ．
 */

/**
 * @author sakaisawayuya
 *
 */
public class Knock007 {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO 自動生成されたメソッド・スタブ
		System.out.println(template("12", "気温", "22.4"));
	}

	private static String template(String x, String y, String z) {
		// TODO 自動生成されたメソッド・スタブ
		return String.format("%s時の%sは%s", x, y, z);
	}

}
