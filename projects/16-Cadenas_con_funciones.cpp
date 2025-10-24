#include <iostream>
#include <cstring>
using namespace std;

int main(){
    char real_madrid[]="Cristiano Ronaldo";
    char juventus[20];
    char comida_uno[]="Papas";
    char comida_dos[]=" Fritas";
    char colores[]="Amarillo";
    char pinturas[]="Naranja";
    //Se devuelve la longitud de las cadenas que le paso como argumento
    cout<<strlen(comida_uno)<<endl;
    //Se va a copiar la cadenas
    strcpy(juventus,real_madrid);
    cout<<juventus<<endl;
    //Se concatenaran cadenas
    cout<<strcat(comida_uno,comida_dos)<<endl;
    //Se utiliza para comparar cadenas
    //Si char a == char b = 0
    //Si char a > char b = -1
    //Si char a < char b = 1
    cout<<strcmp(colores,pinturas)<<endl;
    return 0;
}