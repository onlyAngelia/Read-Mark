[TOC]

# PageRank

为解决早起搜索引擎的缺陷，受论文影响力因子的启发，当一篇论文被引用的次数越多，证明这篇论文的影响力越大，Google创始人拉里·佩奇提出来PageRank算法。

##**PageRank算法原理**

**出链**：链出去的链接

**入链**：链进来的链接

**一个网页的影响力 = 所有入链集合的页面加权影响力之和**，公式：

​			$PR(u) = \sum\limits_{v\in B_u}\dfrac{PR(v)}{L(v)}$

u为待评估的页面，$B_u$为页面u的入链集合。针对集合中的任意页面v，它能给u带来影响力是其自身影响力PR(v)除以v页面的出链数量，即页面v把影响力PR(v)平均分配给来它的出链，这样统计所有给u带来链接的页面v，得到的总和就是网页u的影响力，即PR(u)

假设ABCD四个网页的出链和如链数分别如下：

| 网页 |            出链数            |              入链数              |
| :--: | :--------------------------: | :------------------------------: |
|  A   | 3: $A\to B ,A\to C, A \to D$ | 2: $A\leftarrow B,A\leftarrow D$ |
|  B   |      2: $B\to A,B\to D$      | 2:$B\leftarrow A, B\leftarrow D$ |
|  C   |          1:$C\to A$          | 2:$C\leftarrow A,C\leftarrow D$  |
|  D   |      2:$D\to B,D\to C$       | 2:$D\leftarrow A, D\leftarrow B$ |

针对ABCD四个网页的链接网页情况，得到转移矩阵M:

​			$M = \begin{bmatrix} 0 & \dfrac{1}{2} &1&0\\ \dfrac{1}{3} &0&0&\dfrac{1}{2}\\ \dfrac{1}{3}&0&0&\dfrac{1}{2}\\ \dfrac{1}{3}&\dfrac{1}{2}&0&0\\ \end{bmatrix}$

假设ABCD四个页面的初始影响力都相同，(一般初始影响力都设为1/N)，即

​			$w_0 =\begin{bmatrix}  \dfrac{1}{4}\\ \dfrac{1}{4} \\ \dfrac{1}{4}\\ \dfrac{1}{4} \end{bmatrix} $

当进行第一次转移之后，各页面影响力变为：

$w_1=M\times w_0=\begin{bmatrix} 0 & \dfrac{1}{2} &1&0\\ \dfrac{1}{3} &0&0&\dfrac{1}{2}\\ \dfrac{1}{3}&0&0&\dfrac{1}{2}\\ \dfrac{1}{3}&\dfrac{1}{2}&0&0\\ \end{bmatrix} \begin{bmatrix}  \dfrac{1}{4}\\ \dfrac{1}{4} \\ \dfrac{1}{4}\\ \dfrac{1}{4} \end{bmatrix} = \begin{bmatrix} \dfrac{9}{24}\\ \dfrac{5}{24}\\ \dfrac{5}{24}\\ \dfrac{5}{24}\\ \end{bmatrix}$

然后再用转移矩阵$M\times w_1$得到$w_2$，直到第n次迭代后$w_n$的影响力不再发生变化，收敛到一个固定矩阵。这个时候就是N个页面最平衡状态下的影响力。权重越大，代表PR越高。这就是PageRank的计算过程。

实际情况中，会存在：

1.**等级泄露（Rank Leak）**: 如果网页只有入链，会造成其它网页的PR值为0

2.**等级沉没(Rank Sink)**: 如果网页只有出链，会造成这个网页的PR值为0

为解决上述问题，拉里·佩奇 提出来**PageRank随机浏览模式**。

定义来阻尼因子d，而1-d则代表来用户是不是通过跳转链接的方式来访问网页的，公式为：

$PR(u) = \dfrac{1-d}{N} + d\sum\limits_{v\in B_u} \dfrac{PR(v)}{L(v)}$

最终PageRank随机浏览模型可以收敛到固定值，得到一个稳定正常的PR值。

##**PageRank 的应用**

1.社交影响力评估

2.个人职场影响力

3.公司影响力

4.行业影响力

5.文学作品影响力

6.图书推荐影响力

其它可以应用的方面也还有很多

