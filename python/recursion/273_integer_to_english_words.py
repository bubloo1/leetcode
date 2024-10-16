class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return 'Zero'

        # belowTwenty = ['',        'One',       'Two',      'Three',
        #                 'Four',    'Five',      'Six',      'Seven',
        #                 'Eight',   'Nine',      'Ten',      'Eleven',
        #                 'Twelve',  'Thirteen',  'Fourteen', 'Fifteen',
        #                 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
        # tens = ['',      'Ten',   'Twenty',  'Thirty', 'Forty',
        #         'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']

        # def helper(num: int) -> str:
        #     if num < 20:
        #         s = belowTwenty[num]
        #     elif num < 100:
        #         s = tens[num // 10] + ' ' + belowTwenty[num % 10]
        #     elif num < 1000:
        #         s = helper(num // 100) + ' Hundred ' + helper(num % 100)
        #     elif num < 1000000:
        #         s = helper(num // 1000) + ' Thousand ' + helper(num % 1000)
        #     elif num < 1000000000:
        #         s = helper(num // 1000000) + ' Million ' + helper(num % 1000000)
        #     else:
        #         s = helper(num // 1000000000) + ' Billion ' + helper(num % 1000000000)
        #     return s.strip()

        # return helper(num)
        ones_map = {
            1: "One",
            2: "Two",
            3: "Three",
            4: "Four",
            5: "Five",
            6: "Six",
            7: "Seven",
            8: "Eight",
            9: "Nine",
            10: "Ten",
            11: "Eleven",
            12: "Twelve",
            13: "Thirteen",
            14: "Fourteen",
            15: "Fifteen",
            16: "Sixteen",
            17: "Seventeen",
            18: "Eighteen",
            19: "Nineteen",
        }
        tens_map = {
            20: "Twenty",
            30: "Thirty",
            40: "Forty",
            50: "Fifty",
            60: "Sixty",
            70: "Seventy",
            80: "Eighty",
            90: "Ninety"
        }

        def getString(n):
            res = []
            hundreds = n //100
            if hundreds:
                res.append(ones_map[hundreds] + " Hundred")
            last2 = n % 100
            if last2 >= 20:
                tens, ones = last2 // 10, last2 % 10
                res.append(tens_map[tens * 10])
                if ones: 
                    res.append(ones_map[ones])
            elif last2:
                res.append(ones_map[last2])
            return " ".join(res)

        postfix = ["", " Thousand", " Million", " Billion"]
        i = 0
        res = []
        while num:
            digits = num % 1000
            s = getString(digits)
            if s:
                res.append(s  + postfix[i])
            num = num // 1000
            i += 1
        res.reverse()
        return " ".join(res)

print(123//100,"sfgfg")
newObject = Solution()
print(newObject.numberToWords(12))