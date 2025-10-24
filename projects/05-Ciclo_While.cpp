#include <iostream>
#include <iomanip>
using namespace std;
int main(){
    setlocale(LC_ALL,"");
    //Tabla de multiplicar
    int n,c=1,limite;
    cout<<"Ingrese un número: ";
    cin>>n;
    cout<<"Ingrese un límite: ";
    cin>>limite;

    while (c<=limite)
    {
        cout<<n<<" x "<<setw(2)<<c<<" = "<<n*c<<endl;
        c++;
    }

    //Suma
    //int numero;
    //int suma=0;
    //cout<<"Ingrese un número: ";
    //cin>>numero;
    //while (numero>=0)
    //{
        //suma+=numero;
        //cout<<"Ingrese más números: ";
        //cin>>numero;
    //}
    //cout<<"La suma total es: "<<suma;
    
    
    return 0;
}