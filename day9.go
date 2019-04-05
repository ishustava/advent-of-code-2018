package main

import "fmt"

type node struct {
	number int
	ccw *node
	cw *node
}

type circle struct {
	currentMarble *node
}

func (c *circle) addOneClockwise(item int) *node {
	oneCWMarble := c.currentMarble.cw
	twoCWMarble := c.currentMarble.cw.cw

	newMarble := new(node)
	newMarble.number = item
	newMarble.cw = twoCWMarble
	newMarble.ccw = oneCWMarble

	oneCWMarble.cw = newMarble
	twoCWMarble.ccw = newMarble

	c.currentMarble = newMarble

	return newMarble
}

func (c *circle) remove7Counterclockwise() *node {
	current := c.currentMarble
	for i := 0; i < 7; i++ {
		current = current.ccw
	}
	current.ccw.cw = current.cw
	current.cw.ccw = current.ccw
	c.currentMarble = current.cw

	return current
}

func main() {
	numPlayers := 476
	numMarbles := 71657*100

	scores := make(map[int]int)
	for i := 0; i < numPlayers; i++ {
		scores[i] = 0
	}

	first := new(node)
	first.number = 0
	first.cw = first
	first.ccw = first
	circle := new(circle)
	circle.currentMarble = first

	for marble := 1; marble <= numMarbles; marble++ {
		player := marble % numPlayers

		if marble % 23 == 0 {
			scores[player] += marble
			removed := circle.remove7Counterclockwise()
			scores[player] += removed.number
			//fmt.Println(circle.currentMarble.ccw, circle.currentMarble, circle.currentMarble.cw)
			continue
		}

		circle.addOneClockwise(marble)
		//fmt.Println(newItem.ccw, newItem, newItem.cw)
	}

	maxScore := 0
	for _, score := range scores {
		if score > maxScore {
			maxScore = score
		}
	}
	fmt.Println(maxScore)
}
