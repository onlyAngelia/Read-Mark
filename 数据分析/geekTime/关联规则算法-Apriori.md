[TOC]

# 关联规则算法

关联规则是由Agrawal等人于1993年提出，1994年提出来基于关联规则的Apriori算法。

关联规则算法分为两种：广度优先算法、深度优先算法

广度优先算法的代表算法有：Apriori、AprioriFid、AprioriHybrid，其中AprioriHybrid效率更高。

深度优先算法的代表算法有：FP-growth、Eclat和H-Mine。

##**关联规则概念**

**支持度**：$\dfrac{商品或商品组合出现次数}{总次数}$

**置信度**：A发生的情况下，B发生的概率

**提升度**：A出现的情况 ，是否会对B出现的概率有所提升

​		$提升度(A\to B) = \dfrac{置信度(A\to B)}{支持度(B)}$

​        $提升度(A\to B)>1$:代表有提升

​		$提升度(A\to B)=1$：无提升，也没有下降

​		$提升度(A\to B)< 1$:代表有下降

**频繁项集**：支持度大于等于最小支持度(Min Support)阈值的项集。最小支持度是认为设定的，项集英文叫做itemset，可以是单个商品也可以是商品的组合。

**闭频繁项集**：支持度大于最小设置阈值，具有超集，并且超集中项集个数大于自身项集的项集个数。

**极大频繁项集**：支持度大于最小设置阈值，并且没有超项集。

## **频繁模式挖掘种类**

**根据完全性质分类**：频繁项集完全集、闭频繁项集、极大频繁项集、被约束的频繁项集、近似的频繁项集

接近匹配的频繁项集、最频繁的K个项集。

**根据抽象层分类**：单层关联规则、多层关联规则

**根据数据维度分类**：一维关联规则、多维关联规则

**根据处理值类型分类**：布尔关联规则、量化关联规则

## **Apriori算法原理**

1.K-1,计算K项集的支持度

2.筛选掉小于最小支持度的项集

3.如果项集为空，则对应K-1项集的结果为最终结果。

否则K=K+1，重复以上步骤

## **FP-Growth算法:基于Apriori**

Apriori算法缺点：

1.产生大量后选集，浪计算空间

2.每次计算重新扫描数据集计算支持度，浪费计算时间

FP-Growth算法原理：

1.创建项头表(item header table)

2.构造FP树

3.通过FP树挖掘频繁项集

创建项头表流程是扫描数据集，将满足最小支持度的单个项按照支持度从高到低排序，项头表包括项目、支持度以及该项在FP树中的链表。

FP树根节点为NULL节点。再次扫描数据集，按照从高到低顺序进行创建节点，节点如果存在就将计数count+1，如果不存在就进行创建，同时更新项头表的链接。

**条件模式基**：以要挖掘的节点为叶子节点，自底向上求出FP子树，然后将FP子树的祖先节点设置为叶子结点之和。

## **Apriori算法实践**

1.超市消费记录关联

```python
from efficient_apriori import apriori
data = [['牛奶','面包','尿布'],
           ['可乐','面包', '尿布', '啤酒'],
           ['牛奶','尿布', '啤酒', '鸡蛋'],
           ['面包', '牛奶', '尿布', '啤酒'],
           ['面包', '牛奶', '尿布', '可乐']]
items,rules = apriori(data,min_confidence=1,min_support=0.5)
print(items)
print(rules)
```

输出结果:

```python
{1: {('啤酒',): 3, ('尿布',): 5, ('牛奶',): 4, ('面包',): 4}, 2: {('啤酒', '尿布'): 3, ('尿布', '牛奶'): 4, ('尿布', '面包'): 4, ('牛奶', '面包'): 3}, 3: {('尿布', '牛奶', '面包'): 3}}
[{啤酒} -> {尿布}, {牛奶} -> {尿布}, {面包} -> {尿布}, {牛奶, 面包} -> {尿布}]
```

2.导演如何选择演员

