//funciones
#include<iostream>
using namespace std;
 //funcion prototipo 
 int sum(int a, int b=20, int c=10);

int main(){
    setlocale(LC_ALL,"");
    cout<<sum(1,2,3);
    return 0;
}

 int sum(int a, int b, int c){
    int resultado;
    resultado = a+b+c;
    return resultado;
 }