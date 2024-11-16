def bubble_sort_and_print():
    A = list(map(int, input('Enter a list: ').split()))  

    # Реалізація алгоритму бульбашкового сортування
    n = len(A)
    for i in range(n - 1):  
        for j in range(n - i - 1):  
            if A[j] > A[j + 1]:  
                A[j], A[j + 1] = A[j + 1], A[j]

    print("Sorted list:", A)

bubble_sort_and_print()
