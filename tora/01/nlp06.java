import java.util.*;
import java.io.*;
import org.apache.commons.lang.*;


public class nlp06{
    public static void main(String[] args){
		String str1 = "paraparaparadise";
		String str2 = "paragraph";
		
		HashMap X = createSet(bigramChar.parsetoBigram(str1));
		HashMap Y = createSet(bigramChar.parsetoBigram(str2));
		//intersection(X,Y);
		//union(X,Y);
		difference(X,Y);
		//for(Iterator i=X.keySet().iterator(); i.hasNext();)
		//	System.out.println(i.next());
    } 

	public static HashMap createSet(String[] str){
		HashMap<String,Integer> bigram = new HashMap<String,Integer>();
		for(int i=0; i<str.length; i++){
			if(!bigram.containsKey(str[i])) bigram.put(str[i],1);
			else{
				int oldValue = bigram.get(str[i]); 
				bigram.put(str[i],oldValue+1);
			}
		}
		return bigram;
	}

	public static void intersection(HashMap X, HashMap Y){
		for(Iterator i=X.keySet().iterator(); i.hasNext();){
			String bigramX = (String)i.next();
			if(Y.containsKey(bigramX))
				System.out.println(bigramX);
		}
	}

	public static void union(HashMap X, HashMap Y){
		for(Iterator i=Y.keySet().iterator(); i.hasNext();){
			String bigramY = (String)i.next();
			System.out.println(bigramY);
		}
		for(Iterator i=X.keySet().iterator(); i.hasNext();){
			String bigramX = (String)i.next();
			if(!Y.containsKey(bigramX))
				System.out.println(bigramX);
		}
	}

	public static void difference(HashMap X, HashMap Y){
		for(Iterator i=X.keySet().iterator(); i.hasNext();){
			String bigramX = (String)i.next();
			if(Y.containsKey(bigramX))
				continue;
			else
				System.out.println(bigramX);
		}
	}
}
