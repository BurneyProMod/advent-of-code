package main

import (
	"bufio"
	"fmt"
	"math/big"
	"os"
)

const pickCountPart2 = 12

func toDigit(c byte) int {
	return int(c - '0')
}

// maxJoltage2Digits finds the biggest 2-digit number by picking 2 digits from line in order
func maxJoltage2Digits(bank string) int {
	best := -1

	for i := 0; i < len(bank); i++ {
		a := toDigit(bank[i])

		for j := i + 1; j < len(bank); j++ {
			b := toDigit(bank[j])

			value := a*10 + b
			if value > best {
				best = value
			}
		}
	}

	return best
}

// Greedy approach to find the best k digits in order.
func bestKDigits(s string, k int) string {
	n := len(s)
	if n < k {
		return ""
	}

	toRemove := n - k
	stack := make([]byte, 0, n)

	// Walk through each digit in the string.
	for i := 0; i < n; i++ {
		currentDigit := s[i]
		// If the last digit we kept is smaller than this new digit, and we are still allowed to throw away digits, then throw away the smaller digit.
		for toRemove > 0 && len(stack) > 0 && stack[len(stack)-1] < currentDigit {
			stack = stack[:len(stack)-1]
			toRemove--
		}

		stack = append(stack, currentDigit)
	}

	if toRemove > 0 {
		stack = stack[:len(stack)-toRemove]
	}

	return string(stack[:k])
}

func main() {
	file, err := os.Open("input.txt")
	if err != nil {
		fmt.Println("Failed to open input.txt:", err)
		os.Exit(1)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)

	var totalPart1 int64 = 0
	totalPart2 := big.NewInt(0)

	for scanner.Scan() {
		bank := scanner.Text()
		if bank == "" {
			continue
		}

		// Part 1
		if len(bank) >= 2 {
			best2 := maxJoltage2Digits(bank)
			if best2 >= 0 {
				totalPart1 += int64(best2)
			}
		}

		// Part 2
		best12Str := bestKDigits(bank, pickCountPart2)
		if best12Str != "" {
			value := new(big.Int)
			value.SetString(best12Str, 10)
			totalPart2.Add(totalPart2, value)
		}
	}

	if err := scanner.Err(); err != nil {
		fmt.Println("Error reading input.txt:", err)
		os.Exit(1)
	}

	fmt.Println("Part 1:", totalPart1)
	fmt.Println("Part 2:", totalPart2.String())
}
