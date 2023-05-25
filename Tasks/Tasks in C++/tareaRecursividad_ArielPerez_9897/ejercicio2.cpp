//Ariel Perez
#include <iostream>
using namespace std;

int fibonacci(int f){
    if (f == 1 || f == 2){
        return 1;
    }
    //recursividad directa
    return fibonacci(f-1) + fibonacci(f-2);
}
int main(){
    int n;
    int serie[]={1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765};
    cout << "los primeros 20 coeficientes de la serie de fibonacci son: " <<endl;
      for(int i = 0; i < 20; i++) {
      cout << serie[i] <<endl;
    }
    cout<<"ingrese el numero de la fila que desea obtener la suma"<< endl;
    cin>>n;
    cout<<"el valor de la suma de la fila " << n << " es "<< fibonacci(n) << endl;

}

