[TOC]

#EM聚类

EM:Expectation Maximization，最大期望算法。

算法过程分为两个步骤：

Expectation，期望步骤：初始化参数$\to$观察预期

Maximization，最大化步骤：重新估计参数$\to$ 初始化参数

##**EM算法工作原理**

EM的工作原理就是求解最大思然估计，通过观测样本，找出样本的模型参数。

最大似然：Maximum Likelihood ，通过已知结果，估计参数

通过旧参数来计算隐藏变量，然后通过得到的隐藏变量的结果重新估计参数，知道参数不再发生变化，得到想要的结果。参数的衡量标准是通过概率来计算，这点与K-Means不同。

##**EM聚类工作原理**

较 K-Means 算法，EM 聚类更加灵活

 K-Means 通过距离来区分样本，每个样本只能属于一个分类，称之为是**硬聚类算法**。

 EM 聚类通过概率求解样本，实际上每个样本都有一定的概率和每个聚类相关，叫做**软聚类算法**。

EM算法相当于一个框架，可以采用不同的模型来进行聚类，比如**GMM(高斯混合模型)**或**HMM（隐马尔科夫模型）**来进行聚类。很多K-Means解决不了的问题，EM聚类可以解决。

GMM是通过概率密度来进行聚类，聚成的类符合高斯分布，即正态分布。

HMM用到来马尔可夫过程，过程中通过状态转移矩阵来计算状态转移的概率。HMM在自然语言处理核语音识别领域中有广泛的应用。

##**EM聚类实践**

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import csv
from sklearn.mixture import GaussianMixture
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import calinski_harabaz_score

#数据加载
path = '/Users/apple/Desktop/GitHubProject/Read mark/数据分析/geekTime/data/'
original_data = pd.read_csv(path + 'heros.csv',encoding='gb18030')
features = [u'最大生命',u'生命成长',u'初始生命',u'最大法力', u'法力成长',u'初始法力',u'最高物攻',u'物攻成长',
            u'初始物攻',u'最大物防',u'物防成长',u'初始物防', u'最大每5秒回血', u'每5秒回血成长', u'初始每5秒回血',
            u'最大每5秒回蓝', u'每5秒回蓝成长', u'初始每5秒回蓝', u'最大攻速', u'攻击范围']
data = original_data[features]

#可视化分析
plt.rcParams['font.sans-serif']=['SimHei'] #正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #正常显示负号
#热力图呈现相关性
corr = data[features].corr()
plt.figure(figsize=(14,14))
#显示每个方格的数据
sns.heatmap(corr, annot=True)
plt.show()

#相关性大的属性属性保留一个，对属性进行降维
features_remain = [u'最大生命', u'初始生命', u'最大法力', u'最高物攻', u'初始物攻', u'最大物防', u'初始物防',
                   u'最大每5秒回血', u'最大每5秒回蓝', u'初始每5秒回蓝', u'最大攻速', u'攻击范围']
data = original_data[features_remain]
data[u'最大攻速']=data[u'最大攻速'].apply(lambda x:float(x.strip('%'))/100)
data[u'攻击范围']=data[u'攻击范围'].map({'远程':1,'近战':0})
#Z-Score规划数据
scaler = StandardScaler()
data = scaler.fit_transform(data)

#构造GMM聚类
gmm = GaussianMixture(n_components=30,covariance_type='full')
predic = gmm.fit_predict(data)
print(predic)

#将分组结果输出到csv文件
original_data.insert(0,'分组',predic)
original_data.to_csv(path+'heros_out.csv', index=False,sep=',')
print(calinski_harabaz_score(data,predic))
```

输出结果为：

```python
[25 11  9 20  3  3 14  9  0 11 16 11 20 23 17 16 29  0 10  8 21 22  8 22
 22 22  8  6 27 26 23  4 15 27 26  4 27  7 19 24 15 27 27  4 27 24 11 19
 11 27  5 12 10  1  1 25 12  2 28  3 12 10 13 25 18  2  2  2  6]
22.180175615890516
```



GMM构建参数：

1.n_components:高斯混合模型的个数，聚类的个数，默认值为1

2.covariance_type：协方差类型，共有四种

​				covariance_type = full :代表完全协方差，即元素都不为0

​				covariance_type=tied：代表相同的完全协方差

​				covariance_type=diag:代表对角协方差，即对焦不为0

​				covariance_type=spherical：代表球面协方差，非对角为0

3.max_iter:代表最大迭代次数，默认为100

