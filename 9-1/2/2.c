# include<stdio.h>

int gMul=1;

int addTotal(int a)
{
    int sum=0;
    for(int i=1; i<a+1; i++)
        sum+=i;
    return sum;
}

void mulTotal(int a)
{
    for(int i=1; i<a+1; i++)
        gMul*=i;
    printf("gMul: %d", gMul);
}



int main()
{
    int num;
    scanf("%d", &num);
    printf("addTotal(): %d\n", addTotal(num));
    mulTotal(num);

    return 0;
}