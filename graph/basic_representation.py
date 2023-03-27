"""
input : n,m
and m lines containing the edge info.
Given the above info, represent it to adjacency matrix and adjacency list for graph.
"""


def create_adjacency_matrix(input_arr, m, n):
    adj_matrix = [[0 for j in range(n + 1)] for i in range(n + 1)]
    for i, item_list in enumerate(input_arr):
        adj_matrix[item_list[0]][item_list[1]] = 1
        adj_matrix[item_list[1]][item_list[0]] = 1
    return adj_matrix


def create_adjacency_list(input_arr, m, n):
    adj_list = dict()
    for i in range(n):
        adj_list[i] = []

    for (u, v) in input_arr:
        adj_list[u].append(v)
        adj_list[v].append(u)

    for item in adj_list.items():
        print(item)


if __name__ == '__main__':
    n, m = [int(ele) for ele in input("Enter nodes and edges\n").split(",")]
    input_ = [[int(ele) for ele in input("enter node,node\n").split(",")] for i in range(m)]
    print(input_)
    print(create_adjacency_matrix(input_, m, n))
    create_adjacency_list(input_, m, n)
