# import numpy as np
import time


class TiMapTree():
    def __init__(self):
        self.tiseq = []
        self.tarseq = []
        self.zero = [0, 0]
        self.timapTree = []  # BFS queue
        self.moveseq = []  # movement sequence, [0,3]

    def conv_mvseq(self) -> str:
        matseq = 'UDLR'
        convseq = ''
        for i in range(self.moveseq):
            convseq += matseq[self.moveseq[i]]
        return convseq[:]

    def isEqual(self, xlist, ylist) -> bool:
        i: int = 0
        while i != 24:
            if (xlist[i] == ylist[i]):
                i += 1
                continue
            else:
                return False
        return True

    def input(self, str_file='./input.txt'):
        with open(str_file, 'r') as rf:
            self.tiseq = [int(line.strip('\n')) for line in rf.readlines()]
            self.update()

    def update(self):
        self.timapTree.append(self.tiseq[:])
        addr: int = self.tiseq.index(0)  # [0,len(list)-1]
        self.zero[0] = addr / 5  # [0,4]
        self.zero[1] = addr - 5 * self.zero[0]  # [0,4]

    def inputTarget(self, str_file='./target.txt'):
        with open(str_file, 'r') as f:
            self.tarseq = [int(line.strip('\n')) for line in f.readlines()]

    def move(self, arrow: int, zero_x: int, zero_y: int):
        """
            zero_x : [0,4]
            zero_y : [0,4]
            arrow  : [0,3]
        """
        temp = [zero_x,zero_y]
        if arrow==0 :
            temp[1] +=1
        elif arrow == 1 :
            temp[1] -= 1
        elif arrow == 2 :
            temp[0] -=1
        else:
            temp[0] +=1

        return

    def hrcs_func(self):
        return

    def output(self, exec_time,
               str_clrs='A', str_int='h1', str_out='_solution.txt', ):
        file_output = str_clrs + str_int + str_out
        with open(file_output, 'w') as wf:
            wf.write(str(exec_time) + 's\n')
            tmp_a = self.conv_mvseq()
            wf.write(tmp_a + '\n')
            wf.write(len(tmp_a))

    def print5step(self, i: int):
        print(str(i)+': about '+str(5*i)+' step\n')
        for i in range(25):
            print(self.tiseq[i])
            if (i+1)%5 == 0 :
                print('\n')
            else:
                print(' ')

    def exec(self):
        exec_begin = time.process_time()

        exec_end = time.process_time()
        total_exec = exec_end - exec_begin
        self.output(exec_time=total_exec)
