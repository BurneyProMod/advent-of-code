package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func parseCoord(s string) (int, int) {
	var x, y int
	fmt.Sscanf(s, "%d,%d", &x, &y)
	return x, y
}

func main() {
	file, err := os.Open("input.txt")
	if err != nil {
		fmt.Println("Failed to open input.txt:", err)
		return
	}
	defer file.Close()

	var part1 [1000][1000]bool
	var part2 [1000][1000]int

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()
		if line == "" {
			continue
		}

		fields := strings.Fields(line)

		var action, start, end string

		if fields[0] == "toggle" {
			action = "toggle"
			start = fields[1]
			end = fields[3]
		} else if fields[0] == "turn" {
			action = fields[1]
			start = fields[2]
			end = fields[4]
		} else {
			fmt.Println("Invalid instruction:", line)
			continue
		}

		x1, y1 := parseCoord(start)
		x2, y2 := parseCoord(end)

		for x := x1; x <= x2; x++ {
			for y := y1; y <= y2; y++ {
				if action == "toggle" {
					part1[x][y] = !part1[x][y]
					part2[x][y] += 2
				} else if action == "on" {
					part1[x][y] = true
					part2[x][y] += 1
				} else if action == "off" {
					part1[x][y] = false
					if part2[x][y] > 0 {
						part2[x][y] -= 1
					}
				}
			}
		}
	}

	if err := scanner.Err(); err != nil {
		fmt.Println("Error reading input.txt:", err)
		return
	}

	onLights := 0
	for x := 0; x < 1000; x++ {
		for y := 0; y < 1000; y++ {
			if part1[x][y] {
				onLights++
			}
		}
	}

	brightness := 0
	for x := 0; x < 1000; x++ {
		for y := 0; y < 1000; y++ {
			brightness += part2[x][y]
		}
	}

	fmt.Println("Part 1: ", onLights)
	fmt.Println("Part 2: ", brightness)
}
