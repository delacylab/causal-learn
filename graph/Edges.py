#!/usr/bin/env python3
from graph.Edge import Edge
from graph.Endpoint import Endpoint

class Edges:

    # constructs a new bidirected edge from node_a to node_b <->
    def bidirected_edge(self, node_a, node_b):

        edge = Edge(node_a, node_b, Endpoint.ARROW, Endpoint.arrow)
        return edge

    # constructs a new directed edge from node_a to node_b -->
    def directed_edge(self, node_a, node_b):

        edge = Edge(node_a, node_b, Endpoint.TAIL, Endpoint.ARROW)
        return edge

    # constructs a new partially oriented edge from node_a to node_b o->
    def partially_oriented_edge(self, node_a, node_b):

        edge = Edge(node_a, node_b, Endpoint.CIRCLE, Endpoint.ARROW)
        return edge

    # constructs a new undirected edge from node_a to node_b --
    def undirected_edge(self, node_a, node_b):

        edge = Edge(node_a, node_b, Endpoint.TAIL, Endpoint.TAIL)
        return edge

    # return true iff an edge is a bidrected edge <->
    def is_bidirected_edge(self, edge):
        return edge.get_endpoint1() is Endpoint.ARROW and edge.get_endpoint2() is Endpoint.ARROW

    # return true iff the given edge is a directed edge -->
    def is_directed_edge(self, edge):
        if edge.get_endpoint1() is Endpoint.TAIL:
            if edge.get_endpoint2() is Endpoint.ARROW:
                return True
        else:
            if edge.get_endpoint2() is Endpoint.TAIL:
                if edge.get_endpoint1() is Endpoint.ARROW:
                    return True
            else:
                return False

    # return true iff the given edge is a partially oriented edge o->
    def is_partially_oriented_edge(self, edge):
        if edge.get_endpoint1() is Endpoint.CIRCLE:
            if edge.get_endpoint2() is Endpoint.ARROW:
                return True
        else:
            if edge.get_endpoint2() is Endpoint.CIRCLE:
                if edge.get_endpoint1() is Endpoint.ARROW:
                    return True
            else:
                return False

    # return true iff some edge is an undirected edge --
    def is_undirected_edge(self, edge):
        pass