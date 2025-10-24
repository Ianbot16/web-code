#include <iostream>
using namespace std;
int main(){
    //Matriz de 3 dimensiones
    //int a[3][3]={{1,2,3},{4,5,6},{7,8,9}};
    //cout<<a[1][1]<<endl;
    //for (int i = 0; i < 3; i++)
    //{
        //for (int j = 0; j < 3; j++)
        //{
            //cout<<"Datos de la matriz a: ["<<i<<"]["<<j<<"]: ";
            //cout<<a[i][j]<<endl;
        //}
        
    //}
    //Matriz multidimensional de dos dimensiones
    int a[2][2][2]={
        //Primera Matriz
        {{1,2},{3,4}},
        //Segunda Matriz
        {{5,6},{7,8}}
    };

    for (int i = 0; i < 2; i++)
    {
        for (int j = 0; j < 2; j++)
        {
            for (int k = 0; k < 2; k++)
            {
                cout<<"Datos de la matriz a: ["<<i<<"]["<<j<<"]["<<k<<"]: ";
                cout<<a[i][j][k]<<endl;
            }
            
        }
        
    }
    
    
    return 0;
}