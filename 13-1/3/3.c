# include <stdio.h>

void printString(const char*str)
{
    printf("%s\n",str);
}



int main()
{
    char* arr[3]={"One", "Two", "Three"};
    void (*fptr)(const char*);
    fptr=printString;
    fptr(arr[0]); fptr(arr[1]); fptr(arr[2]);
    return 0;

}