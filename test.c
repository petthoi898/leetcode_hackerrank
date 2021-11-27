#include <iostream>
int main(){
    int c = 3;
    int a = c*(c = 5);
    print("%d", a);
}