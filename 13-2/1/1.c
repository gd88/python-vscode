# include <stdio.h>

void printArray(char** arr, int len)
{
    printf("Array ");
    for(int i=0; i<len; i++)
    printf("[%d]:%s, ", i, arr[i]);
    printf("\n");
    char*temp=arr[0];
    arr[0]=arr[1];
    arr[1]=temp;
    printf("Array ");
    for(int i=0; i<len; i++)
    printf("[%d]:%s, ", i, arr[i]);
}

int main()
{
    char* str[2]={"aaa", "bbb"};
    printArray(str,2);
    return 0;
}