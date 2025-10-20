class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        res = []
        m = len(searchWord)
        products.sort()

        prefix = []
        start = 0

        def binary_search(target, start):
            l, r = start, len(products)
            while l < r:
                mid = l + (r - l) // 2
                if products[mid] >= target:
                    r = mid
                else:
                    l = mid + 1
            return l

        for i in range(m):
            prefix.append(searchWord[i])
            start = binary_search("".join(prefix), start)

            cur = []
            for j in range(start, min(start + 3, len(products))):
                if products[j].startswith("".join(prefix)):
                    cur.append(products[j])
                else:
                    break

            res.append(cur)

        return res