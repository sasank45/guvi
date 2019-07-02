#include<stdio.h>
int main()
{
    int n,i,count=0,rem;
    scanf("%d",&n);
    while(rem!=0)
    {
        rem = n/10;
        n = rem;
        count++;
    }
    printf("%d",count);
    return 0;
}   
