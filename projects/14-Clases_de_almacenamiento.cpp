#include<iostream>
using namespace std;

 //Varialble global del programa
 int numero_global=9;

 void ejemplo();

int main(){
    setlocale(LC_ALL,"");
    //Variable local de main
    int numero=100;
    cout<<numero<<endl;
    cout<<numero_global<<endl;
    ejemplo();
    ejemplo();
    return 0;
}

 void ejemplo(){
    //Variable local de ejemplo
    int numero_dos=200;
    //Variable estatica de ejemplo
    static int numero_static=700;
    numero_static++;
    cout<<numero_dos<<endl;
    cout<<numero_global<<endl;
    cout<<numero_static<<endl;


 }