# include <stdio.h>

int main()
{
    int num;
    scanf("%d", &num);
    for (int a=1; a<10; a++)
    {
        printf("%d*%d=%d\n", num, a, num*a);
    }
    return 0;
}