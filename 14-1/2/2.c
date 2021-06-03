# include <stdio.h>
# include <stdlib.h>

int main()
{
    int num;
    scanf("%d", &num);
    int*pi=(int*)malloc(num*sizeof(int));

    for(int i=0; i<num; i++)
    scanf("%d", &pi[i]);

    int min=pi[0];
    int max=pi[0];
    for(int i=1; i<num; i++)
    {
        if(min>pi[i])
        min=pi[i];
    }
    for(int i=1; i<num; i++)
    {
        if(max<pi[i])
        max=pi[i];
    }
    printf("min: %d\n", min);
    printf("max: %d", max);
    free(pi);
    return 0;
}