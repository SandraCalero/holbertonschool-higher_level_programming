#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    i = 0
    result_list = []
    while i < list_length:
        try:
            element_result_list = my_list_1[i] / my_list_2[i]
        except TypeError:
            element_result_list = 0
            print("wrong type")
        except ZeroDivisionError:
            element_result_list = 0
            print("division by 0")
        except IndexError:
            element_result_list = 0
            print("out of range")
        finally:
            result_list.append(element_result_list)
            i += 1
    return result_list
