# include <Stdio.h>

int main()
{
    int arr[3][2];
    
    for (int row=0; row<3; row++)
    {
        for(int col=0; col<2; col++)
        {
            scanf("%d", &arr[row][col]);
        }
    }
    for (int row=0; row<3; row++)
    {
        for(int col=0; col<2; col++)
        {
            printf("%d ", arr[row][col]);
        }
        printf("\n");
    }
    return 0;
}