#include <iostream>
#include <cmath>
using namespace std;
int main(){
    setlocale(LC_ALL,"");
    //La raiz cuadrada de un n�mero
    double n,raiz_cuadrada;
    cout<<"Ingrese un n�mero: ";
    cin>>n;
    raiz_cuadrada=sqrt(n);
    cout<<"La raiz cuadrada de "<<n<<" es: "<<raiz_cuadrada;

    return 0;
}