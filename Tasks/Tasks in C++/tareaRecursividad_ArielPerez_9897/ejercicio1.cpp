//Ariel Perez
#include <iostream>
using namespace std;
int f(int n){
  if (n == 0) {
    return 1;
  }else{
    //funcion de recurcion directa
    return n * f(n-1); 
  }
}
int main() 
{
  cout <<"ejercicio 1, calculo de un factorial"<< endl;
  int nu;
  cout << "Ingresa un número"<<endl;
  cin >> nu;
  cout << "el factorial de: "<< nu <<" es: " << f(nu)<<endl;
return 0;
}