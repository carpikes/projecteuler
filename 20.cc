#include <cstring>
#include <iostream>

char str[] = "93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000";

int main() {
    int sum = 0;
    for(int i=0;i<strlen(str);i++)
        sum += str[i]-'0';
    std::cout << sum << std::endl;
    return 0;
}
