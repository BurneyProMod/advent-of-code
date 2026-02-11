package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func Part1(line string) bool {
	// Contains 3 vowels
	vowels := 0
	for _, i := range line {
		if i == 'a' || i == 'e' || i == 'i' || i == 'o' || i == 'u' {
			vowels++
		}
	}
	// At least one letter twice in a row
	hasDouble := false
	for i := 1; i < len(line); i++ {
		if line[i] == line[i-1] {
			hasDouble = true
			// No need to check for more than one double
			break
		}
	}
	// Does not contain prohibited substrings
	hasSubstring := false
	var prohibited = []string{"ab", "cd", "pq", "xy"}
	for _, p := range prohibited {
		if strings.Contains(line, p) {
			return false
		}
	}
	if vowels >= 3 && hasDouble && !hasSubstring {
		return true
	}
	return false
}

func Part2(line string) bool {
	// Contains a pair of two letter that don't overlap
	hasPair := false
	for i := 0; i < len(line)-1; i++ {
		pair := line[i : i+2]
		if strings.Count(line, pair) > 1 {
			hasPair = true
			break
		}
	}
	// Contains a letter that repeats with one letter between them
	hasRepeat := false
	for i := 0; i < len(line)-2; i++ {
		if line[i] == line[i+2] {
			hasRepeat = true
			break
		}
	}
	return hasPair && hasRepeat
}

func main() {
	file, err := os.Open("input.txt")
	if err != nil {
		fmt.Println("Failed to open input.txt:", err)
		return
	}
	defer file.Close()
	scanner := bufio.NewScanner(file)
	if !scanner.Scan() {
		fmt.Println("input.txt is empty")
		return
	}

	part1Counter := 0
	part2Counter := 0
	for scanner.Scan() {
		var line string = scanner.Text()
		if Part1(line) {
			part1Counter++
		}
		if Part2(line) {
			part2Counter++
		}
	}
	fmt.Println("Part 1:", part1Counter)
	fmt.Println("Part 2:", part2Counter)
}
