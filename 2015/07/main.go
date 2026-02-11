package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

type Value struct {
	isNumber bool
	number   uint16
	wire     string
}

type Expr struct {
	operator string
	inputA   Value
	inputB   Value
	shift    uint16
}

func parseValue(token string) Value {
	var n int
	if _, err := fmt.Sscanf(token, "%d", &n); err == nil {
		return Value{isNumber: true, number: uint16(n)}
	}
	return Value{isNumber: false, wire: token}
}

func resolveValue(v Value, instructions map[string]Expr, wireValuesCache map[string]uint16) uint16 {
	if v.isNumber {
		return v.number
	}
	return resolveWire(v.wire, instructions, wireValuesCache)
}

func resolveWire(wire string, instructions map[string]Expr, wireValuesCache map[string]uint16) uint16 {
	// If we already computed this wire, reuse it.
	if cachedValue, ok := wireValuesCache[wire]; ok {
		return cachedValue
	}

	expr, ok := instructions[wire]
	if !ok {
		fmt.Println("Unknown wire:", wire)
		return 0
	}

	var result uint16

	switch expr.operator {
	case "":
		result = resolveValue(expr.inputA, instructions, wireValuesCache)

	case "NOT":
		result = ^resolveValue(expr.inputA, instructions, wireValuesCache)

	case "AND":
		result = resolveValue(expr.inputA, instructions, wireValuesCache) &
			resolveValue(expr.inputB, instructions, wireValuesCache)

	case "OR":
		result = resolveValue(expr.inputA, instructions, wireValuesCache) |
			resolveValue(expr.inputB, instructions, wireValuesCache)

	case "LSHIFT":
		result = resolveValue(expr.inputA, instructions, wireValuesCache) << expr.shift

	case "RSHIFT":
		result = resolveValue(expr.inputA, instructions, wireValuesCache) >> expr.shift

	default:
		fmt.Println("Unknown operator:", expr.operator, "for wire:", wire)
		return 0
	}

	// Store the result so we don't compute this wire again.
	wireValuesCache[wire] = result
	return result
}

func main() {
	file, err := os.Open("input.txt")
	if err != nil {
		fmt.Println("Failed to open input.txt:", err)
		return
	}
	defer file.Close()

	instructions := make(map[string]Expr)

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()
		if line == "" {
			continue
		}

		parts := strings.Split(line, " -> ")
		leftSide := parts[0]
		outputWire := parts[1]

		tokens := strings.Fields(leftSide)

		if len(tokens) == 1 {
			instructions[outputWire] = Expr{
				operator: "",
				inputA:   parseValue(tokens[0]),
			}
		} else if len(tokens) == 2 {
			instructions[outputWire] = Expr{
				operator: tokens[0], // "NOT"
				inputA:   parseValue(tokens[1]),
			}
		} else if len(tokens) == 3 {
			operator := tokens[1]

			if operator == "LSHIFT" || operator == "RSHIFT" {
				instructions[outputWire] = Expr{
					operator: operator,
					inputA:   parseValue(tokens[0]),
					shift:    parseValue(tokens[2]).number, // shift amount is numeric
				}
			} else {
				instructions[outputWire] = Expr{
					operator: operator, // "AND" or "OR"
					inputA:   parseValue(tokens[0]),
					inputB:   parseValue(tokens[2]),
				}
			}
		} else {
			fmt.Println("Unexpected instruction:", line)
			return
		}
	}

	if err := scanner.Err(); err != nil {
		fmt.Println("Error reading input.txt:", err)
		return
	}

	// Part 1
	wireValuesCachePart1 := make(map[string]uint16)
	signalOnA := resolveWire("a", instructions, wireValuesCachePart1)
	fmt.Println("Part 1:", signalOnA)

	// Part 2
	instructions["b"] = Expr{
		operator: "",
		inputA:   Value{isNumber: true, number: signalOnA},
	}

	// Reset all cached wire values
	wireValuesCachePart2 := make(map[string]uint16)
	newSignalOnA := resolveWire("a", instructions, wireValuesCachePart2)
	fmt.Println("Part 2:", newSignalOnA)
}
