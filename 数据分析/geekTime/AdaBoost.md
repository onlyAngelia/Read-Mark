[TOC]

# AdaBoost

AdaBoost:Adaptive Boosting，自适应提升算法。是分类算法中的集成算法。

集成算法有两种模式：投票选举(bagging)、再学习(boosting)

投票选举模式：做决定时，让K个模型分别进行分类，然后选择出现次数最多的类作为最终分类结果。

再学习模式：把K个分类器（弱分类器）进行加权融合，形成一个新的分类器(强分类器)

## **AdaBoost工作原理**

AdaBoost算法通过训练多个弱分类器，将它们组成一个强分类器。强分类器是由一系列的弱分类器根据不同的权重组合而成。

假设弱分类器为$G_i(x)$，它在强分类器中的权重$\alpha_i$,得出强分类器f(x):

​			 	$f(x)=\sum\limits_{i=1}^n \alpha_i G_i(x)​$

若弱分类器分类效果好，权重增大，如果弱分类器分类效果一般，权重应该降低，权重决定于弱分类器对样本的分类错误率。

 			$ \alpha_i = \dfrac{1}{2}\log^{\dfrac{1-e_i}{e_i}}$

通过改变样本的数据分布选择最优的弱分类器。AdaBoost 会判断每次训练的样本是否正确分类，对于正确正确分类的样本，降低它的权重，对于被错误分类的样本，增加它的权重。再基于上一次得到的分类准确率，来确定这次训练样本中每个样本的权重。然后将修改过权重的新数据集传递给下一层的分类器进行训练。

可以用 $D_{k+1}$ 代表第 k+1 轮训练中，样本的权重集合，其中 $W_{k+1},1$ 代表第 k+1 轮中第一个样本的权重,以此类推 $W_{k+1},N$代表第k+1轮中第N个样本的权重；

​		$D_{k+1} = (w_{k+1,1},W_{k+1,2}…,W_{k+1,N})$

第k+1轮中的样本权重，是根据该样本在第K轮的权重以及第k个分类器的准确率而定，

​		$W_{k+1,i} = \dfrac{W_k,i}{Z_k} \times e^{-\alpha _k y_i G_k(x_i)},i = 1,2,…,N$

AdaBoost算法是一个框架，可以指定任意的分类器，通常可以采用CART分类器作为弱分类器。



## **AdaBoost对房价进行预测**

```python
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.datasets import load_boston
from sklearn.ensemble import AdaBoostRegressor
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

#加载数据
data = load_boston()
#分割数据
train_data,test_data,train_feature,test_feature = train_test_split(data.data,data.target,test_size=0.25,random_state=33)
#使用AdaBoost回归模型
regressor = AdaBoostRegressor()
regressor.fit(train_data,train_feature)
predict = regressor.predict(test_data)
mse = mean_squared_error(test_feature,predict)
print('房价预测结果',predict)
print('均方误差=',round(mse,2))
```

输出结果为：

```python
房价预测结果 [20.71470588 10.3        12.87708333 17.66346154 25.83823529 22.65714286
 29.15384615 18.49642857 27.4137931  21.03333333 30.45979381 31.14545455
 10.71142857 24.81532258 13.33283582 25.67371429 17.66346154 16.49545455
 27.21962617 24.935      17.81904762 18.31734694 18.14064516 19.47735849
 31.62093023 18.31734694 23.77777778 25.67371429 10.71142857 29.28253968
 17.81904762 25.77624309 10.3        21.31023622 26.38041667 29.28253968
 26.34090909 12.51111111 13.33283582 26.02621359 14.79462366 11.87634409
 28.38010471 17.81904762 27.07490196 19.04123711 18.14064516 20.23611111
 26.34090909 19.23125    17.66346154 34.31320755 16.18947368 17.69848485
 25.77624309 20.91       26.02621359 17.38125    24.935      24.56330645
 19.21496063 16.31860465 44.21052632 21.29295775 17.02727273 26.38041667
 26.34090909 12.51111111 18.74473684 27.71223404 24.56330645 18.59268293
 17.81904762 26.83609023 20.46923077 44.21052632 16.03133333 10.85918367
 16.90333333 24.81532258 20.88907563 15.44166667 12.13134328 25.49166667
 20.88907563 21.29295775 48.11923077 16.90333333 44.65625    30.7037037
 27.21962617 18.66285714 18.74473684 17.8369863  14.79462366 34.0125
 24.935      23.3        18.65714286 18.31734694 15.79135802 20.51495327
 27.07490196 26.34090909 11.33571429 16.18641975 11.33571429 27.07490196
 11.33571429 26.38041667 49.18285714 12.51111111 18.00526316 25.77624309
 29.28253968 24.81532258 20.97857143 20.97857143 27.21962617 20.81836735
 19.66363636 17.8369863  11.33571429 20.91       23.3        16.90333333
 43.5       ]
均方误差= 18.4
```

