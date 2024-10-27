from typing import List
import collections
from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # # Creating a queue of type (word, transitions to reach 'word').
        # queue = deque([(beginWord, 1)])

        # # Using a set to store words for quick lookup and removal.
        # word_set = set(wordList)
        # word_set.discard(beginWord)

        # while queue:
        #     word, steps = queue.popleft()

        #     # Return steps as soon as the target_word is found.
        #     if word == endWord:
        #         return steps

        #     for i in range(len(word)):
        #         # Replace each character of 'word' with char from a-z.
        #         for ch in range(ord('a'), ord('z') + 1):
        #             new_word = word[:i] + chr(ch) + word[i + 1:]

        #             # Check if it exists in the set and enqueue it.
        #             if new_word in word_set:
        #                 word_set.remove(new_word)
        #                 queue.append((new_word, steps + 1))

        # # If there is no transformation sequence possible.
        # return 0

        if endWord not in wordList:
            return 0

        nei = collections.defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j + 1 :]
                nei[pattern].append(word)

        visit = set([beginWord])
        q = deque([beginWord])
        res = 1
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j + 1 :]
                    for neiWord in nei[pattern]:
                        if neiWord not in visit:
                            visit.add(neiWord)
                            q.append(neiWord)
            res += 1
        return 0

        