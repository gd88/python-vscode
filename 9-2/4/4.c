# include<stdio.h>

int combination(int n, int r)
{
    if (n==r)
    return 1;
    else if (r==0)
    return 1;
    else 
    return combination(n-1,r-1)+combination(n-1,r);
}

int main()
{
    int a,b;
    scanf("%d %d", &a, &b);
    printf("%d", combination(a,b));

    return 0;

}