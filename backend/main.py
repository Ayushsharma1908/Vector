# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Any, Dict

app = FastAPI()

# Allow requests from React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/')
def read_root():
    return {'Ping': 'Pong'}


class PipelineData(BaseModel):
    nodes: List[Dict[str, Any]]
    edges: List[Dict[str, Any]]


def is_dag(nodes: List[Dict], edges: List[Dict]) -> bool:
    """
    Check if the graph formed by nodes and edges is a Directed Acyclic Graph.
    Uses DFS-based cycle detection.
    """
    # Build adjacency list
    node_ids = {node['id'] for node in nodes}
    graph = {node_id: [] for node_id in node_ids}

    for edge in edges:
        src = edge.get('source')
        tgt = edge.get('target')
        if src in graph and tgt in graph:
            graph[src].append(tgt)

    # DFS cycle detection
    # States: 0 = unvisited, 1 = visiting, 2 = visited
    state = {node_id: 0 for node_id in node_ids}

    def has_cycle(node):
        if state[node] == 1:
            return True   # back edge → cycle
        if state[node] == 2:
            return False  # already fully processed

        state[node] = 1  # mark as visiting
        for neighbor in graph[node]:
            if has_cycle(neighbor):
                return True
        state[node] = 2  # mark as visited
        return False

    for node_id in node_ids:
        if state[node_id] == 0:
            if has_cycle(node_id):
                return False  # cycle found → not a DAG

    return True


# main.py - add print statements
@app.post('/pipelines/parse')
def parse_pipeline(pipeline: PipelineData):
    print(f"Received request with {len(pipeline.nodes)} nodes and {len(pipeline.edges)} edges")
    print(f"Nodes: {pipeline.nodes}")
    print(f"Edges: {pipeline.edges}")
    
    num_nodes = len(pipeline.nodes)
    num_edges = len(pipeline.edges)
    dag = is_dag(pipeline.nodes, pipeline.edges)
    
    print(f"Returning: nodes={num_nodes}, edges={num_edges}, is_dag={dag}")
    
    return {
        'num_nodes': num_nodes,
        'num_edges': num_edges,
        'is_dag': dag,
    }