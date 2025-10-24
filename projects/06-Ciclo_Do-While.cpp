#include <iostream>
using namespace std;
int main(){
    setlocale(LC_ALL,"");
    //Ver cuantos digitos tiene el numero
    int numero,i=0;
    cout<<"Ingrese un número para ver cuantos digitos tiene: ";
    cin>>numero;
    do
    {
        numero=numero/10;
        i++;
    } while (numero!=0);
    cout<<"La cantidad de digitos es: "<<i<<endl;

    return 0;
}
