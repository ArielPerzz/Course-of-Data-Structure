//Ariel Perez
#include <iostream>
using namespace std;
int suma_recursiva(int n) {
    if(n == 1) {
        return 1;
    } else {
        return n + suma_recursiva(n-1);
    }
}
int main() {
    int n;
    cout << "Ingresa un número: ";
    cin >> n;
    int resultado = suma_recursiva(n);
    cout << "La suma de los números enteros desde 1 hasta " << n << " es " << resultado << endl;
    return 0;
}7
