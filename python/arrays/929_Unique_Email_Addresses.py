from typing import List
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        res = set()
        for email in emails:
            local, domain = email.split('@')
            temp = ''
            for c in local:
                if c == '.':
                    continue
                elif c == '+':
                    break
                else:
                    temp += c
                    # temp = ''.join(temp + '@' + domain)
            res.add(temp+'@'+domain)
        return len(res)