package main

import (
	"bufio"
	"fmt"
	"os"
)

// A roll '@' is accessible if it has fewer than 4 '@' in the 8 surrounding spots.

func inBounds(r, c, rows, cols int) bool {
	return r >= 0 && r < rows && c >= 0 && c < cols
}

func countAdjacentRolls(grid [][]byte, r, c int) int {
	rows := len(grid)
	cols := len(grid[0])

	adj := 0

	// check all 8 neighbors
	for dr := -1; dr <= 1; dr++ {
		for dc := -1; dc <= 1; dc++ {
			// skip the center cell since we're only counting neighbors.
			if dr == 0 && dc == 0 {
				continue
			}
			nr := r + dr
			nc := c + dc
			if !inBounds(nr, nc, rows, cols) {
				continue
			}
			if grid[nr][nc] == '@' {
				adj++
			}
		}
	}
	return adj
}

func countAccessible(grid [][]byte) int {
	rows := len(grid)
	cols := len(grid[0])
	accessible := 0
	for r := 0; r < rows; r++ {
		for c := 0; c < cols; c++ {
			if grid[r][c] != '@' {
				continue
			}
			if countAdjacentRolls(grid, r, c) < 4 {
				accessible++
			}
		}
	}

	return accessible
}

// removeOneRound finds all currently-accessible rolls and removes them.
func removeOneRound(grid [][]byte) int {
	rows := len(grid)
	cols := len(grid[0])

	// mark which cells to remove this round
	toRemove := make([][]bool, rows)
	for r := 0; r < rows; r++ {
		toRemove[r] = make([]bool, cols)
	}
	removedThisRound := 0

	// decide what gets removed
	for r := 0; r < rows; r++ {
		for c := 0; c < cols; c++ {
			if grid[r][c] != '@' {
				continue
			}
			if countAdjacentRolls(grid, r, c) < 4 {
				toRemove[r][c] = true
				removedThisRound++
			}
		}
	}
	// remove decided from grid
	for r := 0; r < rows; r++ {
		for c := 0; c < cols; c++ {
			if toRemove[r][c] {
				grid[r][c] = '.'
			}
		}
	}
	return removedThisRound
}

func totalRemovable(grid [][]byte) int {
	total := 0
	for {
		removed := removeOneRound(grid)
		if removed == 0 {
			break
		}
		total += removed
	}
	return total
}

func main() {
	file, err := os.Open("input.txt")
	if err != nil {
		fmt.Println("Failed to open input.txt:", err)
		os.Exit(1)
	}
	defer file.Close()

	// read the grid line by line
	grid := [][]byte{}
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()
		if line != "" {
			grid = append(grid, []byte(line))
		}
	}

	if err := scanner.Err(); err != nil {
		fmt.Println("Error reading input.txt:", err)
		os.Exit(1)
	}

	// Part 1
	part1 := countAccessible(grid)

	// Part 2
	// Make a copy to avoid destructive editing.
	gridCopy := make([][]byte, len(grid))
	for r := range grid {
		gridCopy[r] = make([]byte, len(grid[r]))
		copy(gridCopy[r], grid[r])
	}

	part2 := totalRemovable(gridCopy)

	fmt.Println("Part 1:", part1)
	fmt.Println("Part 2:", part2)
}
