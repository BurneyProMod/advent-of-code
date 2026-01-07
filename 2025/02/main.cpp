/* 
Plan of approach:
Get ID range
For each id: determine number of digits, then split in the center.
compare substrings, If all digits match, add ID to array
Repeat for next range of IDs
Add all units in array
*/

#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <cctype>

// Let s = to_string(id)
// For every possible block length len that evenly divides s.size() and len < s.size, check if repeating
bool isRepeated(long long n) {
    if (n < 0) return false;
    std::string s = std::to_string(n);
    std::size_t L = s.size();
    // Try every possible block length
    for (std::size_t len = 1; len <= L / 2; ++len) {
        if (L % len != 0) continue;           
        // must divide evenly
        std::size_t reps = L / len;
        const std::string block = s.substr(0, len);
        bool ok = true;
        // Compare each character against what it should be in repeated blocks
        for (std::size_t i = 0; i < L; ++i) {
            if (s[i] != block[i % len]) {
                ok = false;
                break;
            }
        }
        if (ok && reps >= 2) return true;
    }
    return false;
}

int main() {
    std::ifstream in("input.txt");
    if (!in) {
        std::cerr << "Failed to open input.txt\n";
        return 1;
    }
    std::string line;
    if (!std::getline(in, line)) {
        std::cerr << "input.txt is empty\n";
        return 1;
    }
    std::vector<long long> invalidIDs;
    long long sum = 0;
    // Parse: ranges separated by commas, each range is "A-B"
    std::size_t i = 0;
    while (i < line.size()) {
        while (i < line.size() && line[i] == ',')
            ++i;
        if (i >= line.size()) break;
        // Read A up to '-'
        std::size_t dash = line.find('-', i);
        if (dash == std::string::npos) {
            std::cerr << "Parse error: missing '-' after position " << i << "\n";
            return 1;
        }
        long long a = std::stoll(line.substr(i, dash - i));
        // Read B up to ',' or EOF
        std::size_t comma = line.find(',', dash + 1);
        std::string bStr = (comma == std::string::npos)
            ? line.substr(dash + 1)
            : line.substr(dash + 1, comma - (dash + 1));
        long long b = std::stoll(bStr);
        // Move i to next range
        i = (comma == std::string::npos) ? line.size() : comma + 1;
        // Calculate invalid IDs in range [a, b]
        for (long long id = a; id <= b; ++id) {
            if (isRepeated(id)) {
                invalidIDs.push_back(id);
                sum += id;
            }
        }
    }

    // Print array of invalid IDs
    std::cout << "Invalid IDs found (" << invalidIDs.size() << "):\n";
    for (long long id : invalidIDs) {
        std::cout << id << "\n";
    }

    std::cout << "Sum: " << sum << "\n";
    return 0;
}