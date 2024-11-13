package arrays

import "math/rand"

type RandomizedSet struct {
	itemsSet  map[int]int
	itemsList []int
}

func Constructor() RandomizedSet {
	return RandomizedSet{
		itemsSet: make(map[int]int),
	}
}

func (this *RandomizedSet) Insert(val int) bool {

	if _, exists := this.itemsSet[val]; exists {
		return false
	}

	this.itemsSet[val] = len(this.itemsSet)
	this.itemsList = append(this.itemsList, val)
	return true
}

func (this *RandomizedSet) Remove(val int) bool {
	if _, exists := this.itemsSet[val]; !exists {
		return false
	}

	idx := this.itemsSet[val]

	lastVal := this.itemsList[len(this.itemsList)-1]
	this.itemsList[idx] = lastVal
	this.itemsSet[lastVal] = idx
	this.itemsList = this.itemsList[:len(this.itemsList)-1]
	delete(this.itemsSet, val)
	return true
}

func (this *RandomizedSet) GetRandom() int {
	return this.itemsList[rand.Intn(len(this.itemsList))]
}

//   Your RandomizedSet object will be instantiated and called as such:
