#include <iostream>
using namespace std;
int main(){
    setlocale(LC_ALL,"");
    //int n,suma=0;
    //while (true)
    //{
        //cout<<"Ingrese un número: ";
        //cin>>n;
        //if (n<0)
        //{
            //break;
        //}
        //suma+=n;
        
    //}
    //cout<<"El resultadoes: "<<suma;
    for (int i = 1; i <=10; i++)
    {
        if (i==6 || i==9)
        {
            continue;
        }
        cout<<i<<endl;
        
    }
    

    

    
    return 0;
}