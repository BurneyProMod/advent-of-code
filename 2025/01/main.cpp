#include <fstream>
#include <iostream>
#include <string>

long long hits_to_zero(int pos, long long dist, char dir) {
    const int N = 100;

    long long first;
    if (dir == 'R') {
        first = (N - pos) % N;   // how many clicks until 0
    } else { // 'L'
        first = pos % N;
    }

    if (first == 0) first = N;  // if already at 0, next hit is after 100 clicks

    if (dist < first) return 0;
    return 1 + (dist - first) / N;
}

int main() {
    // Starting position of lock is 50
    int pos = 50;
    int part1 = 0;

    // Import file
    std::ifstream in("input.txt");
    if (!in) {
        std::cerr << "Failed to open input.txt\n";
        return 1;
    }

    std::string line;
    while (std::getline(in, line)) {
        // Determine if Left or Right
        char dir = line[0];
        // Distance to move. stoi converts string to integer
        int dist = std::stoi(line.substr(1));
        if (dir == 'R') {
            pos = (pos + dist) % 100;
        }
        else if (dir == 'L') {
            // Handle wrap around without negatives.
            pos = (pos + 100 - (dist % 100)) % 100;
        }
        // If the dial stops at 0, increment password variable
        if (pos == 0) ++part1;
    }
    std::cout << "Part 1: " << part1 << std::endl;

    // Reset file to beginning for part 2
    in.clear();
    in.seekg(0, std::ios::beg);
    // reset position for part 2
    pos = 50;
    long long part2 = 0;
    while (std::getline(in, line)) {
        char dir = line[0];
        long long dist = std::stoll(line.substr(1));

        part2 += hits_to_zero(pos, dist, dir);

        int step = static_cast<int>(dist % 100);
        if (dir == 'R') {
            pos = (pos + step) % 100;
        } 
        else if (dir == 'L') {
            pos = (pos + 100 - step) % 100;
        }
    }
    std::cout << "Part 2: " << part2 << std::endl;
    return 0;
}