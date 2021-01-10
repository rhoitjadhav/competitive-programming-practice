#include <iostream>
using std::cout;
using std::endl;

int maxConsecutiveOnes(int a) 
{ 
 
    int cnt = 0; 
  
    
    
    while (a!=0) 
    { 
       
  
        a = (a & (a << 1)); 
  
        cnt++; 
    } 
  
    return cnt; 
} 
  
 
int main() 
{ 
    int data;
    data = maxConsecutiveOnes(15);
    cout << data; 
    return 0; 
}
