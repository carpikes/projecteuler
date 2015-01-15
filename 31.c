#include <stdio.h>

int arr[] = { 200, 100, 50, 20, 10, 5, 2, 1 };
#define SZ sizeof(arr)/sizeof(int)

int solve(int max, int pos) {
    int sols = 0, i;

    if(max == 0) return 1;
    if(max < 0) return 0;

    for(i = pos; i<SZ;i++) 
        sols += solve(max - arr[i],i);
    
    return sols;
}

int main() {
    printf("%d\n", solve(200, 0));   
}
