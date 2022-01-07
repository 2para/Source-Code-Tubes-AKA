#include "tubes.h"

int main()
{
    /*int arr[] = {7,4,3,7,9,7,5,9,7,2};
    int n = sizeof(arr)/sizeof(arr[0]);
    insertion(arr, n);
    cout<<"Hasil Insertion Sort: ";
    print(arr, n);*/

    int arr[] = {7,4,3,7,9,7,5,9,7,2};
    int n = sizeof(arr)/sizeof(arr[0]);
    quickSort(arr, 0, n-1);
    printf("Hasil Quick Sort: ");
    printArray(arr, n);
}
