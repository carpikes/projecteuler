#include <sstream>
#include <iostream>
#include <NTL/ZZ.h>
#include <NTL/RR.h>

using std::cout;
using std::endl;
using namespace NTL;

int main() {
    int i;
    ZZ a,b,n;

    a = 0;
    b = 1;

    RR big = pow(to_RR(10), to_RR(1000));
    ZZ bbig = to_ZZ(big);

    i=1;
    std::string s="";
    while(s.length()<1000) {
        n = a+b;
        a = b;
        b = n;
        std::stringstream ss;
        ss << n;
        s = ss.str();
        i++;
    }

    cout << i << endl;
    return 0;    
}
