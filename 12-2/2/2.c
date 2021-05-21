# include <stdio.h>

typedef struct
{
    char name[7];
    int score;
} Person;

void printScoreStars(Person* persons, int len)
{  
    for (int i=0; i<len; i++)
        {char c[20]={0,};
            int m=((*(persons+i)).score)/5;
        for (int j=0; j<m; j++)
            c[j]='*';
        printf("%s ", (*(persons+i)).name);
        for (int j=0; j<m; j++)
            printf("%c", c[j]);
        printf("\n");
        }
}

int main()
{
    Person p[3];
    for (int i=0; i<3; i++)
        scanf("%s %d", &p[i].name, &p[i].score);
    printScoreStars(p, 3);
    
    return 0;
}