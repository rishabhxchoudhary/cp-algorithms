#include<iostream>
using namespace std;

int extended_euclid(int a, int b, int &x, int &y){
    if (b==0){
        x=1;y=0;return a;
    }
    int x1,y1;
    int g = extended_euclid(b,a%b,x1,y1);
    x = y1;
    y = x1 - (a/b)*y1;
    return g;
}

int main(){
    int a=5,b=3,x,y;
    int g = extended_euclid(a,b,x,y);
    cout<<g<<" "<<x<<" "<<y;
}
