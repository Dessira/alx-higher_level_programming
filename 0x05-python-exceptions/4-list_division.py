#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        try:
            value = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
            value = 0
            continue
        except TypeError:
            print("wrong type")
            value = 0
            continue
        except IndexError:
            print("out of range")
            value = 0
            continue
        finally:
            new_list += [value]
    return new_list
