from matplotlib import pyplot


def main():
    """Генерируем графики"""

    size = [100, 10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000]

    times_linear_search = [7.152557373046875e-06, 1.3113021850585938e-05, 4.100799560546875e-05, 1.33514404296875e-05, 1.3113021850585938e-05, 1.2636184692382812e-05, 1.430511474609375e-05, 1.33514404296875e-05, 1.2159347534179688e-05, 1.1682510375976562e-05, 1.3113021850585938e-05]
    times_bin_search =  [1.2874603271484375e-05, 6.365776062011719e-05, 3.790855407714844e-05, 4.315376281738281e-05, 7.128715515136719e-05, 4.696846008300781e-05, 7.176399230957031e-05, 4.100799560546875e-05, 5.1975250244140625e-05, 4.458427429199219e-05, 0.00011134147644042969]
    times_multimap_search = [0.174715, 25.2602, 62.9474, 155.504, 141.14, 170.558, 208.112, 303.202, 336.401, 332.455, 371.996]

    for i in range(len(times_multimap_search)):
        times_multimap_search[i] /= 1000

    pyplot.plot(size, times_linear_search, label="linear search")
    pyplot.plot(size, times_bin_search, label="bin search")
    pyplot.plot(size, times_multimap_search, label="multimap bin search")

    pyplot.xlabel("Количество элементов, штук")
    pyplot.ylabel("Время, секунды")
    pyplot.legend()
    pyplot.savefig("bin_lin_presorted")


if __name__ == "__main__":
    main()
