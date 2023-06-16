from matplotlib import pyplot


def main():
    """Генерируем графики"""

    size = [100, 10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000]

    times_linear_search = [0.012909650802612305, 0.002028942108154297, 0.0018072128295898438, 0.0003268718719482422,
                           0.017965078353881836, 0.0004138946533203125, 0.0006740093231201172, 0.0012631416320800781,
                           0.0017850399017333984, 0.0006504058837890625, 0.0001862049102683941]
    times_bin_search = [0.004589080810546875, 0.0552670955657959, 0.016047000885009766, 0.000576019287109375,
                        0.00039076805114746094, 0.006530046463012695, 0.00028586387634277344, 0.0005159378051757812,
                        0.0052068233489990234, 0.0021288394927978516, 0.008389949798459124]

    times_multimap_search = [0, 0.001, 23.0054, 37.0082, 49.459, 61.0143, 76.0166, 91.0198, 103.023, 115.025, 119]

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
