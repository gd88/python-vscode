# include <stdio.h>

int main()
{
    int arr[5];
    scanf("%d %d %d %d %d", &arr[0], &arr[1], &arr[2], &arr[3], &arr[4]);

    int max=arr[0];
    for (int i=1; i<=4; i++)
    {
        if(max<arr[i])
        max=arr[i];
    }
     int min=arr[0];
    for (int i=1; i<=4; i++)
    {
        if(min>arr[i])
        min=arr[i];
    }
    int sum=0;
    for(int i=0; i<=4; i++)
    {sum=sum+arr[i];}

    printf("min: %d\n", min); printf("max: %d\n", max); printf("sum: %d\n", sum);
    return 0;

}