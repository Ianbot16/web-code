#include <iostream>
#include <iomanip>
using namespace std;
int main(){
    setlocale(LC_ALL,"");
    //Tabla de multiplicar
    int n,c=1,limite;
    cout<<"Ingrese un n�mero: ";
    cin>>n;
    cout<<"Ingrese un l�mite: ";
    cin>>limite;

    while (c<=limite)
    {
        cout<<n<<" x "<<setw(2)<<c<<" = "<<n*c<<endl;
        c++;
    }

    //Suma
    //int numero;
    //int suma=0;
    //cout<<"Ingrese un n�mero: ";
    //cin>>numero;
    //while (numero>=0)
    //{
        //suma+=numero;
        //cout<<"Ingrese m�s n�meros: ";
        //cin>>numero;
    //}
    //cout<<"La suma total es: "<<suma;
    
    
    return 0;
}