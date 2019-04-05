nums = []
with open("day8.txt") as f:
    nums = f.read().split(" ")


class Node:
    def __init__(self):
        self.parent = None
        self.children = []
        self.metadata_entries = []
        self.num_children = 0
        self.num_metadata_entries = 0

    def __str__(self):
        return "Children:" + str(self.num_children) + ";" + str(self.children) + "Metadata:" + str(
            self.num_metadata_entries) + ";" + str(self.metadata_entries)

    def __repr__(self):
        return "Children:" + str(self.num_children) + ";" + str(self.children) + "; Metadata:" + str(
            self.num_metadata_entries) + ";" + str(self.metadata_entries)


def process_input(input_nums):
    current = None
    root = None

    while input_nums:
        if current and current.num_children == len(current.children):
            current.metadata_entries = list(map(lambda x: int(x), input_nums[:current.num_metadata_entries]))
            input_nums = input_nums[current.num_metadata_entries:]
            if not current.parent:
                root = current
            current = current.parent
        else:
            new_node = Node()
            new_node.parent = current
            new_node.num_children = int(input_nums.pop(0))
            new_node.num_metadata_entries = int(input_nums.pop(0))
            if current:
                current.children.append(new_node)
            current = new_node

    return root


def dfs(tree):
    print(tree.num_children, tree.num_metadata_entries, tree.metadata_entries)
    for child in tree.children:
        dfs(child)


def sum_metadata(tree):
    total = sum(tree.metadata_entries)
    for child in tree.children:
        total += sum_metadata(child)
    return total


tree = process_input(nums)
# dfs(tree)
print(sum_metadata(tree))


# ************************************* PART TWO *******************************************

def node_value(tree):
    if tree.num_children == 0:
        return sum(tree.metadata_entries)
    val = 0
    for entry in tree.metadata_entries:
        if entry <= tree.num_children:
            val += node_value(tree.children[entry-1])

    return val

print(node_value(tree))
