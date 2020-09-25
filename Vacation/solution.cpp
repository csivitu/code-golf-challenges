#include<bits/stdc++.h>
using namespace std;

int ans(vector<int> v){
    int counter=0,max=-1;
    for(auto i=v.begin();i!=v.end();i++){
        counter=0;
        for(auto j=i;j!=v.end();j++){
            if(*j==0){
                counter++;
            }
            if(counter>max)max=counter;
            if(*j==1){
                break;
            }
        }
    }
    return max;
}   
    int main(){
        ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int k;
    cin>>k;
    while(k--){
        int n,counter=0;
        cin>>n;
        vector<int> v;
        int arr[5];
        for(int i=0;i<5;i++){cin>>arr[i];
        v.push_back(arr[i]);
        }
        int x=1;
        int nn=n;
        if(n>5){
            for(int i=0;i<4;i++){
                
                if(x%2!=0){
                    arr[0]=arr[0]==1?0:1;
                    arr[2]=arr[2]==1?0:1;
                    arr[4]=arr[4]==1?0:1;
                    x++;
                    for(int i=0;i<5;i++)v.push_back(arr[i]);
                    
                }
                else if(x%2==0){
                    arr[1]=arr[1]==1?0:1;
                    arr[3]=arr[3]==1?0:1;
                    x++;
                    for(int i=0;i<5;i++)v.push_back(arr[i]);
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
                    for(int i=0;i<5;i++)v.push_back(arr[i]);
                }
                
                
                if(x%2==0){
                    arr[1]=arr[1]==1?0:1;
                    arr[3]=arr[3]==1?0:1;
                    x++;
                    for(int i=0;i<5;i++)v.push_back(arr[i]);
                }
            }
        }
        cout<<ans(v);
        v.clear();
    }
        return 0;
}

