# Vectorshift
---
# Visual Pipeline Builder

A interactive pipeline builder application that allows users to create, connect, 
and analyze custom workflow nodes through an intuitive visual interface.

## Features

- **Visual Node Editor**: Drag-and-drop interface for building pipelines
- **Custom Node System**: Extensible architecture for creating different node types
- **Real-time Validation**: Automatic DAG (Directed Acyclic Graph) detection
- **Smart Text Nodes**: Dynamic resizing and variable handle generation
- **Pipeline Analysis**: One-click analysis of node/edge counts and graph properties

## Tech Stack

- **Frontend**: React, React Flow, Zustand (state management)
- **Backend**: FastAPI (Python)
- **Styling**: Custom CSS with modern design system

## Architecture

The application follows a component-based architecture with:
- Abstract node classes for consistent behavior
- Real-time state synchronization
- RESTful API integration for pipeline analysis
- Responsive design principles

## Getting Started

### Prerequisites
- Node.js (v14+)
- Python (3.8+)
- npm or yarn

### Installation

1. Clone the repository
```bash
git clone https://github.com/Ayushsharma1908/Vector.git
cd Vectorshift
