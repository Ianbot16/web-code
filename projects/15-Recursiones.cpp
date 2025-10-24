#include <iostream>
using namespace std;
 //Se va a llamar una función varias veces
 //Función prototipo
 int factorial(int);

int main(){
    setlocale(LC_ALL,"");
    int n,resultado;
    cout<<"Ingrese un número: ";
    cin>>n;

    resultado=factorial(n);
    cout<<"El factorial de " <<n<<" es: "<<resultado<<endl;

    return 0;
}

 int factorial(int n){
    if (n>1){
        return n*factorial(n-1);
    }
    else{
        return 1;
    }
 }