使用决策树和KNN回归模型

```python
from sklearn.tree import DecisionTreeRegressor
from sklearn.neighbors import KNeighborsRegressor
#使用决策树回归模型
treeregressor = DecisionTreeRegressor()
treeregressor.fit(train_data,train_feature)
pred_y = treeregressor.predict(test_data)
mse_y = mean_squared_error(test_feature,pred_y)
print('决策树均方误差=', round(mse_y,2))
#使用KNN回归模型
knnregressor = KNeighborsRegressor()
knnregressor.fit(train_data,train_feature)
pred_z = knnregressor.predict(test_data)
mse_z = mean_squared_error(test_feature, pred_z)
print('KNN均方误差=', round(mse_z,2))
```

输出结果：

```python
决策树均方误差= 37.65
KNN均方误差= 27.87
```

**AdaBoost参数意义**:

AdaBoostClassifier创建过程：

1.base_estimator:代表弱分类器，默认决策树

2.n_estimators: 算法的最大迭代次数，分类器个数，默认是50

3.learning_rate:代表学习率，取值在0-1之间，默认是1.0。如果学习率较小，需要比较多的迭代次数才能收敛，所以learning_rate核n_estimators两个参数要一起调整。

4.alborithm：采用哪种boosting算法，有两种：SAMME、SAMME.R。默认是SAMME.R

5.random_state:代表随机数种子的设置，默认是None

AdaBoostRegressor创建过程：

基本同上，但没有algorithm这个参数。

loss：代表损失函数的设置，一共有三种选择：

​		linear：线性

​		square：平方

​		exponential：指数



三种回归正确率分析：

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.metrics import zero_one_loss
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import  AdaBoostClassifier
# 设置 AdaBoost 迭代次数
n_estimators=200
# 使用
X,y=datasets.make_hastie_10_2(n_samples=12000,random_state=1)
# 从 12000 个数据中取前 2000 行作为测试集，其余作为训练集
test_x, test_y = X[2000:],y[2000:]
train_x, train_y = X[:2000],y[:2000]
# 弱分类器
dt_stump = DecisionTreeClassifier(max_depth=1,min_samples_leaf=1)
dt_stump.fit(train_x, train_y)
dt_stump_err = 1.0-dt_stump.score(test_x, test_y)
# 决策树分类器
dt = DecisionTreeClassifier()
dt.fit(train_x,  train_y)
dt_err = 1.0-dt.score(test_x, test_y)
# AdaBoost 分类器
ada = AdaBoostClassifier(base_estimator=dt_stump,n_estimators=n_estimators)
ada.fit(train_x,  train_y)
# 三个分类器的错误率可视化
fig = plt.figure()
# 设置 plt 正确显示中文
plt.rcParams['font.sans-serif'] = ['SimHei']
ax = fig.add_subplot(111)
ax.plot([1,n_estimators],[dt_stump_err]*2, 'k-', label=u'决策树弱分类器 错误率')
ax.plot([1,n_estimators],[dt_err]*2,'k--', label=u'决策树模型 错误率')
ada_err = np.zeros((n_estimators,))
# 遍历每次迭代的结果 i 为迭代次数, pred_y 为预测结果
for i,pred_y in enumerate(ada.staged_predict(test_x)):
     # 统计错误率
    ada_err[i]=zero_one_loss(pred_y, test_y)
# 绘制每次迭代的 AdaBoost 错误率 
ax.plot(np.arange(n_estimators)+1, ada_err, label='AdaBoost Test 错误率', color='orange')
ax.set_xlabel('迭代次数')
ax.set_ylabel('错误率')
leg=ax.legend(loc='upper right',fancybox=True)
plt.show()
```

