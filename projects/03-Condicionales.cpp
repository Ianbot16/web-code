#include <iostream>
#include <cmath>
using namespace std;
int main(){
    //En un estacionamiento cobran $3,50 determine cuanto debe pagar un cliente por el estacionamiento de su vehiculo conociendo el tiempo de estacionamiento en horas y minutos
    //Crear condicionales
    int horas,minutos;
    double total;
    const double multa=3.50;
    
    cout<<"Ingrese la hora: ";
    cin>>horas;
    cout<<"Ingrese los minutos: ";
    cin>>minutos;
    horas=horas*60;

    if(horas>0){
        total=((horas+minutos)*multa)/60;
    }

    else{
        total=(minutos*multa)/60;
    }
    cout<<"El precio a pagar es: "<<total<<endl;

    
    return 0;
}