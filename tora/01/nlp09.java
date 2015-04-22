import java.util.*;
import java.io.*;
import java.lang.*;


public class nlp09{
    public static void main(String[] args){
		String str = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind .";
		String new_str = Typoglycemia(str);
		System.out.print(new_str);
		//System.out.println(decode(encode(str1)));
    } 

	public static String Typoglycemia(String str){
		String[] words = str.split(" ");
		int len = words.length;

		int count_move = 0;
		for(int i=0; i<len; i++){
			if(!(i==0 || i==len-1 || words[i].length()<=4))
				count_move++;
		}

		int[] sequence = new int[count_move];
		for(int i=0; i<len; i++){
			if(!(i==0 || i==len-1 || words[i].length()<=4)){
				int rand = (int)(Math.random()*len);
				while(rand==0 || rand==len-1 || words[rand].length()<=4)
					rand = (int)(Math.random()*len);
				String temp = words[i];
				words[i] = words[rand];
				words[rand] = temp;
			}
		}
	
		return toString(words);
	}

	public static String toString(String[] words){
		String sent = "";
		
		for(int i=0; i<words.length; i++)
			sent = sent + words[i] + " ";

		sent = sent.trim();

		return sent;
	}

}
