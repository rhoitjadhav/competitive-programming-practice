#include<stdio.h>

int main(){
    int mex = 0;

    int arr[4] = {0, 0, 1, 2};

    for(int i=0; i<sizeof(arr); i++) {
        if(mex == arr[i]) {
            mex++;
        }
    }
    printf("%d", mex);
    
    return 0;
}
