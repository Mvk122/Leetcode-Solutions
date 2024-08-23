# TODO Complete
def getPermutation(self, n: int, k: int) -> str:
    pass

def get_path_to_node(n: int, node_index: int) -> list:
    # Initialize variables
    nodes_in_previous_layer = 0
    nodes_so_far = 1
    n_cpy = n
    current_layer = 0
    nodes_per_layer_count = []

    # Getting the layer of the node
    while nodes_so_far < node_index:
        nodes_in_previous_layer = nodes_in_previous_layer + n_cpy
        nodes_so_far += nodes_in_previous_layer
        nodes_per_layer_count.append(nodes_so_far)
        n_cpy -= 1
        current_layer += 1
        if n_cpy < 0:
            raise Exception("Node not in graph")
        
    print(n_cpy)
    return current_layer       


print(get_path_to_node(3, 11))
