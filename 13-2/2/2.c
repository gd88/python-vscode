# include <stdio.h>
# include <string.h>

int main()
{
    char str[10][20]={"",""};
    int j=0;
    for(int i=0; i<10; i++)
    {
        printf("Enter a word(Enter 'end' to quit): ");
        scanf("%s", str[j]);
        for(int m=0; m<j; m++)
        {
            if(strcmp(str[m],str[j])==0)
            {printf("This word already exists. Please enter another word.\n");
            j=j-1;}
        }
        if(strcmp(str[j], "end")==0)
        {
        printf("%d words in the list:\n", j);
        for(int n=0; n<j; n++)
        printf("%s ", str[n]);
        printf("\n");
        break;
        }

        j=j+1;
    }
    
    while(1)
    {
        int t=0;
        char arr[10]="";
        printf("Enter a word to search (Enter 'end' to quit): ");
        scanf("%s", arr);
        
        if(strcmp(arr,"end")==0)
        break;

        for(int i=0; i<j; i++)
        {if(strcmp(arr,str[i])==0)
        t=1;
        }
        if (t==1)
        printf("This word is in the list\n");
        else
        printf("This word is NOT in the list\n");


    }

    return 0;
}