#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result_list = []

    for elements in range(0, list_length):
        try:
            div = my_list_1[elements] / my_list_2[elements]
        except TypeError as e:
            print("wrong type".format())
            div = 0
        except ZeroDivisionError as e:
            print("division by 0".format())
            div = 0
        except IndexError as e:
            print("out of range".format())
            div = 0
        finally:
            result_list.append(div)
    return (result_list)
