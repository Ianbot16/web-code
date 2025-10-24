#include<iostream>
using namespace std;

//funcion prototipo
  int mul(int,int);
  float mul(float,int);
  float mul(float,float);
  
  int mul(int a, int b){
    return a*b;
  }

  float mul(double x, int y){
    return x*y;
  }

  float mul(double m, double n){
    return m*n;
  }

int main(){
    setlocale(LC_ALL,"");
    int f1=mul(3,3);
    float f2=mul(25.9,8);
    float f3=mul(32.8,5.2);
    cout<<"f1 es: "<<f1<<endl;
    cout<<"f2 es: "<<f2<<endl;
    cout<<"f3 es: "<<f3<<endl;

    return 0;
}