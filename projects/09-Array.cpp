#include <iostream>
using namespace std;
int main(){
    setlocale(LC_ALL,"");
    //int array[10];
    //for (int i = 0; i < 10; i++)
    //{
        //cout<<"Posición: "<<i<<" : ";
        //cin>>array[i];
    //}
    //cout<<"Contenido de mi array: "<<endl;
    //for ( int i = 0; i < 10; i++)
    //{
      //  cout<<array[i]<<" ";
   // }
   
   char text[60];
   cout<<"Ingrese sus datos: ";
   cin.getline(text,60);
   cout<<"Datos ingresados: "<<text;
   return 0;
}