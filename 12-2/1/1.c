# include<stdio.h>

void getSumDiff(int a, int b, int* pSum, int* pDiff)
{
    *pSum=a+b;
    *pDiff=a-b;
}

int main()
{
    int a; int b;
    scanf("%d %d", &a, &b);
    int sum; int diff;
    getSumDiff(a,b,&sum,&diff);
    printf("sum: %d \ndiff: %d", sum, diff);

    return 0;

}