import java.io.*;
import java.math.*;
import java.util.*;
public class LongIncSubSeq {
	public static int getMaxValue(int[] array){  
	      int maxValue = array[0];  
	      for(int i=1;i < array.length;i++){  
	      if(array[i] > maxValue){  
	      maxValue = array[i];  

	         }  
	     }  
	             return maxValue;  
	}  
	public static void main(String[] args) {
		int[] input={10,22,9,33,21,50,41,60,80};
		//finding length of subseq on all sub problems
		int []ls=new int[input.length];
		int []prev=new int[input.length+1];
		ls[0]=1;
		for(int i=1;i<input.length;i++){
			int max=1,temp=0;ls[i]=1;
			for (int j=i-1;j>=0;j--){
				//System.out.println(input[j]);
				if(input[i]>input[j]){
						temp=ls[j]+1;
						//System.out.println(input[i]+" "+input[j]);
					if(temp>max){max=temp;}
				}
				else{
					temp=1;
					if(temp>max){max=temp;}
					}
			}
			ls[i]=max;
			
		}
		
		for(int i=0;i<=ls.length-1;i++)
			System.out.println(ls[i]);
		
		System.out.println("longest seq length "+getMaxValue(ls));
		
	}

}
