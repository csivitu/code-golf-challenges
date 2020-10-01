#include<iostream>
using namespace std;
int main()
{
	ios_base::sync_with_stdio(false);
        cin.tie(NULL);
	int t;
	cin>>t;
	while(t--){
	    int n;
		cin>>n;
		int a[n],fl=0,j=0;
		for(int i=0;i<n;i++){
			int el;
			cin>>el;
			if(el==1){
				a[j]=i;	
				j++;	
			}
		}
		for(int i=j-1;i>0;i--)
		{
			if(a[i]-a[i-1]<6){
				fl=1;
				cout<<"NO\n";
				break;
			}
		}
		if(fl==0)
		cout<<"YES\n";
	}
	return 0;
}
