#include <iostream>
using namespace std;
 //Se va a llamar una funci�n varias veces
 //Funci�n prototipo
 int factorial(int);

int main(){
    setlocale(LC_ALL,"");
    int n,resultado;
    cout<<"Ingrese un n�mero: ";
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