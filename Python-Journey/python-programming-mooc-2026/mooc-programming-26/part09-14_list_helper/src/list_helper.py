# WRITE YOUR SOLUTION HERE:
class ListHelper:

    @classmethod
    def greatest_frequency(cls,my_list: list):
        if not my_list:
            return None

        frequency_dict = {}
        for item in my_list:
            frequency_dict[item] = my_list.count(item)
        return max(frequency_dict,key=frequency_dict.get)

    @classmethod
    def doubles(cls,my_list: list):
        unique_two = []
        for item in my_list:
            if my_list.count(item)>=2 and item not in unique_two:
                unique_two.append(item)
        return len(unique_two)

if __name__ == "__main__":
    numbers = [1, 1, 2, 1, 3, 3, 4, 5, 5, 5, 6, 5, 5, 5]
    print(ListHelper.greatest_frequency(numbers))
    print(ListHelper.doubles(numbers))