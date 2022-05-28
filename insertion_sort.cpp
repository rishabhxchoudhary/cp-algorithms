#include<iostream>
using namespace std;
int main(){
    int n=9;
    int a[]={1,3,2,5,4,6,8,10,7};

    // insertion sort
    for(int j=2;j<n;j++){
        int i=j-1;
        while(i>0 && a[i]>a[j]){
            a[i+1]=a[i];
            i--;
        }
        a[i+1]=a[j];
    }
    for(int i=0;i<n;i++){
        cout<<a[i]<<" ";
    }
    cout<<endl;
}
