def split_and_print_list():
   
    user_input = input("Enter a list of numbers: ")
    input_list = list(map(int, user_input.split()))  
    
    # Введення порядкового номера для розбиття
    split_index = int(input("Enter the index to split the list (starting from 1): ")) - 1  # Зміщення до індексу Python (з 0)
    
    # Перевірка правильності введеного індексу
    if split_index < 0 or split_index >= len(input_list):
        print("Invalid index for splitting the list!")
        return
    
   
    list1 = input_list[:split_index]
    list2 = input_list[split_index:]
    
    
    print("First list:", list1)
    print("Second list:", list2)


split_and_print_list()
