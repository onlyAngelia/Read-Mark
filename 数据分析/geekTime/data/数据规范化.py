Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 05:52:31) 
[GCC 4.2.1 Compatible Apple LLVM 6.0 (clang-600.0.57)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> from sklearn  import preprocessing
>>> import numpy as np
>>> #初始化数据
>>> x = np.array([[0.,-3,1],[3,1,2],[0,1,-1]])
>>> #将数据进行[0,1]规范化
>>> min_max_scaler = preprocessing.MinMaxScaler()
>>> print (min_max_scaler)
MinMaxScaler(copy=True, feature_range=(0, 1))
>>> minmax_x = min_max_scaler.fit_transform(x)
>>> print (minmax_x)
[[0.         0.         0.66666667]
 [1.         1.         1.        ]
 [0.         1.         0.        ]]
>>> x=np.array([[0.,-3.,1.],[3.,1.,2.],[0.,1.,-1.]])
>>> scaled_x=preprocessing.scale(x)
>>> print (scaled_x)
[[-0.70710678 -1.41421356  0.26726124]
 [ 1.41421356  0.70710678  1.06904497]
 [-0.70710678  0.70710678 -1.33630621]]
>>> #小数定标规范化
>>> j = np.ceil(np.log10(np.max(abs(x))))
>>> print (j)
1.0
>>> scaled_x = x/(10**j)
>>> print (scaled_x)
[[ 0.  -0.3  0.1]
 [ 0.3  0.1  0.2]
 [ 0.   0.1 -0.1]]
>>> 
