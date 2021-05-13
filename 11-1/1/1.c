# include <stdio.h>
# include <string.h>

int main()
{
    char a[10], b[10];
    scanf("%s %s", a, b);
    printf("str1: %s\n", a);
    printf("str2: %s\n", b);
    printf("length of str1: %d\n", strlen(a));
    printf("length of str2: %d\n", strlen(b));
    int c;
    c=strcmp(a,b);
    printf("str1+str2: %s\n", strcat(a, b));
    if (c==0)
    printf("same");
    else
    printf("not same");

    return 0;

}