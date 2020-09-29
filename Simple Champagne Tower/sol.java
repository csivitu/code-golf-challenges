import java.util.*; 

public class SCT
{ 
	static int n, t; 

	public static int champagneGlasses(int n, int t) 
	{ 
		
		double Tower[][] = new double[n][n]; 

		Tower[0][0] = t * 1.0; 
		
		int glasses = 0; 

		for (int i = 0; i < n; i++) 
		{   // Number of glasses at each level= j 
			for (int j = 0; j <= i; j++) 
			{   // excess champagne
				double overflow = Tower[i][j] - 1.0;
				
				if (overflow < 0) 
					continue; 

				glasses++; 

				// there is a left-bottom glass
				if (i + 1 < n) 
					Tower[i + 1][j] += overflow / 2; 

				// there is a right-bottom glass
				if (i + 1 < n && j + 1 < n) 
					Tower[i + 1][j + 1] += overflow / 2; 
			} 
		} 

		return glasses; 
	} 

	public static void main(String[] args) 
	{   Scanner sc=new Scanner(System.in);
		int N=sc.nextInt();
        int T=sc.nextInt();
		
		System.out.println( champagneGlasses(N, T)); 
	} 
}

