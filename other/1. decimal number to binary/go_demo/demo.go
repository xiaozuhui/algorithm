package main

import (
	"fmt"
	"strconv"
	"strings"
)

func main() {
	var number = 2893747748326487237
	res := make([]string, 0, 0)
	for {
		if number <= 0 {
			break
		}
		res = append(res, strconv.Itoa(number%2))
		number = number / 2
	}
	fmt.Println(fmt.Sprintf("二进制是：%s", strings.Join(res, "")))
}
