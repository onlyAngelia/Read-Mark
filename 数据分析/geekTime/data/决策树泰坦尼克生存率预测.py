import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report
from sklearn.model_selection import cross_val_score
from sklearn import tree
train_data = pd.read_csv('/Users/apple/Desktop/GitHubProject/Read mark/数据分析/geekTime/data/Titannic_Data_train.csv')
test_data = pd.read_csv('/Users/apple/Desktop/GitHubProject/Read mark/数据分析/geekTime/data/Titannic_Data_test.csv')
#了解数据表的基本情况
print (train_data.info())
print ('-' *30)
#了解数据表的统计情况
print (train_data.describe())
print ('-' *30)
#查看字符串类型的整体情况
print (train_data.describe(include=['O']))
print ('-' *30)
#使用head查看前几行数据
print (train_data.head())
print ('-' *30)
#使用tail查看后几行数据
print (train_data.tail())
#使用平均年龄填充年龄nan值
train_data['Age'].fillna(train_data['Age'].mean(), inplace=True)
test_data['Age'].fillna(test_data['Age'].mean(), inplace = True)
print (train_data['Embarked'].value_counts())
#使用登录最多的港口来进行填充港口nan缺失
train_data['Embarked'].fillna('S', inplace=True)
test_data['Embarked'].fillna('S', inplace=True)
#特征选择
features = ['Pclass','Sex','Age','SlibSp','Parch','Embarked']
train_features = train_data[features]
train_labels = train_data['Survived']
test_features = test_data[features]
devc = DictVectorizer(sparse=False)
train_features = devc.fit_transform(train_features.to_dict(orient='record'))
print (devc.feature_names_)
#构造ID3决策树
clf = DecisionTreeClassifier(criterion='entropy')
#决策树训练
clf.fit(train_features, train_labels)
test_features = devc.transform(test_features.to_dict(orient='record'))
#决策树预测
pred_labels = clf.predict(test_features)
#得到决策树准确率
acc_decision_tree = round(clf.score(train_features, train_labels),6)
print ('score准确率为%.4f' % acc_decision_tree)
#使用K折交叉验证 统计决策树准确率
print ('cross_val_score准确率为%.4lf' % np.mean(cross_val_score(clf, train_features,train_labels,cv=10)))
with open("jueceshu.dot",'w') as f:
    f = tree.export_graphviz(clf, out_file = f)
