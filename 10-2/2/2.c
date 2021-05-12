# include <stdio.h>

int main()
{
    int a[5];
    scanf("%d %d %d %d %d", &a[0], &a[1], &a[2], &a[3], &a[4]);
    int* pa=a;
    int b=*pa; int c=*(pa+1);
    *(pa)=*(pa+4);
    *(pa+1)=*(pa+3);
    *(pa+3)=c;
    *(pa+4)=b;



   
    printf("%d %d %d %d %d", *pa, *(pa+1), *(pa+2), *(pa+3), *(pa+4));
    return 0;

}