# include<stdio.h>

int add(int a, int b)
{
    return a+b;
}

int sub (int a, int b)
{
    return a-b;
}

int mul (int a, int b)
{
    return a*b;
}

double div (double a, double b)
{
    return a/b;
}

int mod (int a, int b)
{
    return a%b;
}

void printMsg()
{
    printf("completed");
}

int main(int num1, int num2)
{
    scanf("%d", &num1);
    scanf("%d", &num2);
    printf("sum: %d\n", add(num1, num2));
    printf("difference: %d\n", sub(num1, num2));
    printf("product: %d\n", mul(num1, num2));
    printf("division: %f\n", div(num1, num2));
    printf("remainder: %d\n",mod(num1, num2));
    printMsg();

    return 0;
}