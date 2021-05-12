# include <stdio.h>

int main()
{
    double a[5];
    scanf("%lf %lf %lf %lf %lf", &a[0], &a[1], &a[2], &a[3], &a[4]);
    double* parr=&a[0];
    *parr=*(parr)*2;
    *(parr+1)=*(parr+1)*2;
    *(parr+2)=*(parr+2)*2;
    *(parr+3)=*(parr+3)*2;
    *(parr+4)=*(parr+4)*2;

    double sum=0;
    for (int i=0; i<=4; i++)
    sum=sum+*(parr+i);

    printf("%f\n", *parr);
    printf("%f\n", *(parr+1));
    printf("%f\n", *(parr+2));
    printf("%f\n", *(parr+3));
    printf("%f\n", *(parr+4));
    printf("sum: %f", sum);

    return 0;

}