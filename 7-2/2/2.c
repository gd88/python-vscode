# include<stdio.h>

int main()
{
    while (1)
    {
        char a=0;
        char b=0;
        scanf("%c", &a);
        scanf("%c", &b);
        
        if (97<=a && a<=122)
        {
            a=a-32;
            printf("%c\n", a);
            
        }
        else if (65<=a && a<=90)
        {
            a=a+32;
            printf("%c\n", a);
           
        }
        else if (48<=a && a<=57)
        {
            printf("%c\n", a);
            
        }

        else
        {
           break;
        }
        
        
        
    }
    return 0;
}