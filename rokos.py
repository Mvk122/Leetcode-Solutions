from dataclasses import dataclass, field

@dataclass
class Node:
    subtrees: "array" = field(default_factory=list)

def set_counts(tree):
    if len(tree.subtrees) == 0:
        tree.count = 1
        return 1
    else: 
        total = 1
        for subtree in tree.subtrees:
            total += set_counts(subtree)
        tree.count = total
        return total

def solution():
    a = Node()
    b = Node()
    c = Node(subtrees=[a, b])
    d = Node()
    e = Node(subtrees=[d])
    f = Node(subtrees=[c, e])
    set_counts(f)
    print(f)

solution()

def solve_better(node, counts, seen):
    if len(node.subtrees) == 0:
        if id(node) not in seen:
            seen.add(id(node))
            counts[0] += 1
        return 0
    else:
        all_nodes = []
        for sub in node.subtrees:
            all_nodes.append(solve_better(sub, counts, seen))
            if len(set(all_nodes)) == 1 and id(node) not in seen:
                seen.add(id(node))
                counts[0] += 1
        return sum(all_nodes)
    
def solve_better(node, counts, seen):
    if len(node.subtrees) == 0:
        if id(node) not in seen:
            seen.add(id(node))
            counts[0] += 1
        return 1
    else:
        all_nodes = []
        for sub in node.subtrees:
            all_nodes.append(solve_better(sub, counts, seen))
            if len(set(all_nodes)) == 1 and id(node) not in seen:
                seen.add(id(node))
                counts[0] += 1
        return sum(all_nodes)