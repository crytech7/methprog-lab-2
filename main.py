#  =====================================================================================================
# 	 ﾞ☆ﾞ            ﾞ☆ﾞ            ﾞ☆ﾞ            ﾞ☆ﾞ            ﾞ☆ﾞ            ﾞ☆ﾞ
#   ／|、         ﾞ☆ﾞ            ﾞ☆ﾞ            ﾞ☆ﾞ            ﾞ☆ﾞ            ﾞ☆ﾞ            ﾞ☆ﾞ
# （ﾟ､ ｡ つ               ﾞ☆ﾞ             ﾞ☆ﾞ               ﾞ☆ﾞ            ﾞ☆ﾞ              ﾞ☆ﾞ              ﾞ☆ﾞ
#  |、ﾞ  ヽ        ﾞ☆ﾞ            ﾞ☆ﾞ            ﾞ☆ﾞ            ﾞ☆ﾞ            ﾞ☆ﾞ            ﾞ☆ﾞ
#  じーし__ )つ            ﾞ☆ﾞ            ﾞ☆ﾞ            ﾞ☆ﾞ            ﾞ☆ﾞ            ﾞ☆ﾞ            ﾞ☆ﾞ
#  =====================================================================================================
#  МЕТОДЫ ПРОГРАММИРОВАНИЯ | LAB 2 10.03.2023 | ВАРИАНТ 12
#  by crytech7
#  =====================================================================================================
#  > ВАРИАНТ 12:
# 	Массив данных о командах, принимающих участие в  чемпионате страны по футболу:
# 	страна, название клуба,  город, год, ФИО главного тренера
# 	(сравнение по полям – год, страна, количество набранных очков (по убыванию), название клуба):

#       Country,Club Name,City,Year,Coach Name,Points
#  ====================================================================================================
import sys, time


sys.setrecursionlimit(500000000)


class Object:
    def __init__(self, Country, Club_Name, City, Year, Coach_Name, Points):

        self.Country = Country
        self.Club_Name = Club_Name
        self.City = City
        self.Year = Year
        self.Coach_Name = Coach_Name
        self.Points = Points

    def __gt__(self, other):
        """operator > overloading"""

        if self.Year > other.Year:
            return True
        elif self.Year < other.Year:
            return False
        elif self.Year == other.Year:
            if self.Country > other.Country:
                return True
            elif self.Country < other.Country:
                return False
            elif self.Country == other.Country:
                if self.Points > other.Points:
                    return True
                elif self.Points < other.Points:
                    return False
                elif self.Points == other.Points:
                    if self.Club_Name > other.Club_Name:
                        return True
                    elif self.Club_Name < other.Club_Name:
                        return False
                    elif self.Club_Name == other.Club_Name:
                        return False

    def __lt__(self, other):
        """operator < overloading"""

        return other > self

    def __ge__(self, other):
        """operator >= overloading"""

        if self.Year > other.Year:
            return True
        elif self.Year < other.Year:
            return False
        elif self.Year == other.Year:
            if self.Country > other.Country:
                return True
            elif self.Country < other.Country:
                return False
            elif self.Country == other.Country:
                if self.Points > other.Points:
                    return True
                elif self.Points < other.Points:
                    return False
                elif self.Points == other.Points:
                    if self.Club_Name > other.Club_Name:
                        return True
                    elif self.Club_Name < other.Club_Name:
                        return False
                    elif self.Club_Name == other.Club_Name:
                        return True

    def __le__(self, other):
        """operator <= overloading"""

        return other >= self

    def __eq__(self, other):
        """operator == overloading"""
        # Country,Club_Name,City,Year,Coach_Name,Points
        return self.Year == other.Year and self.Country == other.Country and \
            self.Points == other.Points and self.Club_Name == other.Club_Name and \
            self.City == other.City and self.Coach_Name == other.Coach_Name


def linear_search(data, arr):
    '''Просто идём подряд по элементам пока не найдём искомый'''
    for i in range(len(arr)):
        if arr[i][0] == data:
            return i
    return -1


def quick_sort(array):
    """Выбирается опорный элемент - первый, берём все элементы меньшие - слева, больше - справа, рекурсивно повторяем пока длина не будет 0"""

    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)
        return quick_sort(less) + equal + quick_sort(greater)
    else:
        return array


def bin_search(arr, low, high, data, sorted=False):
    '''Берём серединный элемент в отсортированном массиве, сравниваем его с искомым, если меньше то берём левую (правую)
    половину или наоборот, также берём серединный элемент и т.д пока не найдём искомый или же не закончим на подмассиве длинной 1'''
    if not sorted:
        arr = quick_sort(arr)
    if high >= low:

        mid = (high + low) // 2

        if arr[mid] == data:
            return mid

        elif arr[mid] > data:
            return bin_search(arr, low, mid - 1, data, sorted=True)
        else:
            return bin_search(arr, mid + 1, high, data, sorted=True)

    else:
        return -1


size = [100, 10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000]

if __name__ == "__main__":
    times_linear_search = []
    times_bin_search = []

    for i in range(len(size)):
        """Сортируем нагенеренное"""
        f = open("ds_" + str(size[i]) + ".csv", 'r')
        arr = []
        print("STARTING SIZE", size[i])
        for j in f.readlines():
            temp = j.split(",")
            arr.append(Object(temp[0], temp[1], temp[2], int(temp[3]), temp[4], int(temp[5])))
        f.close()

        t1 = time.time()
        test_obj = Object("Russia", "Stade Rennais", "Valencia", int(2012), "Norman White", int(68))
        index = linear_search(arr, test_obj.Country)

        times_linear_search.append(time.time() - t1)
        arr = quick_sort(arr)
        print("sorted")
        t1 = time.time()
        index = bin_search(arr, 0, len(arr) - 1, test_obj, sorted=True)
        times_bin_search.append(time.time() - t1)
        temp2 = []
        print('times_linear_search =', times_linear_search)
        print('times_bin_search = ', times_bin_search)


# def multimap_search():
#     '''
#     #include <iostream>
#     #include <iterator>
#     #include <fstream>
#     #include <chrono>
#     #include <string>
#     #include <map>
#
#     int main() {
#
#         typedef std::multimap < char, int >::iterator MMAPIterator;
#         std::ifstream file("100000.csv");
#         std::multimap < std::string, std::string > my_map; // empty
#         std::string first, second;
#         auto t_start = std::chrono::high_resolution_clock::now();
#
#         while (file >> first >> second) {
#             my_map.insert(std::make_pair(first, second));
#             }
#
#         file.close();
#
#         auto range = my_map.equal_range("Russia");
#         auto t_end = std::chrono::high_resolution_clock::now();
#         auto duration = std::chrono::duration_cast < std::chrono::nanoseconds > (t_end - t_start).count();
#         std::cout << "time: " << (duration + 0.0) / 1000000 << std::endl;
#         return 0;
#
#     }
#     '''
