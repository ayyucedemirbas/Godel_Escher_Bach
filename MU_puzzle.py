class Node:
    def __init__(self, value, parent=None):
        self.value = value
        self.parent = parent
        self.children = []

    def add_child(self, child_value):
        child_node = Node(child_value, self)
        self.children.append(child_node)
        return child_node

    def print_path(self):
        if self.parent is not None:
            self.parent.print_path()
        print(self.value)

def apply_rules(input_str):
    results = []
    # Rule 1
    if input_str[-1] == 'I':
        results.append(input_str + 'U')
    # Rule 2
    if input_str[0] == 'M':
        results.append(input_str + input_str[1:])
    # Rule 3
    results.extend(input_str.replace('III', 'U', 1) for _ in range(input_str.count('III')))
    # Rule 4
    results.extend(input_str.replace('UU', '', 1) for _ in range(input_str.count('UU')))
    return results

def search_mu(start, depth_limit=10):
    root = Node(start)
    queue = [(root, 0)]
    while queue:
        current_node, current_depth = queue.pop(0)
        if current_node.value == 'MU':
            print("Solution found:")
            current_node.print_path()
            return True
        if current_depth < depth_limit:
            for result in apply_rules(current_node.value):
                child_node = current_node.add_child(result)
                queue.append((child_node, current_depth + 1))
    print("No solution within depth limit.")
    return False

# Start the search with the initial string MI
search_mu('MI', 10)
