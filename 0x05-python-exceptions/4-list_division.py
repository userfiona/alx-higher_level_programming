#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        try:
            elem_1 = my_list_1[i]
            elem_2 = my_list_2[i]
            if not isinstance(elem_1, (int, float)) or not isinstance(elem_2, (int, float)):
                raise TypeError
            if elem_2 == 0:
                raise ZeroDivisionError
            result = elem_1 / elem_2
        except ZeroDivisionError:
            result = 0
            print("division by 0")
        except (TypeError, IndexError):
            result = 0
            print("wrong type or out of range")
        finally:
            new_list.append(result)
    return new_list
