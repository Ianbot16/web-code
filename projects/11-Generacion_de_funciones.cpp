#include<iostream>
using namespace std;
//Funci�n prototipo
int suma(int,int);

int main(){
    setlocale(LC_ALL,"");
    int s;
    s=suma(10,7);
    cout<<"La suma es: "<<s<<endl;
    return 0;
}

//Definir funciones
int suma(int a,int b){
    return(a+b);
}