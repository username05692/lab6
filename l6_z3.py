def add_vowels_to_set():
    a = {'c', 'd'}
    b = {'a', 'e', 'i', 'o', 'u', 'y'}

    print("A:", a)
    print("B:", b)

    result_set = a | b
    
    print("Result after addition:",result_set)

add_vowels_to_set()
