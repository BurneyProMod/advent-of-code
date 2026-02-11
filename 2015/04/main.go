package main

import (
	"bufio"
	"crypto/md5"
	"encoding/hex"
	"fmt"
	"os"
	"strconv"
)

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

	secret := scanner.Text()
	part1 := 0
	part2 := 0

	for n := 1; part1 == 0 || part2 == 0; n++ {
		text := secret + strconv.Itoa(n)
		sum := md5.Sum([]byte(text))
		hash := hex.EncodeToString(sum[:])

		// Part 1
		if part1 == 0 && hash[:5] == "00000" {
			part1 = n
			fmt.Println("Part 1:", part1)
		}
		// Part 2
		if part2 == 0 && hash[:6] == "000000" {
			part2 = n
			fmt.Println("Part 2:", part2)
		}
	}
}
