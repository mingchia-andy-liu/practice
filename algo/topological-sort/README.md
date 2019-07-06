# Topological sort

## Table of Content

## Fundamental

A `topological sort` of a **`directed graph`** is a **`linear`** ordering of its vertices such that for every directed edge `uv` from vertex `u` to vertex `v`, `u` comes before `v` in the ordering.


A `topological ordering` is possible if and only if the graph has **NO** directed cycles, that is, if it is a **`directed acyclic graph`** (DAG).


Any DAG has _at least_ one topological ordering and can be constructed in `O(N)` linear time.

## Idea

The idea is to use DFS and add the node to the ordering if only if all dependencies adjacency nodes are added.