```python
#-*- coding: utf-8 -*-
from efficient_apriori import apriori
from lxml import etree
from selenium import webdriver
import time
import csv

#第一步：数据爬取
driver = webdriver.Chrome('/Users/apple/Downloads/chromedriver')
#设置要下载的导演，数据集
director = u'张艺谋'
#写CSV文件
path =  '/Users/apple/Desktop/GitHubProject/Read mark/数据分析/geekTime/data/'
file_name = path + director +'.csv'
base_url = 'https://movie.douban.com/subject_search?search_text='+director+'&cat=1002&start='
out = open(file_name,'w',newline='',encoding='utf-8-sig')
csv_write = csv.writer(out,dialect='excel')
flags=[]

# 下载指定页面资源
def download(request_url):
    driver.get(request_url)
    time.sleep(1)
    html = driver.find_element_by_xpath('//*').get_attribute('outerHTML')
    html = etree.HTML(html)
    #设置电影名称，导演演员的XPATH
    movie_lists = html.xpath("/html/body/div[@id='wrapper']/div[@id='root']/div[1]//div[@class='item-root']/div[@class='detail']/div[@class='title']/a[@class='title-text']")
    name_lists = html.xpath("/html/body/div[@id='wrapper']/div[@id='root']/div[1]//div[@class='item-root']/div[@class='detail']/div[@class='meta abstract_2']")
    #获取返回的数据个数
    num = len(movie_lists)
    if num > 15:
        movie_lists = movie_lists[1:]
        name_lists = name_lists[1:]
    for(movie, name_list) in zip(movie_lists,name_lists):
        if name_list.text is None:
            continue
        print(name_list.text)
        names=name_list.text.split('/')
        if names[0].strip() == director and movie.text not in flags:
            names[0] = movie.text
            flags.append(movie.text)
            csv_write.writerow(names)
    print('该页下载成功', num)

    if num >= 14:
        return  True
    else:
        return False
# 开始Id为0，每页增加15
start = 0
while start < 10000:
    request_url = base_url + str(start)
    #下载数据，并返回是否有下一页
    flag = download(request_url)
    if flag:
        start = start +15
    else:
        break

out.closed
print('下载完成')
```

下载成功之后进行关联分析，因演员的支持度不高，所以min_support设置太高会无结果

```python
#第二步：用Apriori算法进行关联分析
#数据加载
director = '张艺谋'
#写CSV文件
path = '/Users/apple/Desktop/GitHubProject/Read mark/数据分析/geekTime/data/'
file_name = path + director +'.csv'
print(file_name)
lists = csv.reader(open(file_name, 'r', encoding='utf-8-sig'))
data =[]
for names in lists:
    name_new = []
    for name in names:
        name_new.append(name.strip())
    if len(name_new[1:]) >0:
        data.append(name_new[1:])
print('data--',data)

#挖掘频繁项集合关联规则
items,rules = apriori(data,min_support=0.05,min_confidence=1)
print(items)
print(rules)
```

输出结果：

```python
{1: {('倪大红',): 3, ('傅彪',): 2, ('刘佩琦',): 2, ('刘德华',): 2, ('姜文',): 2, ('孙红雷',): 3, ('巩俐',): 9, ('李保田',): 3, ('李曼',): 2, ('李雪健',): 5, ('杨凤良',): 2, ('牛犇',): 2, ('章子怡',): 3, ('葛优',): 3, ('赵本山',): 2, ('郭涛',): 2, ('闫妮',): 2, ('陈道明',): 2}, 2: {('倪大红', '巩俐'): 2, ('傅彪', '李雪健'): 2, ('刘佩琦', '巩俐'): 2, ('孙红雷', '赵本山'): 2, ('巩俐', '李保田'): 2, ('巩俐', '杨凤良'): 2, ('巩俐', '葛优'): 2, ('巩俐', '郭涛'): 2, ('李保田', '李雪健'): 2}}
[{傅彪} -> {李雪健}, {刘佩琦} -> {巩俐}, {赵本山} -> {孙红雷}, {杨凤良} -> {巩俐}, {郭涛} -> {巩俐}]
```

