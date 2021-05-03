# include<stdio.h>

void printLine(n)
{
    for(int i=1; i<=n; i++)
    {printf("%d ", i);}
    printf("\n");

}

int main()
{
    int n;
    scanf("%d", &n);
    for(int j=1; j<=n; j++)
    printLine(j);
    for(int j=1; j<=n; j++)
    printLine(n+1-j);
    return 0;
}