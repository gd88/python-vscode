#include<stdio.h>
#include<stdlib.h>
#include<string.h>

typedef struct
{
   char name[7];
   int score;
} Person;

void printScoreStars(Person* persons, int Len)
{
   for (int i = 0; i < Len; i++)
   {
      printf("%s\t", persons[i].name);
      for (int j = 0; j < (persons[i].score / 5); j++)
      {
         printf("*");
      }
      printf("\n");
   }
}

int main()
{
   int size = 0;
   Person *p = (Person*)malloc(sizeof(Person) * size);
   
   while (1) 
   {
      Person aperson;
      scanf("%s %d", aperson.name, &aperson.score);
    if ((strcmp(aperson.name, "END") == 0) && (aperson.score == 0))
      {
         break;
      }

      Person *temp = (Person*)malloc(sizeof(Person) * (size + 1));

      for (int i = 0; i < size; i++)
      {
         strcpy(temp[i].name, p[i].name);
         temp[i].score = p[i].score;
      }

      temp[size] = aperson;

      free(p);
      
      p = temp;
      
      size += 1;
   }

   printScoreStars(p, size);
   
   free(p);

   return 0;
}