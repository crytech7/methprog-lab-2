#include <iostream>
#include <iterator>
#include <fstream>
#include <chrono>
#include <string>
#include <map>


int main() {
    std::string csv_file;
    std::cout << "Enter csv file to read: ";
    std::cin >> csv_file;
    typedef std::multimap < char, int >::iterator MMAPIterator;
    std::ifstream file(csv_file);
    std::multimap < std::string, std::string > my_map; // empty
    std::string first, second;
    auto t_start = std::chrono::high_resolution_clock::now();

    while (file >> first >> second) {
        my_map.insert(std::make_pair(first, second));
        }

    file.close();

    auto range = my_map.equal_range("Russia");
    auto t_end = std::chrono::high_resolution_clock::now();
    auto duration = std::chrono::duration_cast < std::chrono::nanoseconds > (t_end - t_start).count();
    std::cout << "time: " << (duration + 0.0) / 1000000 << std::endl;
    return 0;

}
