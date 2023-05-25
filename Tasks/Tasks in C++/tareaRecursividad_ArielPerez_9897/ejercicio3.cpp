//Ariel Perez
#include <iostream>
#include <cmath>

using namespace std;
float taylor(float x, int n) {
    static float p = 1, f = 1;
    float result;
    if (n == 0) {
        return 1;
    }3
    result = taylor(x, n - 1);
    p = p*x;
    f = f*n;
    return result + p / f;
}
int main() {
    float x;
    int n;
    cout << "Ingrese el valor de x: ";
    cin >> x;
    cout << "Ingrese la cantidad de términos: ";
    cin >> n;
    float result = taylor(x, n);
    cout << "El resultado de la serie de Taylor de exp(" << x << ") es: " << result << endl;
    return 0;
}
