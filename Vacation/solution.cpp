//every odd week, alternate positions (1,3,5) are reversed.
//every even week, alternate positions(2,4) are reversed.
//find longest subsequence of holidays 
//1 is attend 
//0 is bunk 

#include<bits/stdc++.h>
using namespace std;

int checker(int arr[], int n){
    int counter=0,max=-1;
    for(int i=0;i<n;i++){
        counter=0;
        for(int j=i;j<n;j++){
            
            if(arr[j]==0){
                counter++;
            }
            if(counter>max)max=counter;
            if(arr[j]==1){
                break;
            }
        }
    }
    return max;
}
    
    
    int main(){
    int k;
    cin>>k;
    while(k--){
        int n,counter=0;//number of weeks n
        cin>>n;
        int arr[5];
        for(int i=0;i<5;i++)cin>>arr[i];
        //after week 1 (1,3,5) are flipped 
        counter=checker(arr,5);
        int x=1;
        int nn=n;
        if(n>5){
            for(int i=0;i<4;i++){
                
                if(x%2!=0){
                    arr[0]=arr[0]==1?0:1;
                    arr[2]=arr[2]==1?0:1;
                    arr[4]=arr[4]==1?0:1;
                    x++;
                    if(checker(arr,5)>counter)counter=checker(arr,5);
                }
                else if(x%2==0){
                    arr[1]=arr[1]==1?0:1;
                    arr[3]=arr[3]==1?0:1;
                    x++;
                    if(checker(arr,5)>counter)counter=checker(arr,5);
                }
            }
        }
        else{
            while(nn--){
                int x=1;
                if(x%2!=0){
                    arr[0]=arr[0]==1?0:1;
                    arr[2]=arr[2]==1?0:1;
                    arr[4]=arr[4]==1?0:1;
                    x++;
                    if(checker(arr,5)>counter)counter=checker(arr,5);
                }
                
                
                if(x%2==0){
                    arr[1]=arr[1]==1?0:1;
                    arr[3]=arr[3]==1?0:1;
                    x++;
                    if(checker(arr,5)>counter)counter=checker(arr,5);
                }
            }
        }
        cout<<counter<<endl;
    }
        return 0;
}

