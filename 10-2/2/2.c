# include <stdio.h>

int main()
{
    int a[5];
    scanf("%d %d %d %d %d", &a[0], &a[1], &a[2], &a[3], &a[4]);
    int* pa=a;
    int b=*a; int c=*(a+1);
    *(a)=*(a+4);
    *(a+1)=*(a+3);
    *(a+3)=c;
    *(a+4)=b;



   
    printf("%d %d %d %d %d", a[0], a[1], a[2], a[3], a[4]);
    return 0;

}