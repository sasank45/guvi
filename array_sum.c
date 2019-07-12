#include <stdio.h>
int main()
{
  int N,a[100],K,i,sum=0;
  scanf("%d",&N);
  scanf("%d",&K);
  for(i=0;i<N;i++){
      scanf("%d",&a[i]);
  }
  for(i=0;i<K;i++){
      sum=sum+a[i];
  }
     printf("%d",sum);
  return 0;
}
