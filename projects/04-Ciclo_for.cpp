#include <iostream>
using namespace std;
int main(){
    setlocale(LC_ALL,"");
    int numero, i=0;
    cout<<"Ingrese un n�mero: ";
    cin>>numero;
    for (int x = 1; x <= numero; x++)
    {
        if (numero % x ==0){
            i++;
        }

    }
    if (i==2)
    {
        cout<<"N�mero primo";
    }
    else{
        cout<<"No es n�mero primo";
    }
    
    
    
    return 0;
}