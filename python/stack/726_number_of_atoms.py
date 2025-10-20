class Solution:
    def countOfAtoms(self, formula: str) -> str:
        stack = [defaultdict(int)]
        i = 0
        n = len(formula)
        while i < n:
            if formula[i] == '(':
                stack.append(defaultdict(int))
                i += 1
            
            elif formula[i] == ')':
                i += 1
                # parse multiplier number after ')'
                start = i
                while i < n and formula[i].isdigit():
                    i += 1
                multiplier = int(formula[start:i] or 1)
                
                poppedMap = stack.pop()
                for atom, cnt in poppedMap.items():
                    stack[-1][atom] += cnt * multiplier

            else:
                # parse atom name
                start = i
                i += 1  # move past capital letter
                while i < n and formula[i].islower():
                    i += 1
                atom = formula[start:i]

                # parse possible number after atom
                start = i
                while i < n and formula[i].isdigit():
                    i += 1
                count = int(formula[start:i] or 1)

                stack[-1][atom] += count
                
        # Final result in stack[0]
        result = ""
        for atom in sorted(stack[-1]):
            count = stack[-1][atom]
            result += atom + (str(count) if count > 1 else "")
        return result