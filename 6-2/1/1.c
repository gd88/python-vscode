# include <stdio.h>

int main(void)
{
    int num = 0;
    int a;
    scanf("%d", &a);
    while (num<9)
    {
        num++;
        printf("%d*%d=%d\n", a, num, a*num);
    } 
    return 0;

}