package main

import (
	"bufio"
	"fmt"
	"os"
)

// Part 1
// Returns how many characters the string literal contains in memory.
func memoryLength(line string) int {
	// Remove surrounding quotes if present.
	if len(line) >= 2 && line[0] == '"' && line[len(line)-1] == '"' {
		line = line[1 : len(line)-1]
	}

	count := 0

	for i := 0; i < len(line); {
		// Normal characters
		if line[i] != '\\' {
			count++
			i++
			continue
		}

		// Safety, in case the backslash is the last character of line
		if i+1 >= len(line) {
			break
		}

		next := line[i+1]

		// \\ or \"
		if next == '\\' || next == '"' {
			count += 1
			i += 2
			continue
		}

		// It doesn't matter what the hex digits are, they always represent one character
		if next == 'x' && i+3 < len(line) {

			count += 1
			i += 4
			continue
		}

		count += 1
		i += 2
	}

	return count
}

// Part 2
func encodedLength(line string) int {
	// Start with 2 extra chars for the new surrounding quotes
	encodedLen := len(line) + 2

	// Every " and \ in the original becomes two characters in the encoded string
	for i := 0; i < len(line); i++ {
		if line[i] == '"' || line[i] == '\\' {
			encodedLen += 1
		}
	}

	return encodedLen
}

func main() {
	file, err := os.Open("input.txt")
	if err != nil {
		fmt.Println("Error opening file:", err)
		return
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)

	// Part 1
	totalCodeChars := 0
	totalMemoryChars := 0

	// Part 2
	totalOriginalCode := 0
	totalEncodedCode := 0
	for scanner.Scan() {
		line := scanner.Text()
		// Part 1
		totalCodeChars += len(line)
		totalMemoryChars += memoryLength(line)
		// Part 2
		totalOriginalCode += len(line)
		totalEncodedCode += encodedLength(line)
	}

	if err := scanner.Err(); err != nil {
		fmt.Println("Error reading file:", err)
		return
	}

	fmt.Println("Part 1:")
	fmt.Println("Total characters (code):", totalCodeChars)
	fmt.Println("Total characters (memory):", totalMemoryChars)
	fmt.Println("Difference:", totalCodeChars-totalMemoryChars)
	fmt.Println()
	fmt.Println("Part 2:")
	fmt.Println("Total characters (encoded):", totalEncodedCode)
	fmt.Println("Total characters (original):", totalOriginalCode)
	fmt.Println("Difference (encoded - original):", totalEncodedCode-totalOriginalCode)
}
