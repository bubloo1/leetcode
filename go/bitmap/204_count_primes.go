package bitmap

func CountPrimes(n int) int {

	primes := make([]bool, n)

	for i := range primes {
		primes[i] = true
	}

	for i := 2; i*i < n; i++ {
		if primes[i] {
			for j := i; j*i < n; j++ {
				primes[j*i] = false
			}
		}
	}

	primeCount := 0

	for i := 2; i < n; i++ {
		if primes[i] {
			primeCount++
		}
	}

	return primeCount

	//brute force
	// if n <= 1 {
	// 	return 0
	// }
	// count := 0
	// for i := 2; i < n; i++ {
	// 	for j := 2; j < i; j++ {
	// 		if i%j == 0 {
	// 			count++
	// 			break
	// 		}
	// 	}
	// }
	// return (n - count) - 2

}
