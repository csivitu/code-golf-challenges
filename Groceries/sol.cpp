
#include <bits/stdc++.h> 
using namespace std; 
  
bool Check(int arr1[], int arr2[], int m, int n) 
{ 
    int i = 0, j = 0; 
      
    if (m < n) 
    return 0; 
    sort(arr1, arr1 + m); 
    sort(arr2, arr2 + n);  
        
    while (i < n && j < m ) 
    {  
        if( arr1[j] <arr2[i] ) 
            j++;  
        else if( arr1[j] == arr2[i] ) 
        { 
            j++; 
            i++; 
        } 
        else if( arr1[j] > arr2[i] ) 
            return 0; 
    } 
   
    return  (i < n)? false : true; 
}  
  
int main() 
{ 
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int k;
    cin>>k;
    while(k--){
        int n,m;
        cin>>n>>m;
        int arr1[n],arr2[m];
        for(int i=0;i<n;i++)cin>>arr1[i];
        for(int i=0;i<m;i++)cin>>arr2[i];
        if(Check(arr1, arr2, n, m)) cout<<"YES"<<endl;
        else cout<<"NO"<<endl;       
  
    } 
    
    return 0; 
}