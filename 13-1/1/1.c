# include <Stdio.h>

const double PI=3.141592;

int main()
{
    double r;
    scanf("%lf", &r);
    printf("Perimeter: %f\n", 2*PI*r);
    printf("Area: %f", PI*r*r);
    return 0;

}