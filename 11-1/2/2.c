# include <Stdio.h>
# include <string.h>
# include <ctype.h>
int main()
{
    char a[10];
    scanf("%s", a);
    if (a[0]>90)
    {for(int i=0; i<=strlen(a); i++)
    printf("%c", toupper(*(a+i)));}
    if (a[0]<=90)
    {for(int i=0; i<=strlen(a); i++)
    printf("%c", tolower(*(a+i)));}

  
    return 0;

}