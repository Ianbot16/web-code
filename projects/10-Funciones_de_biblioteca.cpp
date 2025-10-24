#include <iostream>
#include <cmath>
using namespace std;
int main(){
    setlocale(LC_ALL,"");
    //La raiz cuadrada de un número
    double n,raiz_cuadrada;
    cout<<"Ingrese un número: ";
    cin>>n;
    raiz_cuadrada=sqrt(n);
    cout<<"La raiz cuadrada de "<<n<<" es: "<<raiz_cuadrada;

    return 0;
}