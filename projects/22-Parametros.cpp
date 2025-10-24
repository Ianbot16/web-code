#include <iostream>
#include <string>
using namespace std;
void myfunction(string fname){
    cout<<fname<<" Refsname \n";
}

int main(){
    myfunction("Christian");
    myfunction("Carlos");
    myfunction("Carla");
    return 0;
}