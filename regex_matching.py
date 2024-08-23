class Node(object):
    def __init__(self, terminal, mapping):
        self.terminal = terminal
        self.mapping = mapping

    def match(self, current, ret):
        if len(current) == 0:
            if self.terminal:
                ret[0] = True
            return
        

        for mtch in [self.mapping.get(current[0], None), self.mapping.get(".", None)]:
            if mtch is not None:
                mtch.match(current[1:], ret)


    
    def __repr__(self):
        return f"terminal: {self.terminal} mapping: {self.mapping}"

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        start = Node(False, {})
        prev = start

        ptr = 0

        while ptr != len(p):
            if p[ptr] != "*":
                new_node = Node(False, {})
                prev.mapping[p[ptr]] = new_node
                prev = new_node
            else:
                prev.mapping[p[ptr-1]] = prev
            ptr += 1

        prev.terminal = True

        match_found = [False]
        start.match(s, match_found)

        return match_found[0]


s = Solution()
print(s.isMatch("aaa", "a*"))
print(s.isMatch("ab", ".*"))
print(s.isMatch("aab", "c*a*b"))
