import java.util.Stack;


public class LonComSubSeq {
	
	public static int getMaxValue(int[] array){  
	      int maxValue = array[0];  
	      for(int i=1;i < array.length;i++){  
	      if(array[i] > maxValue){  
	      maxValue = array[i];  

	         }  
	     }  
	             return maxValue;  
	}  
	
	String input1="saturday";
	String input2="sunday";
	public boolean existbefore(int a,char b){
		boolean temp=false;
		for (int i=0;i<a;i++){
			if(input1.charAt(i)==b){
				temp=true;
			}
		}
		return temp;
	}
	
	public boolean existafter(int a,char b){
		boolean temp=false;
		for (int i=a;i<input1.toString().length();i++){
			if(input1.charAt(i)==b){
				temp=true;
			}
		}
		return temp;
	}
	
	public int[] positions(){
		int []temp=new int[input2.length()];
		for(int i=0;i<input2.length();i++){
			temp[i]=input1.indexOf(input2.charAt(i));
			if(temp[i]==-1){temp[i]=0;}
		}
		return temp;
	}
	
	public static void main(String[] args) {
		LonComSubSeq obj=new LonComSubSeq();
		int []ls=new int[obj.input2.length()];
		int []prev=new int[obj.input2.length()+1];
		int []pos=obj.positions();
		ls[0]=1;
		pos[0]=obj.input1.toString().indexOf(obj.input2.toCharArray()[0]);
		for (int i=1;i<obj.input2.length();i++){
			char crntchar=obj.input2.toCharArray()[i];
			int max=0,temp=1;
			for(int j=i-1;j>=0;j--){
				if(obj.existafter(pos[j], crntchar)){
					temp=ls[j]+1;
					if(temp>max){max=temp;}
					
				}
				else if(obj.existbefore(pos[j], crntchar)){
						temp=ls[obj.input1.toString().indexOf(crntchar)];
						if(temp>max){max=temp;}			
				}
				else{
					temp=0;
					if(temp>max){max=temp;}
				}
			}
			ls[i]=max;
			System.out.println(ls[i]);
		}
		


		for(int i=0;i<=ls.length-1;i++)
			System.out.println(ls[i]);
		
		System.out.println("longest seq length "+getMaxValue(ls));
	}
}
