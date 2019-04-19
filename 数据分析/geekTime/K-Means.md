[TOC]

# K-Means

K-Means ：非监督学习，解决的是聚类问题。K代表K个类，Means代表中心，确定K类的中心点，最终找到这些中心点，完成聚类。

##**K-Means工作原理**

1.选取K个点作为初始的类中心点，一般从数据集中随机抽取

2.将每个点分配到最近的类中心点，这样形成K个类，然后重新计算每个类的中心点

3.重复第二步，直到类不再发生变化，或者可以设置最大迭代次数，这样即使类中心发生变化，只要达到最大迭代次数就会结束。

##**K-Means实践（一）:球队聚类**

skearn.cluster中提供来K-Means聚类库，包括K-Means在内，其一共提供来9种聚类方法，比如Mean-shift，DBSCAN，Spectralclustering等。

```python
#导入数据
path ='/Users/apple/Desktop/GitHubProject/Read mark/数据分析/geekTime/data/'
data = pd.read_csv(path + 'foot_team_data.csv', encoding='gbk')
train_data = data[['2019年国际排名','2018世界杯','2015亚洲杯']]
df = pd.DataFrame(train_data)
kmeans = KMeans(n_clusters=3)

#规范化数据
min_max_scaler = preprocessing.MinMaxScaler()
train_data = min_max_scaler.fit_transform(train_data)

#聚合
kmeans.fit_transform(train_data)
#预测
predict = kmeans.predict(train_data)

#合并聚类结果，插入到原数据中
result = pd.concat((data,pd.DataFrame(predict)),axis=1)
result.rename({0:u'聚类'},axis=1,inplace=True)
print(result)
```

输出结果

```python
 国家  2019年国际排名  2018世界杯  2015亚洲杯  聚类
0       中国         73       40        7   0
1       日本         60       15        5   2
2       韩国         61       19        2   2
3       伊朗         34       18        6   2
4       沙特         67       26       10   2
5      伊拉克         91       40        4   0
6      卡塔尔        101       40       13   1
7      阿联酋         81       40        6   0
8   乌兹别克斯坦         88       40        8   0
9       泰国        122       40       17   1
10      越南        102       50       17   1
11      阿曼         87       50       12   1
12      巴林        116       50       11   1
13      朝鲜        110       50       14   1
14      印尼        164       50       17   1
15      澳洲         40       30        1   2
16     叙利亚         76       40       17   1
17      约旦        118       50        9   1
18     科威特        160       50       15   1
19    巴勒斯坦         96       50       16   1
```

**K-Means参数**：

1.n_clusters: K值大小

2.Max_iter: 最大迭代次数

3.n_init：初始化中心点的运算次数，默认是10

4.init:初始值选择方式，默认k-means++方式，可以自己指定，

也可以采用random完全随机方式

5.algorithm: 实现算法，有'auto' '、full'、 'elkan'三种，默认auto，auto会根据数据特点选择是full还是elkan

## K-Means实践(二)：根据图像通道数分割图像

```python
import numpy as  np
import PIL.Image as  image
from sklearn.cluster import KMeans
from sklearn import preprocessing

#加载图像，并对数据进行规范化
path ='/Users/apple/Desktop/GitHubProject/Read mark/数据分析/geekTime/data/'
def load_data(file_path):
    f = open(file_path,'rb')
    data = []
    #得到图像像素值
    img = image.open(f)
    #得到图像尺寸
    width, height = img.size
    for x in  range(width):
        for y in range(height):
            #得到点（x，y）的通道值
            c1,c2,c3 = img.getpixel((x,y))
            data.append([c1,c2,c3])
    f.close()
    #采用Min-Max规范化
    min_max_scaler = preprocessing.MinMaxScaler()
    data = min_max_scaler.fit_transform(data)
    return np.mat(data),width,height

#加载图像，得到规范化结果img，以及图像尺寸
img,width,height = load_data(path + 'weixin.jpg')

#用k-means对图像进行2聚类
kmeans = KMeans(n_clusters=2)
kmeans.fit_transform(img)
predict = kmeans.predict(img)

#将图像聚类结果，转化成图像尺寸的矩阵
result = predict.reshape([width,height])
#创建新图像，保存图像聚类的结果，并设置不同灰度值
pic_mark = image.new('L',(width,height))
for x in  range(width):
    for y in range(height):
        pic_mark.putpixel((x,y),int(256/(result[x][y]+1))-1)
pic_mark.save(path +'weixin_alpha.jpg','JPEG')
```

最终得到的图片结果为:

![](data/weixin_alpha.jpg)

##K-Means实战(三)：根据色值分割图像**

