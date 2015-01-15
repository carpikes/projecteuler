#include <iostream>

using std::cout;
using std::endl;

int dmap[] = { 
    17, 28, 7, 4,
    9, 6, 11, 8,
    5, 10, 7, 12
};

int sundays(int y) {
    int i, sundays = 0;

    int q1 = y / 12;
    int r1 = y % 12;

    int offset = 7 + q1 + r1 + r1/4;

    if(!(y%4)) {
        dmap[1]=29;
        dmap[0]=18;
    } else {
        dmap[1]=28;
        dmap[0]=17;
    }

    offset %= 7;

    for(i=0;i<12;i++)
        if((70+offset-dmap[i])%7==5) 
            sundays++; 
    return sundays;
}

int main(int argc, char **argv) {
    int y, sum = 0;

    for(y=1;y<=100;y++)
        sum += sundays(y);

    cout << sum << endl;
    return 0;
}
