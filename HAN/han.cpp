#include <iostream>
#include <fstream>
#include <string>

int main() {
    // Создаём строку из 2_100_100 символов 'A'
    std::string text(2100100, 'A');

    // Открываем файл для записи
    std::ofstream file("output.txt");
    if (file.is_open()) {
        file << text;
        file.close();
        std::cout << "Файл output.txt создан с 2_100_100 символами." << std::endl;
    } else {
        std::cout << "Не удалось открыть файл для записи." << std::endl;
    }

    return 0;
}
