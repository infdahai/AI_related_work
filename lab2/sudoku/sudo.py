import time
from functools import lru_cache

class SudoMap():
    def __init__(self):
        with open('./input.txt', 'r') as rf:
            self.n, self.k = (int(x) for x in rf.readline().split())
            self.sudo_map: list = [[0 for i in range(self.n)] for j in range(self.n)]  # two-dimension
            self.cons_map: list = [[j + 1 for j in range(self.k)]
                                   for i in range(self.n * self.n)]  # two-dimension
            self.key_vale: dict = {}
            for i in range(self.n):
                val_list: list[str] = rf.readline().split()
                for j in range(self.n):
                    k = int(val_list[j])
                    self.update(i, j, k, 'self')
            for i in range(self.n * self.n):
                self.key_vale[i] = len(self.cons_map[i])
            self.key_value = sorted(self.key_vale.items(), key=lambda x: x[1])

    def __repr__(self) -> str:
        str_1: str = ''
        for list_i in self.sudo_map:
            for elem_j in list_i:
                str_1 += str(elem_j) + ' '
            str_1 += '\n'
        return str_1

    def write(self, time_cost: float) -> None:

        with open('./forcheck_solution.txt', 'w') as wf:
            wf.write('%fs\n' % time_cost)
            wf.write(self.__repr__())

    def add_constraint(self, i: int, j: int, val: int, str_map=''):
        """
           add new elem into sudoMap,then flush constraint Map. 
        """
        # row and column
        if str_map == 'self':
            map = self.cons_map
            dic = self.key_vale
        else:
            dic = self.key_vale.copy()
            map = self.cons_map.copy()
        row_index: int = self.n * i
        row_max: int = row_index + self.n
        while row_index < row_max:
            if self.sudo_map[i][j] == 0 and val in map[row_index]:
                map[row_index].remove(val)
                del dic[row_index]

            row_index += 1

        column_cursor: int = i
        column_max = self.n * self.n
        while column_cursor < column_max:
            if self.sudo_map[i][j] == 0 and val in map[column_cursor]:
                map[column_cursor].remove(val)
                del dic[column_cursor]
            column_cursor += self.n
        dic = sorted(dic.items(), key=lambda x: x[1])
        return map, dic

    def update(self, i: int, j: int, val: int, str_map='') -> None:
        self.sudo_map[i][j] = val
        self.add_constraint(i, j, val, str_map)

    def find_simple(self,str_map='') -> None:
        if str_map == 'self':
            map = self.sudo_map
            dic = self.key_vale
        else:
            dic = self.key_vale.copy()
            map = self.sudo_map.copy()
        for elemL_idnex, elemL in enumerate(self.cons_map):
            if len(elemL) == 1:
                i, j = divmod(elemL_idnex, self.n)
                if self.sudo_map[i][j] == 0:
                    self.sudo_map[i][j] = elemL[0]

    def search(self,dic:dict):
        self.find_simple()
        x_index:int = next(iter(dic))

    def run(self):
        start: float = time.process_time()
        print("\nExecuted now\n-------------\n")
        self.search(self.key_vale.copy())
        end: float = time.process_time()
        self.write(end - start)
        print("\nExecution done\n")


map = SudoMap()
map.run()
