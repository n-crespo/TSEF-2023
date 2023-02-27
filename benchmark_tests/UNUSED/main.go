// use run/debug default config
package main

import (
	"fmt"
	"time"
)

func fib(n int) int {
	if n <= 1 {
		return n
	} else {
		return fib(n-1) + fib(n-2)
	}
}

func main() {
	for i := 0; i < 30; i++ {
		startTime := time.Now()
		result := fib(40)
		endTime := time.Now()

		duration := endTime.Sub(startTime).Milliseconds()

		fmt.Printf("Call took %dms\n", duration)
		result += 1
	}
}
