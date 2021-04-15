# include<stdio.h>

int main ()
{
    int num;
    scanf("%d",&num);

    if(num < -10)
    {
        printf("n<-10");
    }
    else if(-10<=num && num<0)
    {
        printf("-10 <= n < 0");
    }
    else if(0 <= num && num<10)
    {
        printf("0 <= n < 10");
    }
    else if( num >= 10)
    {
        printf("n >= 10");
    }
    return 0;
}