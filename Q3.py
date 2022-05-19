def find_highest_value_index(n_list:list) -> int:
    if len(n_list) < 1:
        raise Exception("Length of the input list must be more than 0")
    max_index = 0
    max_n = n_list[0]-1
    for i,n in enumerate(n_list):
        if n > max_n:
            max_index = i
            max_n = n
    return max_index

if __name__ == "__main__":
    print("please input a list to find index of the highest value (ex. '5 7 3 8 6 4')")
    n_list = input().split(" ")
    n_list = [int(n) for n in n_list if n is not ""]
    print(find_highest_value_index(n_list))