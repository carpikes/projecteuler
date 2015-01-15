#include <iostream>
#include <sstream>
#include <NTL/RR.h>
#include <NTL/ZZ.h>

using namespace NTL;
using namespace std;

int GetSum(int num) {
    RR n;
    int i, sum;
    string s;
    stringstream sstr;

    n = sqrt(to_RR(num));

    sstr << n;
    s = sstr.str();
    if(s.find('.') != string::npos) 
        s[s.find('.')]='0';

    if(s.length()<900)
        return 0;

    sum = 0;
    for(i=0;i<101;++i) 
         sum += s[i]-'0';

    return sum;
}

int main(int argc, char **argv) {
    int i, m_sum = 0;

    RR::SetPrecision(1000);
    RR::SetOutputPrecision(1000);

    for(i=1;i<=100;i++)
        m_sum += GetSum(i);

    cout << m_sum << endl; 
    return 0;
}
