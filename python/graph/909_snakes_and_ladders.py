from typing import List
from collections import deque

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:

        length = len(board)
        board.reverse()

        def squareToPosition(square):
            r = (square - 1) // length
            c = (square - 1) % length
            if r % 2 != 0:
                c = length - 1 - c
            return [r,c]

        queue = deque()
        queue.append([1,0])
        visited = set()

        while queue:
            square, moves = queue.popleft()

            for i in range(1,7):

                nextSquare = square + i
                r,c = squareToPosition(nextSquare)
                if board[r][c] != -1:
                    nextSquare = board[r][c]
                if nextSquare == length * length:
                    return moves + 1
                if nextSquare not in visited:
                    visited.add(nextSquare)
                    queue.append([nextSquare, moves+1])
        return -1