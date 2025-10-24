#include <iostream>
#include <string>
using namespace std;
//Metodo por encapsulamiento
class Empleado{
    private:
     string empleado;
     
    public:
     void setempleado(string e){
        empleado=e;
     }
     
     string getempleado(){
        return empleado;
     }
}; 

int main(){
    Empleado nomina;
    nomina.setempleado("Carlos");
    cout<<nomina.getempleado();
    return 0;
}