#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result_list = []

    for elements in range(list_length):
        try:
            result_list.append(my_list_1[elements] / my_list_2[elements])
        except TypeError as e:
            print("wrong type")
            result_list.append(0)
            pass
        except ZeroDivisionError as e:
            print("division by 0")
            result_list.append(0)
            pass
        except IndexError as e:
            print("out of range")
            result_list.append(0)
            pass
    return (result_list)
