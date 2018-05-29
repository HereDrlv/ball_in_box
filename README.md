

## config environment
conda install --file requirements.txt -y

pip install -e .

---

## 任务

在[-1,1]的方形区域内，给定若干个障碍点坐标，之后放入给定个数的圆

##### 限定条件

1. 圆之间不能相互重叠
2. 圆不能覆盖障碍点
3. 这些圆的总面积和最大.
4. 求得每个圆的圆心坐标及半径大小



## User Story

1. 作为一个用户，通过本算法，应该得到解决方阵投圆问题的解





## Tasks

1. 2~4个成员算法的设计，抽象出需要的类与方法
2. 1~2个组员，分配类与方法的编写
3. 1~2个先预备好测试用例，算法完成后进行算法的测试



## Test Cases

| 圆的个数（m） | 障碍物坐标                                    |
| :------ | :--------------------------------------- |
| 1       | 测试正常情况:随机生成十个在规定正方形内的点                   |
| 1       | 测试边界附近的情况:(0.99,0.99),(1,1)              |
| 1       | 测试边界外的情况:(2,2)                           |
| 1       | 综合测试:随机生成十个在规定正方形内的点;(0.99,0.99),(0.99,0),(1,1); |
| 1       | 没有障碍物                                    |
| 2       | 测试正常情况:随机生成十个在规定正方形内的点                   |
| 2       | 测试边界附近的情况:(0.99,0.99),(1,1)              |
| 2       | 测试边界外的情况:(2,2)                           |
| 2       | 综合测试:随机生成十个在规定正方形内的点;(0.99,0.99),(0.99,0),(1,1); |
| 2       | 没有障碍物                                    |
| 25      | 测试正常情况:随机生成十个在规定正方形内的点                   |
| 25      | 测试边界附近的情况:(0.99,0.99),(1,1)              |
| 25      | 测试边界外的情况:(2,2)                           |
| 25      | 综合测试:随机生成十个在规定正方形内的点;(0.99,0.99),(0.99,0),(1,1); |
| 25      | 没有障碍物                                    |
| 100     | 测试正常情况:随机生成十个在规定正方形内的点                   |
| 100     | 测试边界附近的情况:(0.99,0.99),(1,1)              |
| 100     | 测试边界外的情况:(2,2)                           |
| 100     | 综合测试:随机生成十个在规定正方形内的点;(0.99,0.99),(0.99,0),(1,1); |
| 100     | 没有障碍物                                    |
  
