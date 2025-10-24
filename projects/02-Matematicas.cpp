#include <iostream>
#include <cmath>
#include <ctime>
using namespace std;
int main()
{
    setlocale(LC_ALL,"");
    //Ecuaciones con números
    //Se crean las variables
    double a=7, b = 3,suma,resta,multiplicacion,division;
    double resultado_b=++b;
    time_t ahora=time(0);
    char* fecha=ctime(&ahora);
    int n1,n2,suma_personalizada;
    double area,base,altura;
    double notas_1,notas_2,notas_3,promedio_notas;
    float radio,volumen;
    const float pi=3.14159;
    
    //Se escriben los procesos
    suma=a+b;
    resta=a-b;
    multiplicacion=a*b;
    division=a/b;
    cout<<"Primer n�mero: "<<a<<endl;
    cout<<"Segundo numero: "<<b<<endl;
    cout<<"Suma de los numeros: "<<suma<<endl;
    cout<<"Resta de los numeros: "<<resta<<endl;
    cout<<"Multiplicacion de los numeros: "<<multiplicacion<<endl;
    cout<<"Division de los numeros: "<<division<<endl;
    cout<<"Ahora el segundo numero es: "<<resultado_b<<endl;
    printf("La fecha de hoy es: %s",fecha);
    cout<<"Ingrese un numero: ";
    //Se va a hacer una operacion con numeros ingresados
    cin>>n1;
    cout<<"Ingrese otro numero: ";
    cin>>n2;
    //El proceso de suma de un número debe de ser ubicado debajo de los input
    suma_personalizada = n1 + n2;
    cout<<"El resultado es: "<<suma_personalizada<<endl;
    cout<<endl;

    //Se ingresaran los datos para calcular el area de un triangulo
    cout<<"Calcular la base de un triangulo"<<endl;
    cout<<"Ingrese la base del triangulo: ";
    cin>>base;
    cout<<"Ingrese la altura del triangulo: ";
    cin>>altura;
    area=(base*altura)/2;
    cout<<"El area del triangulo es: "<<area<<endl;
    cout<<endl;

    //Se va a hacer promedio de notas
    cout<<"Se va a sacar promedio de notas"<<endl;
    cout<<"Ingrese la primera nota: ";
    cin>>notas_1;
    cout<<"Ingrese la segunda nota: ";
    cin>>notas_2;
    cout<<"Ingrese la tercera nota: ";
    cin>>notas_3;
    promedio_notas=(notas_1+notas_2+notas_3)/3;
    cout<<"El promedio de las notas es: "<<promedio_notas<<endl;
    cout<<endl;

    //Calcular el volumen de una esfera
    cout<<"Calcular el volumen de una esfera"<<endl;
    cout<<"Datos"<<endl;
    cout<<"Ingrese el radio de la esfera: ";
    cin>>radio;
    cout<<"Pi: "<<pi<<endl;
    volumen=(4*pi*pow(radio,3))/3;
    cout<<"El volumen de la esfera es: "<<volumen<<endl;
    
    return 0;
}

