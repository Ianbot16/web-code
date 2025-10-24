#include<iostream>
#include<cmath>
using namespace std;
int main(){
    setlocale(LC_ALL,"");
    double n1,n2,total;
    int opcion;
    do
    {
        cout<<"Calculadora"<<endl;
        cout<<"1) Suma de operaciones"<<endl;
        cout<<"2) Resta de operaciones"<<endl;
        cout<<"3) Multiplicación de operaciones"<<endl;
        cout<<"4) División de operaciones"<<endl;
        cout<<"5) Salir"<<endl;
        cout<<"Elija una opción: ";
        cin>>opcion;

        switch (opcion)
        {
        case 1:
            cout<<"Ingrese dos números para sumar"<<endl;
            cout<<"Ingrese el primer número: ";
            cin>>n1;
            cout<<"Ingrese el segundo número: ";
            cin>>n2;
            total=n1+n2;
            cout<<"El resultado es: "<<total<<endl;
            break;

        case 2:
            cout<<"Ingrese dos números para restar"<<endl;
            cout<<"Ingrese el primer número: ";
            cin>>n1;
            cout<<"Ingrese el segundo número: ";
            cin>>n2;
            total=n1-n2;
            cout<<"El resultado es: "<<total<<endl;
            break;

        case 3:
            cout<<"Ingrese dos números para multiplicar"<<endl;
            cout<<"Ingrese el primer número: ";
            cin>>n1;
            cout<<"Ingrese el segundo número: ";
            cin>>n2;
            total=n1*n2;
            cout<<"El resultado es: "<<total<<endl;
            break;

        case 4:
            cout<<"Ingrese dos números para dividir"<<endl;
            cout<<"Ingrese el primer número: ";
            cin>>n1;
            cout<<"Ingrese el segundo número: ";
            cin>>n2;
            total=n1/n2;
            cout<<"El resultado es: "<<total<<endl;
            break;
        
        case 5:
            cout<<"Saliendo del sistema"<<endl;
            break;

        default:
            cout<<"Número incorrecto, intente otro número"<<endl;
            break;
        }
    } while (opcion!=5);
    return 0;
}