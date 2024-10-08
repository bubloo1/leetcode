package bitmap

func reverseBits(num uint32) uint32 {
	var res, bit uint32 = 0, 0

	for i := 0; i < 32; i++ {
		bit = (num >> i) & 1
		res = res | (bit << (31 - i))
	}
	return res
}
