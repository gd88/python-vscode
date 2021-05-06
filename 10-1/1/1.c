# include <stdio.h>

int main()
{
    int i;
    scanf("%d", &i);

    int* pi=&i;
    printf("%d\n", *pi);

    *pi+=10;
    printf("%d", *pi);

    return 0;

}