# include<stdio.h>

int main()
{
    int a;
    scanf("%d", &a);
    for(int b=0; b<a; b++)
    {
        for (int c=0; c<=b; c++)
        {
            printf("*");
        }
    printf("\n");
    }
    return 0;
}