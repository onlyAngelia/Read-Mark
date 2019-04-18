[TOC]

#**SVM**

SVM：Support Vector Machine，支持向量机。在机器学习中是有监督学习模型，可以帮助模式识别、分类以及回归分析。

##**有监督学习&无监督学习**

告诉机器，给它一些数据，这部分数据一些是数据集合A，一部分是属于集合B，然后让机器去把数据往集合A和集合B里去划分，这是有监督学习；同样的数据给机器，只是告诉它去做划分和归类，这是无监督学习，类似于孩子的放养。  

##**超平面**

物体有线性规律摆放，可以用一条直线划分，若物体摆放完全无规律，则需要用曲线来划分。在二维平面上很难让不规律的物体线性划分，若将物体放在更高维度的三维平面划分，则会出现一个水平切面恰好把物体按线性规律划分，该平面就是超平面。

##**SVM工作原理**

SVM就是帮助找到一个超平面，这个超平面能将不同的样本划分开，同时使得样本集中的点到这个分类超平面的最小距离(分类间隔)最大化。

**分类间隔**：

我们的分类环境不是在二维平面中的，而是在多维空间中，这样直线 C 就变成了决策面 C。在保证决策面不变，且分类不产生错误的情况下，我们可以移动决策面 C，直到产生两个极限的位置。极限的位置是指，如果越过了这个位置，就会产生分类错误。两个极限位置 A 和 B 之间的分界线 C 就是最优决策面。**极限位置到最优决策面  之间的距离，就是分类间隔**。 (英文名叫margin) 

如果我们转动这个最优决策面，你会发现可能存在多个最优决策面，它们都能把数据集正确分开，这些最优决策面的分类间隔可能是不同的，而那个拥有“最大间隔”（max margin）的决策面就是 SVM 要找的最优解。

 目标是找到所有分类间隔中最大的那个值对应的超平面。在数学上，这是一个凸优化问题(凸优化就是关于求凸集中的凸函数最小化的问题)。 中间求解过程会用到拉格朗日乘子、KKT(Karush-Kuhn-Tucker)条件。

##**有关超平面距离公式**

**点到超平面的距离公式**：

 					**$g(x) = w^Tx + b, w,x\in R^n​$**

w、x 是 n 维空间里的向量，其中 x 是函数变量；w 是法向量。法向量这里指的是垂直于平面的直线所表示的向量，它决定了超平面的方向。

**支持向量**：距离分类超平面最近的样本点。

如果确定了支持向量也就确定了这个超平面。所以支持向量决定了分类间隔到底是多少，而在最大间隔以外的样本点，其实对分类都没有意义。

**样本集到超平面的距离公式**:

​						$d_i = \dfrac{|wx_i + b|}{||w||}$

其中||w||为超平面的范数，di 的公式可以用解析几何知识进行推导



## **硬间隔、软间隔、核函数**

**硬间隔**：表示得到的最大分类间隔即超平面 能完美的划分数据，不存在划分错误的情况，即零误差
**软间隔**：表示得到的最大分类间隔，没有达到完美的程度，对数据划分存在一定的误差
**核函数**：在数据分布无法用线性函数来表示的时候，需要对数据进行划分的标准变成来非线性的，这个时候就需要用到一种函数名叫核函数，核函数要做的工作是将原来的映射关系在更高维度的空间重新映射，使得新的映射关系变得线性可分。

常用的核函数有线性核、多项式核、高斯核、拉普拉斯核、sigmoid核，或者是这些核函数的组合。

## **线性SVM、非线性SVM**

实际中，数据多少会存在一些噪点。这个时候需要使用软间隔SVM(近线性可分)。

对于非线性分布的数据采用非线性SVM，在非线性SVM中，核函数是影响SVM最大的变量。

##**SVM解决多分类问题**

1.**一对多法**

针对K个分类，需要训练K个分类器，分类速度快

缺点：训练速度慢，造成样本不对称、新类增加需要重新对分类器进行构造。

2.**一对一法**

在任意两类样本之间构造一个SVM，这样针对K类的样本，会有C(k,2)类分类器

优点：新增一类，不需要重新训练所有的SVM；训练单个SVM模型的时候，训练速度快。

缺点：分类器个数与K的平方成正比，K较大时，训练核测试的时间会比较慢。

##**SVM实战：如何进行乳腺癌检测**

###**非线性SVM：SVC检测**

