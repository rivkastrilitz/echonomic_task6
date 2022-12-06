import networkx as nx
import doctest


def find_loop(graph:nx.DiGraph):
    """
    This function returns cycle in graph with edge mul < 1 if exisit in the given graph
    otherwise returns -1

    >>> find_loop(crate_graph1())
    [1, 2, 3]
    >>> find_loop(crate_graph2())
    -1
    >>> find_loop(crate_graph3())
    -1
    >>> find_loop(crate_graph4())
    [5, 6, 7]
    >>> find_loop(crate_graph5())
    [1, 2, 5, 6, 7]
    >>> find_loop(nx.DiGraph())
    -1
    >>> find_loop(crate_graph6())
    -1
    """
    all_cycle = nx.simple_cycles(graph)
    for cycle in all_cycle:
        res = cycle_mul(graph,cycle)
        if not res == -1:
            return res
    return -1


# find cycle with mul less than 1
def cycle_mul(graph: nx.DiGraph, cycle: list):
    mul = 1
    for i in range(len(cycle)-1):
        mul *= graph[cycle[i]][cycle[i+1]]["weight"]
    mul *= graph[cycle[len(cycle)-1]][cycle[0]]["weight"]
    if 0 < mul < 1:
        return cycle
    else:
        return -1


def crate_graph1():
    g = nx.DiGraph()
    g.add_node(1)
    g.add_node(2)
    g.add_node(3)
    g.add_node(4)
    g.add_edge(1, 2, weight=0.2)
    g.add_edge(2, 3, weight=0.1)
    g.add_edge(3, 1, weight=0.1)
    return g

# no cycle because mul is bigger than 1
def crate_graph2():
    g = nx.DiGraph()
    g.add_node(1)
    g.add_node(2)
    g.add_node(3)
    g.add_node(4)
    g.add_edge(1, 2, weight=2)
    g.add_edge(2, 3, weight=5)
    g.add_edge(3, 1, weight=0.25)
    return g

# no cycle - because its digraph
def crate_graph3():
    g = nx.DiGraph()
    g.add_node(1)
    g.add_node(2)
    g.add_node(3)
    g.add_node(4)
    g.add_edge(1, 2, weight=0.1)
    g.add_edge(2, 3, weight=0.5)
    g.add_edge(1, 3, weight=0.25)
    return g

# two cycles one with mul < 1 and one with mul >1
def crate_graph4():
    g = nx.DiGraph()
    g.add_node(1)
    g.add_node(2)
    g.add_node(3)
    g.add_node(4)
    g.add_node(5)
    g.add_node(6)
    g.add_node(7)
    g.add_edge(1, 2, weight=2)
    g.add_edge(2, 3, weight=5)
    g.add_edge(3, 1, weight=5)
    g.add_edge(5, 6, weight=0.25)
    g.add_edge(6, 7, weight=0.25)
    g.add_edge(7, 5, weight=0.25)
    return g

def crate_graph5():
    g = nx.DiGraph()
    g.add_node(1)
    g.add_node(2)
    g.add_node(3)
    g.add_node(4)
    g.add_node(5)
    g.add_node(6)
    g.add_node(7)
    g.add_edge(2, 3, weight=5)
    g.add_edge(3, 1, weight=5)
    g.add_edge(5, 6, weight=0.25)
    g.add_edge(6, 7, weight=0.25)
    g.add_edge(7, 1, weight=0.25)
    g.add_edge(1, 2, weight=0.25)
    g.add_edge(2, 5, weight=0.25)
    return g

def crate_graph6():
    g = nx.DiGraph()
    g.add_node(1)
    g.add_node(2)
    g.add_node(3)
    g.add_node(4)
    g.add_edge(1, 2, weight=1)
    g.add_edge(2, 3, weight=1)
    g.add_edge(3, 1, weight=1)
    return g

if __name__ == '__main__':
   print( find_loop(crate_graph1()))
   print(find_loop(crate_graph2()))
   (failures, tests) = doctest.testmod(report=True, optionflags=doctest.NORMALIZE_WHITESPACE + doctest.ELLIPSIS)
   print("{} failures, {} tests".format(failures, tests))

