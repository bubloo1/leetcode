class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stack = []
        
        for ch in expression:
            if ch == ')':  # End of an expression
                # We need to pop the boolean values between '(' and ')'
                seen = set()
                while stack[-1] != '(':
                    seen.add(stack.pop())
                stack.pop()  # Remove the '('
                
                # Get the operator before '('
                operator = stack.pop()
                
                # Perform the operation based on the operator
                if operator == '!':
                    # Negate the only value inside
                    stack.append('t' if 'f' in seen else 'f')
                elif operator == '&':
                    # AND operation: result is true only if all are true
                    stack.append('t' if 'f' not in seen else 'f')
                elif operator == '|':
                    # OR operation: result is true if any is true
                    stack.append('t' if 't' in seen else 'f')
            elif ch != ',':
                stack.append(ch)  # Push other characters except commas
        
        # Final result should be the only item left in the stack
        return stack[0] == 't'