```python
*- coding: utf-8 -*-
#乳腺癌诊断分类
import pandas as  pd
import  matplotlib.pyplot as  plt
import  seaborn as  sns
from sklearn.model_selection import  train_test_split
from sklearn import  svm
from sklearn import metrics
from sklearn.preprocessing import  StandardScaler

#加载数据集
path = '/Users/apple/Desktop/GitHubProject/Read mark/数据分析/geekTime/data/'
data = pd.read_csv(path + 'breast_cancer/data.csv')

#数据探索
pd.set_option('display.max_columns', None)
print(data.columns)
print(data.head(5))
print(data.describe())

#特征字段分成三组
features_mean = list(data.columns[2:12])
features_se = list(data.columns[12:22])
features_worst = list(data.columns[22:32])

#数据清洗
#删除无用的ID列
data.drop('id', axis= 1, inplace=True)
#将B良性替换为0，M恶性替换为1
data['diagnosis']=data['diagnosis'].map({'M':1,'B':0})

#将肿瘤诊断结果可视化
sns.countplot(data['diagnosis'],label='Count')
plt.show()
#用热力图呈现features——mean字段之间的相关性
corr = data[features_mean].corr()
plt.figure(figsize=(14,14))
#annot = True显示每个方格的数据
sns.heatmap(corr, annot=True)
plt.show()

#特征选择
features_remain = ['radius_mean','texture_mean','smoothness_mean','compactness_mean',
                   'symmetry_mean','fractal_dimension_mean']
#抽取30%的数据作为测试集，其余作为训练集
train, test  =  train_test_split(data, test_size= 0.3)
#抽取特征选择的数值作为训练和测试数据
train_x = train[features_remain]
train_y = train['diagnosis']
test_x = test[features_remain]
test_y = test['diagnosis']

#采用Z-SCORE规范化数据，保证每个特征维度的数据均值为0，方差为1
ss = StandardScaler()
train_x = ss.fit_transform(train_x)
test_x = ss.transform(test_x)

#创建SVM分类器
model = svm.SVC()
#用训练集做训练
model.fit(train_x,train_y)
#用测试集做预测
prediction = model.predict(test_x)
print('准确率:', metrics.accuracy_score(prediction, test_y))
```

训练结果：

```py

准确率: 0.9239766081871345

```

### **线性SVM：LinearSVC检测**

```python
import  pandas as  pd
import  matplotlib.pyplot as  plt
import  seaborn as  sns
from sklearn.model_selection import  train_test_split
from sklearn import  svm
from sklearn import  metrics
from sklearn.preprocessing import  StandardScaler

#导入数据
path = '/Users/apple/Desktop/GitHubProject/Read mark/数据分析/geekTime/data/'
data = pd.read_csv(path + 'breast_cancer/data.csv')

#数据探索
pd.set_option('display.max_columns', None)
print(data.columns)
print(data.head(5))
print(data.describe())

#将特征字段进行分组
features_mean = list(data.columns[2:12])
features_se = list(data.columns[12:22])
features_worst = list(data.columns[22:32])

#数据清洗
#删除ID列
data.drop('id',axis=1,inplace=True)
#将良性B替换为0，将恶性替换为1
data['diagnosis'] = data['diagnosis'].map({'B':0,'M':1})

#将肿瘤诊断结果可视化
sns.countplot(data['diagnosis'],label='count')
plt.show()
#计算相关系数
corr = data[features_mean].corr()
plt.figure(figsize=(14,14))

#用热力图呈现相关性，显示每个方格的数据
sns.heatmap(corr,annot=True)
plt.show()

#特征选择，选择所有的mean数据
feature_remain = ['radius_mean', 'texture_mean', 'perimeter_mean',
       'area_mean', 'smoothness_mean', 'compactness_mean', 'concavity_mean',
       'concave points_mean', 'symmetry_mean', 'fractal_dimension_mean']

#抽取30%特征选择作为测试数据，其余作为训练集
train,test = train_test_split(data,test_size=0.3)
#抽取特征选择作为训练和测试数据
train_data = train[feature_remain]
train_result = train['diagnosis']
test_data = test[feature_remain]
test_result = test['diagnosis']

#创建SVM分类器
model = svm.LinearSVC()
#用训练集做训练
model.fit(train_data,train_result)
#用测试集做预测
prediction = model.predict(test_data)
#准确率
print('准确率:', metrics.accuracy_score(prediction,test_result))

#规范化数据，再预估准确率
z_score = StandardScaler()
train_data = z_score.fit_transform(train_data)
test_data = z_score.transform(test_data)
#用新数据做训练
new_model = svm.LinearSVC()
new_model.fit(train_data,train_result)
#重新预测
new_prediction = new_model.predict(test_data)
#准确率
print('准确率:',metrics.accuracy_score(new_prediction,test_result))
```

输出结果：

```python
准确率: 0.7953216374269005
准确率: 0.935672514619883
```

经过比较可以看出，特征选择值越多，对训练结果的准确度越高；数据越规范，训练结果准确度越高