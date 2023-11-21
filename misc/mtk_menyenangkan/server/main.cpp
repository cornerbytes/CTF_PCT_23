#include <iostream>
#include <cstdlib>
#include <ctime>
#include <limits>
#include <random>

void initMenu() {
    std::cout << "> SELAMAT DATANG DI UJIAN MTK PART 1\n";
    std::cout << "> KALIAN AKAN MENDAPATKAN FLAG JIKA BERHASIL MENCAPAI SKOR 25\n";
}

bool question() {
    std::random_device rd;
    std::mt19937 gen(rd());

    std::string operators[] = {"kali", "tambah", "kurang"};
    std::uniform_int_distribution<> operatorDist(0, 2);
    std::uniform_int_distribution<> valueDist(1, 50);

    std::string selectedOperator = operators[operatorDist(gen)];
    int x = valueDist(gen);
    int y = valueDist(gen);
    int answer, userAnswer;

    if (selectedOperator == "kali") {
        answer = x * y;
        std::cout << "Soal : " << x << " * " << y << " ?\n";
    } else if (selectedOperator == "tambah") {
        answer = x + y;
        std::cout << "Soal : " << x << " + " << y << " ?\n";
    } else {
        answer = x - y;
        std::cout << "Soal : " << x << " - " << y << " ?\n";
    }

    std::cout << "Jawaban : ";
    while (!(std::cin >> userAnswer)) {
        std::cout << "Input Error. Hanya Boleh angka\n";
        std::cin.clear();
        std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
        std::cout << "Jawaban : ";
    }

    return userAnswer == answer;
}

int main() {
    const char* FLAG = std::getenv("FLAG");
    int SKOR = 0;

    initMenu();

    try {
        while (SKOR != 25) {
            if (question()) {
                SKOR++;
                std::cout << "SKOR : " << SKOR << "\n\n";
            } else {
                SKOR--;
                std::cout << "SKOR : " << SKOR << "\n\n";
            }

            if (SKOR == 25) {
                std::cout << "CONGRATULATIONS. HERE YOUR FLAG " << FLAG << "\n";
            }
        }
    } catch (...) {
        std::cout << "An error occurred.\n";
    }

    return 0;
}
