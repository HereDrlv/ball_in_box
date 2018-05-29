
  <div id="readme" class="readme blob instapaper_body">
    <article class="markdown-body entry-content" itemprop="text"><h1><a id="user-content-ball_in_box" class="anchor" aria-hidden="true" href="#ball_in_box"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>ball_in_box</h1>
<h2><a id="user-content-config-environment" class="anchor" aria-hidden="true" href="#config-environment"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>config environment</h2>
<p>conda  env create --file environment.yml</p>
<p>conda install --file requirements.txt -y</p>
<p>pip install -e .</p>
<hr>
<h2><a id="user-content-任务" class="anchor" aria-hidden="true" href="#任务"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>任务</h2>
<p>在[-1,1]的方形区域内，给定若干个障碍点坐标，之后放入给定个数的圆</p>
<h5><a id="user-content-限定条件" class="anchor" aria-hidden="true" href="#限定条件"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>限定条件</h5>
<ol>
<li>圆之间不能相互重叠</li>
<li>圆不能覆盖障碍点</li>
<li>这些圆的总面积和最大.</li>
<li>求得每个圆的圆心坐标及半径大小</li>
</ol>
<h2
2a3e
><a id="user-content-user-story" class="anchor" aria-hidden="true" href="#user-story"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>User Story</h2>
<ol>
<li>作为一个用户，通过本算法，应该得到解决方阵投圆问题的解</li>
</ol>
<h2><a id="user-content-tasks" class="anchor" aria-hidden="true" href="#tasks"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Tasks</h2>
<ol>
<li>2~4个成员算法的设计，抽象出需要的类与方法</li>
<li>1~2个组员，分配类与方法的编写</li>
<li>1~2个先预备好测试用例，算法完成后进行算法的测试</li>
</ol>
<h2><a id="user-content-test-cases" class="anchor" aria-hidden="true" href="#test-cases"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Test Cases</h2>
<table>
<thead>
<tr>
<th align="left">圆的个数（m）</th>
<th align="left">障碍物坐标</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">1</td>
<td align="left">测试正常情况:随机生成十个在规定正方形内的点</td>
</tr>
<tr>
<td align="left">1</td>
<td align="left">测试边界附近的情况:(0.99,0.99),(1,1)</td>
</tr>
<tr>
<td align="left">1</td>
<td align="left">测试边界外的情况:(2,2)</td>
</tr>
<tr>
<td align="left">1</td>
<td align="left">综合测试:随机生成十个在规定正方形内的点;(0.99,0.99),(0.99,0),(1,1);</td>
</tr>
<tr>
<td align="left">1</td>
<td align="left">没有障碍物</td>
</tr>
<tr>
<td align="left">2</td>
<td align="left">测试正常情况:随机生成十个在规定正方形内的点</td>
</tr>
<tr>
<td align="left">2</td>
<td align="left">测试边界附近的情况:(0.99,0.99),(1,1)</td>
</tr>
<tr>
<td align="left">2</td>
<td align="left">测试边界外的情况:(2,2)</td>
</tr>
<tr>
<td align="left">2</td>
<td align="left">综合测试:随机生成十个在规定正方形内的点;(0.99,0.99),(0.99,0),(1,1);</td>
</tr>
<tr>
<td align="left">2</td>
<td align="left">没有障碍物</td>
</tr>
<tr>
<td align="left">25</td>
<td align="left">测试正常情况:随机生成十个在规定正方形内的点</td>
</tr>
<tr>
<td align="left">25</td>
<td align="left">测试边界附近的情况:(0.99,0.99),(1,1)</td>
</tr>
<tr>
<td align="left">25</td>
<td align="left">测试边界外的情况:(2,2)</td>
</tr>
<tr>
<td align="left">25</td>
<td align="left">综合测试:随机生成十个在规定正方形内的点;(0.99,0.99),(0.99,0),(1,1);</td>
</tr>
<tr>
<td align="left">25</td>
<td align="left">没有障碍物</td>
</tr>
<tr>
<td align="left">100</td>
<td align="left">测试正常情况:随机生成十个在规定正方形内的点</td>
</tr>
<tr>
<td align="left">100</td>
<td align="left">测试边界附近的情况:(0.99,0.99),(1,1)</td>
</tr>
<tr>
<td align="left">100</td>
<td align="left">测试边界外的情况:(2,2)</td>
</tr>
<tr>
<td align="left">100</td>
<td align="left">综合测试:随机生成十个在规定正方形内的点;(0.99,0.99),(0.99,0),(1,1);</td>
</tr>
<tr>
<td align="left">100</td>
<td align="left">没有障碍物</td>
</tr></tbody></table>
</article>
  </div>
## config environment

  </div>

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
  <button type="button" data-facebox="#jump-to-line" data-facebox-class="linejump" data-hotkey="l" class="d-none">

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
