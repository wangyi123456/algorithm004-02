#37数独 解法，，，92ms  ， 原作者，最好成绩为88ms 。如果直接用heapq ，有机会尝试一下，
from heapq import heappush, heappop
class PriorityQueue:
    def __init__(self, iterable=[]):
        self.heap = []
        for value in iterable:
            heappush(self.heap, (0, value))

    def add(self, value, priority=0):
        heappush(self.heap, (priority, value))

    def pop(self):
        priority, value = heappop(self.heap)
        return value

    def __len__(self):
        return len(self.heap)

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        row = [set(range(1, 10)) for _ in range(9)]  # 行剩余可用数字
        col = [set(range(1, 10)) for _ in range(9)]  # 列剩余可用数字
        block = [set(range(1, 10)) for _ in range(9)]  # 块剩余可用数字

        empty = []  # 收集需填数位置
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':  # 更新可用数字
                    val = int(board[i][j])
                    row[i].remove(val)
                    col[j].remove(val)
                    block[(i // 3)*3 + j // 3].remove(val)
                else:
                    empty.append((i, j))

        you=PriorityQueue()
        for i,j in empty:
            b = (i // 3)*3 + j // 3
            ans=row[i] & col[j] & block[b]#计算它，保存它
            pp=len(ans)
            #if pp==1:                          -------------这里多次尝试，但都是耗时到了500ms ，放弃。
               # t=ans.pop()
               # board[i][j]=str(t)  #直接写上，不进入回溯了。
            #else:
            you.add((i,j,b),pp)           #进入堆，进行重新优先级排序
        ee=[]
        while len(you):
            i, j,b=you.pop()
            ee.append((i,j,b))        #-----把 b 放进去，是优化思想

        def backtrack(iter=0):
            if iter == len(ee):  #变化为 ee
                return True
            i, j,b = ee[iter]  #变化为 ee
            for val in row[i] & col[j] & block[b]:
                row[i].remove(val)
                col[j].remove(val)
                block[b].remove(val)
                board[i][j] = str(val)
                if backtrack(iter+1):
                    return True
                row[i].add(val)  # 回溯
                col[j].add(val)
                block[b].add(val)
            return False
        backtrack()
#作者：yybeta   -----在下面

'''
class Solution:   
    def solveSudoku(self, board: List[List[str]]) -> None:
           row = [set(range(1, 10)) for _ in range(9)]  # 行剩余可用数字
           col = [set(range(1, 10)) for _ in range(9)]  # 列剩余可用数字
           block = [set(range(1, 10)) for _ in range(9)]  # 块剩余可用数字
    
           empty = []  # 收集需填数位置
           for i in range(9):
               for j in range(9):
                   if board[i][j] != '.':  # 更新可用数字
                       val = int(board[i][j])
                       row[i].remove(val)
                       col[j].remove(val)
                       block[(i // 3)*3 + j // 3].remove(val)
                   else:
                       empty.append((i, j))
    
           def backtrack(iter=0):
               if iter == len(empty):  # 处理完empty代表找到了答案
                   return True
               i, j = empty[iter]
               b = (i // 3)*3 + j // 3
               for val in row[i] & col[j] & block[b]:
                   row[i].remove(val)
                   col[j].remove(val)
                   block[b].remove(val)
                   board[i][j] = str(val)
                   if backtrack(iter+1):
                       return True
                   row[i].add(val)  # 回溯
                   col[j].add(val)
                   block[b].add(val)
               return False
           backtrack()
     '''
