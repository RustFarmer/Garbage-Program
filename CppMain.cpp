#include <iostream>
#include <fstream>
#include <string>

int main() {
    std::ifstream file("databasefileDontdellet.txt");

    if (!file.is_open()) {
        std::cerr << "Не удалось открыть файл!" << std::endl;
        return 1;
    }

    std::string line;
    // Читаем файл построчно в цикле
    while (std::getline(file, line)) {
        std::cout << line << std::endl;
    }

    // Файл закрывается автоматически при выходе из области видимости
    file.close();
    return 0;
}