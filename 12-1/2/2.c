# include <stdio.h>

struct person
{
    char name[10];
    int age;
};

int main()
{
    struct person p1;
    scanf("%s %d", &p1.name, &p1.age);
    printf("name: %s\nage: %d", p1.name, p1.age);
    return 0;

}