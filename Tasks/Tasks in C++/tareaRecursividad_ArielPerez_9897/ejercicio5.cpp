//Ariel Perez
#include <iostream>
using namespace std;
const int n = 3;
void print(int arr[n][n], int i, int j) {
    if (i == n) {
        return;
    }
    if (j == n) {
        cout << endl;
        print(arr, i + 1, 0);
        return;
    }
    cout << arr[i][j] << " ";
    print(arr, i, j + 1);
}

int main() {
    int arr[n][n] = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
    print(arr, 0, 0);
    return 0;
}
