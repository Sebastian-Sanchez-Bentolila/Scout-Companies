/* @Author: Sebastian Sanchez Bentolila
https://github.com/Sebastian-Sanchez-Bentolila */

//Modules
#include<iostream>
#include<stdlib.h>
using namespace std;

//Variables
char excel[21]="pip install openpyxl", matplotlib[23]= "pip install matplotlib";

void cmd(){
    system(excel);
    system(matplotlib);
}

int main(){
    cmd();
    cout<<"Intalacion finalizada. Puede cerrar la ventana\n";
    system("pause");
    return 0;
}
