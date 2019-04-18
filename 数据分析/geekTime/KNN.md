[TOC]

#**KNN**

KNN：K-Nearest Neighbor

##**KNN工作原理**

KNN原理分为三步：

1.计算待分类物体与其他物体之间的距离；

2.统计距离最近的 K 个邻居；

3.对于 K 个最近的邻居，它们属于哪个分类最多，待分类物体就属该类

## **K值选择**

K值选择较小，会产生过拟合，K值选择较大，会产生欠拟合。实践中，K值的选取采用交叉验证的方式。

## **距离计算方式**

距离计算有五种，前三种比较常见

1.欧氏距离-欧几里得距离

​        	计算公式：

​				$d =\sqrt[]{ (x_1-x_2)^2 + (y_1-y_2)^2}​$

2.曼哈顿距离

​		计算公式：

​				$d= |x_1-x_2| + [y_1-y_2]​$

3.闵可夫斯基距离

​		计算公式:

​				$d = \sqrt[p]{\sum\limits_{i=1}^n|x_i-y_i|^p}$

​           当p=1 ，就是曼哈顿距离，当p=2，就是欧氏距离，当p$\rightarrow\infty$,	   就是切比雪夫距离。

4.切比雪夫距离

​	两个点坐标数值差的绝对值的最大值，用数学表示就是：					$max(|x_1-x_2|,|y_1-y_2|)$

5.余弦距离

​           余弦计算两个向量的夹角，对绝对值不感兴趣。在兴趣相关性比较上，角度关系比距离的绝对值更重要，蔚县距离可以用于衡量用户对内容兴趣的区分度。

##**KD树**

KD树：K-Dimensional ，是一种每个节点都是k维数值点的二叉树。可以减少计算距离次数，提升KNN的搜索效率。

##**用KNN做回归**

对于一个新点，找出k个最近邻居，将他们的属性加权评均赋给该点。

## KNN实践-手写数字进行识别

```python
from sklearn.model_selection import  train_test_split
from sklearn.metrics import  accuracy_score
from sklearn.datasets import  load_digits
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import MultinomialNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as  plt
# import ssl
#
# ssl._create_default_https_context = ssl._create_unverified_context

#加载数据
digits = load_digits()
data = digits.data
#数据探索
print(data.shape)
print(digits.images[0])
print(digits.target[0])
plt.gray()
plt.imshow(digits.images[0])
plt.show()

#分割数据，将25%的数据作为测试集，其余作为训练集
train_data,test_data,train_result,test_result = train_test_split(data,digits.target,test_size=0.25,random_state=33)
#采用Z-Score规范化
score = StandardScaler()
train_score_data = score.fit_transform(train_data)
test_score_data = score.transform(test_data)

#创建KNN分类器
knn = KNeighborsClassifier()
knn.fit(train_score_data,train_result)
predict_result = knn.predict(test_score_data)
print('knn默认k值为5 准确率:%.4lf' %accuracy_score(predict_result,test_result))

#创建K值为200的KNN分类器
kvalue_twenty_knn = KNeighborsClassifier(n_neighbors=200)
kvalue_twenty_knn.fit(train_score_data,train_result)
print('knn的k值为200的准确率:%.4lf' %accuracy_score(kvalue_twenty_knn.predict(test_score_data),test_result))

#创建svm分类器
svm = SVC()
svm.fit(train_score_data,train_result)
spredict_result = svm.predict(test_score_data)
print('SVM分类准确率:%.4lf' %accuracy_score(spredict_result,test_result))

#创建高斯朴素贝叶斯分类器
clf = GaussianNB()
clf.fit(train_score_data, train_result)
gspredict_result = clf.predict(test_score_data)
print('高斯朴素贝叶斯准确率:%.4lf' %accuracy_score(gspredict_result,test_result))

#CART决策树和多项式朴素贝叶斯只支持离散数据，所以进行Min-Max规范化处理
min_max_scaler = MinMaxScaler()
train_mm_data = min_max_scaler.fit_transform(train_data)
test_mm_data = min_max_scaler.transform(test_data)

#创建多项式朴素贝叶斯分类器
mlf = MultinomialNB()
mlf.fit(train_mm_data,train_result)
mpredict_result = mlf.predict(test_mm_data)
print('多项式朴素贝叶斯分类器准确率:%.4lf' %accuracy_score(mpredict_result,test_result))

#创建CART决策树
cart = DecisionTreeClassifier()
cart.fit(train_mm_data,train_result)
cpredict_result = cart.predict(test_mm_data)
print('CART决策树准确率:%.4lf' %accuracy_score(cpredict_result,test_result))

#创建高斯朴素贝叶斯分类器
clf = GaussianNB()
clf.fit(train_mm_data, train_result)
gspredict_result = clf.predict(test_mm_data)
print('高斯朴素贝叶斯准确率:%.4lf' %accuracy_score(gspredict_result,test_result))
```

输出结果:

```python
knn默认k值为5 准确率:0.9756
knn的k值为200的准确率:0.8489
SVM分类准确率:0.9867
高斯朴素贝叶斯准确率:0.7778
多项式朴素贝叶斯分类器准确率:0.8844
CART决策树准确率:0.8400
高斯朴素贝叶斯准确率:0.8111
```

