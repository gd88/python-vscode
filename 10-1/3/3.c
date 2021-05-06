# include <stdio.h>

int main()
{
    char str[1000];
    scanf("%s", str);

    for (int i=0; i<1000; i++)
    {if (str[i]=='\0')
    {printf("%d", i);
    return 0;} 
    }
}