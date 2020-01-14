def count_element_in_list ():
    my_list = input('Type elements of the list: ').split(' ')
    element = input('Type element to find: ') 
    count_element = my_list.count(element) 
    return print(count_element)
count_element_in_list() 