# include <stdio.h>

void square(double* pdvar)
{
    *pdvar=(*pdvar)*(*pdvar);
}

int main()
{
    double dvar;
    scanf("%lf", &dvar);
    square(&dvar);
    printf("%f", dvar);

    return 0;

}