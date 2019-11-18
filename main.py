from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
from pathfinding.finder.breadth_first import BreadthFirstFinder
from pathfinding.finder.dijkstra import DijkstraFinder
from colorama import Fore, Back, Style
from colorama import init
import sys
import numpy as np

def apply_style(s, style):
    s = style + s + Style.RESET_ALL
    return s

def color_print(s):
    for c in s:
        if(c == 'x'):
            c = apply_style(c, Fore.RED)
        elif(c == ('S' or 's')):
            c = apply_style(c, Fore.GREEN)
        elif(c == ('E' or 'e')):
            c = apply_style(c, Fore.BLUE)
        elif(c == '#'):
            c = apply_style(c, Fore.YELLOW)
        sys.stdout.write(c)
        sys.stdout.flush()

init()

matrix = np.random.randint(9,size=(10,10))

grid = Grid(matrix=matrix)

idxStart =  np.random.randint(0, high=9, size=2)
start = grid.node(idxStart[0], idxStart[1])
idxEnd =  np.random.randint(0, high=9, size=2)
end = grid.node(idxEnd[0], idxEnd[1])

astar_finder = AStarFinder(diagonal_movement=DiagonalMovement.always)
path, runs = astar_finder.find_path(start, end, grid)

print("Legenda: \n")
print(Fore.GREEN + 'S' + ": Inicio\n")
print(Fore.BLUE + 'E' + ": Fim\n")
print(Fore.RED + 'x' + ": Caminho\n")
print(Fore.YELLOW + '#' + ": Obstaculo\n" + Style.RESET_ALL)


print("A*:")
print('Operações:', runs, 'Tamanho:', len(path))
color_print(grid.grid_str(path=path, start=start, end=end, show_weight=True))
print('\n' + "---//----//-----------//----------//---------//-----")

grid2 = Grid(matrix=matrix)

start = grid2.node(idxStart[0], idxStart[1])
end = grid2.node(idxEnd[0], idxEnd[1])

bfs_finder = BreadthFirstFinder(diagonal_movement=DiagonalMovement.always)
path, runs = bfs_finder.find_path(start, end, grid2)
print("Busca em Largura:")
print('Operações:',runs, 'Tamanho:', len(path))
color_print(grid2.grid_str(path=path, start=start, end=end, show_weight=True))
print('\n' + "---//----//-----------//----------//---------//-----")

grid3 = Grid(matrix=matrix)
start = grid3.node(idxStart[0], idxStart[1])
end = grid3.node(idxEnd[0], idxEnd[1])

dijkstra_finder = DijkstraFinder(diagonal_movement=True)
path, runs = dijkstra_finder.find_path(start, end, grid3)
print("Dijkstra:")
print('Operações:',runs, 'Tamanho:', len(path))
color_print(grid3.grid_str(path=path, start=start, end=end, show_weight=True))
