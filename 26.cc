#include <NTL/RR.h>
#include <iostream>
#include <sstream>
#include <vector>

using namespace std;
using namespace NTL;

int getRecLen(int n) {
    RR num = to_RR(1.0)/to_RR(n);
    stringstream ss;

    ss << num;
    string k = ss.str();
  
    if(k.length() < 50)
        return 0;

    int maxr = 0;
    for(int i=5000;i>0;i--) {
        string sub = k.substr(100, i);
        string sub2 = k.substr(100+i, i);
        if(sub == sub2)
            maxr = i;
    }

    return maxr;
}

int main() {
    RR::SetPrecision(10000);
    RR::SetOutputPrecision(10000);

    int mr = 0;
    int md = 0;
    for(int i=1;i<1000;i++) {
        int rec = getRecLen(i);
        if(rec>mr) {
            mr = rec;
            md = i;
        }
        cout << i << ":" << rec << endl;
    }

    cout << md << ":" << mr << endl;
    return 0;
}
