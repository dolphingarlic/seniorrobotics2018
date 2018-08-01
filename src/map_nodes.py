from .node import Node

A1 = Node("A1", "", "B1", "", "B2")
B1 = Node("B1", "", "", "C1", "A1")
B2 = Node("B2", "", "A1", "C4", "")
C1 = Node("C1", "B1", "", "D1", "C2")
C2 = Node("C2", "G", "C1", "R", "C3")
C3 = Node("C3", "B", "C2", "Y", "C4")
C4 = Node("C4", "B2", "C3", "D3", "")
D1 = Node("D1", "C1", "", "D1", "D2")
D2 = Node("D2", "", "D1", "", "D3")
D3 = Node("D3", "C4", "D2", "E3", "")
E1 = Node("E1", "D1", "", "", "E2")
E2 = Node("E2", "", "E1", "F4", "E3")
E3 = Node("E3", "D3", "E2", "", "")
F1 = Node("F1", "", "", "1", "F2")
F2 = Node("F2", "", "F1", "2", "F3")
F3 = Node("F3", "", "F2", "3", "F4")
F4 = Node("F4", "E2", "F3", "", "F5")
F5 = Node("F5", "", "F4", "4", "F6")
F6 = Node("F6", "", "F5", "5", "F7")
F7 = Node("F7", "F6", "", "6", "")

nodes = [A1, B1, B2, C1, C2, C3, C4, D1, D2, D3, E1, E2, E3, F1, F2, F3, F4, F5, F7]


A1C4 = [A1, B2, C4]
D2C2 = [D2, D1, C1, C2]
D2C3 = [D2, D3, C4, C3]
C3E1 = [C3, C2, C1, D1, E1]
C2E1 = [C2, C1, D1, E1]
E3D2 = [E3, D3, D2]
E3A1 = [E3, D3, C4, B2, A1]