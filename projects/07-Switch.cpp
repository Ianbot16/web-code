#include <iostream>
using namespace std;
int main(){
    setlocale(LC_ALL,"");
    //Calculadora
    char operador;
    int n1, n2;
    cout<<"Elija una operación:\n + - * /"<<endl;
    cin>>operador;
    cout<<"Ingrese el primer número: ";
    cin>>n1;
    cout<<"Ingrese el segundo número: ";
    cin>>n2;
    switch (operador)
    {
    case '+':
        cout<<n1<<" + "<<n2<<" = "<<n1+n2;
        break;
    
    case '-':
        cout<<n1<<" - "<<n2<<" = "<<n1-n2;
        break;
    
    case '*':
        cout<<n1<<" * "<<n2<<" = "<<n1*n2;
        break;
    
    case '/':
        cout<<n1<<" / "<<n2<<" = "<<(float)n1/(float)n2;
        break;

    default:
    cout<<"Error, operador incorrecto....";
        break;
    }

    return 0;
}