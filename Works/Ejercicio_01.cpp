#include <iostream>
#include <string>
using namespace std;

int main() {
    string nombre;
    double n1,n2,total;
    cout << "Hello, World!" << endl;
    cout << 3 << endl;
    cout << 3.5 << endl;
    cout << 3 + 3.5 << endl;
    cout << 3 - 3.5 << endl;
    cout << 3 * 3.5 << endl;
    cout << 3 / 3.5 << endl;
    cout << "Ingrese su nombre: ";
    cin >> nombre;
    //getline(cin, nombre);
    cout << "Hola " << nombre << endl;
    cout << "Ingrese un numero: ";
    cin >> n1;
    cout << "Ingrese otro numero: ";
    cin >> n2;
    total = n1 + n2;
    cout << "El total es: " << total << endl;
    return 0;
}