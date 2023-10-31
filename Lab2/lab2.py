def display_main_menu():
    print("Enter some numbers separated by commas(e.g. 5,67,32)")


def get_user_input():
    lists = input()
    lists = list(lists.split(","))
    return lists

def calc_average_temperature(num_list):
    y = 0
    for x in num_list:
        y = float(x) + float(y)
    average = y / len(num_list)
    return average

def calc_min_max_temperature(num_list):
    firstloop =0
    for x in num_list:
        if firstloop == 0:
            max = x
            min = x
            firstloop = 1
        if float(x) > float(max):
            max = x
        if float(x) < float(min):
            min = x
    list_min_max = [min,max]
    return list_min_max

def calc_median_temperature(num_list):
    num_list.sort()
    length = len(num_list)
    x = length % 2
    y = float(length) / 2
    if x == 0:
        median = (int(num_list[int(y)]) + int(num_list[int(y)-1])) / 2
    else:
        median = num_list[int(y)]
    return median


def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()
    print(calc_average_temperature(num_list))
    print(calc_min_max_temperature(num_list))
    print(calc_median_temperature(num_list))

if __name__ == "__main__":
    main()
