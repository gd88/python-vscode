# include <stdio.h>
# include <stdlib.h>

int main()
{
    char str[10];
    scanf("%s", str);

    int l=strlen(str)/2;
    for(int i=0; i<=l-1; i++)
    {
        if(str[i]!=str[strlen(str)-i-1])
        {
            printf("This is not a palindrome");
            return 0;
        }
    }
    printf("This is a palindrome");
    return 0;
}