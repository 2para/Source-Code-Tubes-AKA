#include "tubes.h"

void insertion(int arr[], int n) {
    int i, key, j;
    for (i=2; i<=n;i++) {
        key = arr[i];
        j = i - 1;
        while (j>=0 && key < arr[j]) {
            arr[j+1] = arr[j];
            j = j - 1;
        }
        arr[j+1] = key;
    }
}

void print(int arr[], int size) {
    int i;
    for (i=0;i<size;i++) {
        cout<<arr[i]<<" ";
    }
    cout<<endl;
}

void swap(int* a, int* b) {
    int t = *a;
    *a = *b;
    *b = t;
}

int partition (int arr[], int low, int high) {
    int pivot = arr[high];
    int i = (low - 1);

    for (int j = low; j <= high- 1; j++) {
        if (arr[j] <= pivot) {
            i++;
            swap(&arr[i], &arr[j]);
        }
    }
    swap(&arr[i + 1], &arr[high]);
    return (i + 1);
}

void quickSort(int arr[], int low, int high) {
    if (low < high) {
        int pi = partition(arr, low, high);
        quickSort(arr, low, pi - 1);
        quickSort(arr, pi + 1, high);
    }
}

void printArray(int arr[], int size) {
    int i;
    for (i=0; i < size; i++) {
        cout<<("%d ", arr[i])<<" ";
    }
    cout<<("\n");
}
