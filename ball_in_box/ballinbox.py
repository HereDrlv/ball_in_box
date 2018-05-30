
from itertools import combinations
from scipy.optimize import fsolve
from copy import copy
from pdb import set_trace

INFT = float(10**10)

#定义圆的类 新的圆会作为下一个圆的约束
class Bound(object):
    def __init__(self, x, y, r):
        self.x, self.y, self.r = x, y, r

    #判断圆是否满足某个圆的约束
    def fit(self, another_bound):
        if another_bound.x == INFT:
            return self.x + self.r <= 1.0
        elif another_bound.x == - INFT:
            return self.x - self.r >= -1.0
        elif another_bound.y == INFT:
            return self.y + self.r <= 1.0
        elif another_bound.y == - INFT:
            return self.y - self.r >= -1.0
        else:
            return (self.r + another_bound.r)**2 <= (self.x - another_bound.x)**2 + (self.y - another_bound.y)**2
        #最后一项为恰好相切的情况

    #判断圆是否满足所有圆的约束
    def fit_all(self, bounds):
        for i in bounds:
            if not self.fit(i):
                return False
        return True


# 初始正方形的四条边看作不同约束的圆
bound_set0 = [
    Bound(-INFT, 0.0, INFT),
    Bound(INFT, 0.0, INFT),
    Bound(0.0, -INFT, INFT),
    Bound(0.0, INFT, INFT),
]
circles = []

# 输入所有约束list 查找符合的最大圆
def find(bound_set):
    new_bound_set = bound_set
    max_r = 0
    for selected_3_bound in list(combinations(bound_set, 3)):
        a = []
        for i in range (4):
            a.append(solve(selected_3_bound,i))
            new_bound = Bound(a[i][0],a[i][1],a[i][2])
            if new_bound.fit_all(new_bound_set) and new_bound.r > max_r:
                max_r = new_bound.r
                max_bound = new_bound
    new_bound_set.append(max_bound)   #每次新的最大圆会添加到约束list中
    bd = [max_bound.x, max_bound.y, max_bound.r]
    circles.append(bd)
    return max_bound


# 输入3个约束圆，在这三个约束下找到唯一最大圆
def solve(three_bounds ,i):
    def fi(solution,bound):
        if bound.x == INFT :
            return solution[0] + solution[2] - 1.0
        elif bound.x == - INFT:
            return solution[0] - solution[2] + 1.0
        elif bound.y == INFT:
            return solution[1] + solution[2] - 1.0
        elif bound.y == - INFT:
            return solution[1] - solution[2] + 1.0
        else:
            return -(solution[2] + bound.r)**2 + (solution[0] - bound.x)**2 + (solution[1] - bound.y)**2

    f = lambda x :[
            fi(x,three_bounds[0]),
            fi(x,three_bounds[1]),
            fi(x,three_bounds[2])
        ]
    if(i == 0):
        return fsolve(f, [1.0, 1.0, 0.0])
    elif(i == 1):
        return fsolve(f, [-1.0, -1.0, 0.0])
    elif (i == 2):
        return fsolve(f, [-1.0, 1.0, 0.0])
    elif (i == 3):
        return fsolve(f, [1.0, -1.0, 0.0])
# 设置多个初始迭代点

# 测试接口
def ball_in_box(m, blockers): 
    for x in blockers:
        b = Bound(x[0],x[1],0)
        bound_set0.append(b)
    while m > 0:
        find(bound_set0) 
        m-=1
    return circles
