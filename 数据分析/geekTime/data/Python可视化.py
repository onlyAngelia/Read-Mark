Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 05:52:31) 
[GCC 4.2.1 Compatible Apple LLVM 6.0 (clang-600.0.57)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> import numpy as np
>>> import pandas as pd
>>> import matplotlib.pyplot as plt
>>> import seaborn as sns
>>> N = 1000
>>> x = np.random.randn(N)
>>> y = np.random.randn(N)
>>> plt.scatter(x,y,marker='x')
<matplotlib.collections.PathCollection object at 0x1259f45c0>
>>> df = pd.DataFrame({'x':x,'y':y})
>>> sns.jointplot(x='x',y='y',data=df,kind='scatter')
<seaborn.axisgrid.JointGrid object at 0x1259f4a58>
>>> plt.show()
>>> x= [2010,2011,2012,2013,2014,2015,2016,2017,2018,2019]
>>> y = [3,5,6,23,12,34,56,21,30,19]
>>> plt.plot(x,y)
[<matplotlib.lines.Line2D object at 0x12ab966d8>]
>>> df = pd.DataFrame({'x':x,'y':y})
>>> sns.lineplot(x='x',y='y',data=df)
<matplotlib.axes._subplots.AxesSubplot object at 0x12741e860>
>>> plt.show()
>>> a = np.random.randn(100)
>>> s = pd.Series(a)
>>> plt.hist(s)
(array([ 2.,  6., 10., 15., 20., 21., 15.,  8.,  2.,  1.]), array([-2.48061854, -1.98099175, -1.48136497, -0.98173818, -0.48211139,
        0.0175154 ,  0.51714219,  1.01676898,  1.51639577,  2.01602256,
        2.51564935]), <a list of 10 Patch objects>)
>>> sns.distplot(s,kde=False)
<matplotlib.axes._subplots.AxesSubplot object at 0x12758c438>
>>> plt.show()
>>> x = ['cat1','cat2','cat3','cat4','cat5']
>>> y = [5,4,8,12,7]
>>> plt.bar(x,y)
<BarContainer object of 5 artists>
>>> plt.show()
>>> sns.barplot(x,y)
<matplotlib.axes._subplots.AxesSubplot object at 0x12741ea90>
>>> plt.show()
>>> data = np.random.normal(size=(10,4))
>>> labels = ['A','B','C','D']
>>> plt.boxplot(x,labels)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    plt.boxplot(x,labels)
  File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/matplotlib/pyplot.py", line 2496, in boxplot
    is not None else {}))
  File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/matplotlib/__init__.py", line 1810, in inner
    return func(ax, *args, **kwargs)
  File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/matplotlib/axes/_axes.py", line 3503, in boxplot
    labels=labels, autorange=autorange)
  File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/matplotlib/cbook/__init__.py", line 1215, in boxplot_stats
    stats['mean'] = np.mean(x)
  File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/numpy/core/fromnumeric.py", line 3118, in mean
    out=out, **kwargs)
  File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/numpy/core/_methods.py", line 75, in _mean
    ret = umr_sum(arr, axis, dtype, out, keepdims)
TypeError: cannot perform reduce with flexible type
>>> plt.boxplot(data,labels=labels)
{'whiskers': [<matplotlib.lines.Line2D object at 0x1276f9390>, <matplotlib.lines.Line2D object at 0x1276f96d8>, <matplotlib.lines.Line2D object at 0x127713ac8>, <matplotlib.lines.Line2D object at 0x127713e10>, <matplotlib.lines.Line2D object at 0x127729240>, <matplotlib.lines.Line2D object at 0x127729588>, <matplotlib.lines.Line2D object at 0x127733978>, <matplotlib.lines.Line2D object at 0x127733cc0>], 'caps': [<matplotlib.lines.Line2D object at 0x1276f9a20>, <matplotlib.lines.Line2D object at 0x1276f9d68>, <matplotlib.lines.Line2D object at 0x12771f198>, <matplotlib.lines.Line2D object at 0x12771f4e0>, <matplotlib.lines.Line2D object at 0x1277298d0>, <matplotlib.lines.Line2D object at 0x127729c18>, <matplotlib.lines.Line2D object at 0x12773e048>, <matplotlib.lines.Line2D object at 0x12773e390>], 'boxes': [<matplotlib.lines.Line2D object at 0x1276f9240>, <matplotlib.lines.Line2D object at 0x127713748>, <matplotlib.lines.Line2D object at 0x12771fe80>, <matplotlib.lines.Line2D object at 0x1277335f8>], 'medians': [<matplotlib.lines.Line2D object at 0x1277130f0>, <matplotlib.lines.Line2D object at 0x12771f828>, <matplotlib.lines.Line2D object at 0x127729f60>, <matplotlib.lines.Line2D object at 0x12773e6d8>], 'fliers': [<matplotlib.lines.Line2D object at 0x127713438>, <matplotlib.lines.Line2D object at 0x12771fb70>, <matplotlib.lines.Line2D object at 0x1277332e8>, <matplotlib.lines.Line2D object at 0x12773ea20>], 'means': []}
>>> df = pd.DataFrame(data,columns=labels)
>>> sns.boxplot(data=df)
<matplotlib.axes._subplots.AxesSubplot object at 0x126121c50>
>>> plt.show()
>>> nums = [25,37,33,37,6]
>>> labels = ['High-school','Bachelor','Master','Ph.d','Others']
>>> plt.ple(x=nums,labels=labels)
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    plt.ple(x=nums,labels=labels)
AttributeError: module 'matplotlib.pyplot' has no attribute 'ple'
>>> plt.pie(x=nums,labels=labels)
([<matplotlib.patches.Wedge object at 0x12610de80>, <matplotlib.patches.Wedge object at 0x12610df60>, <matplotlib.patches.Wedge object at 0x12610d6d8>, <matplotlib.patches.Wedge object at 0x1261079e8>, <matplotlib.patches.Wedge object at 0x1261076a0>], [Text(0.9266076783810917, 0.5927885039077627, 'High-school'), Text(-0.4382411947237755, 1.0089324334399594, 'Bachelor'), Text(-0.9986952352308595, -0.4610941629723568, 'Master'), Text(0.48370817836049246, -0.9879404831198964, 'Ph.d'), Text(1.0897545367529526, -0.14978334228597634, 'Others')])
>>> plt.show()
>>> flights = sns.load_dataset("flights")
>>> data = flights.pivot('year','month','passengers')
>>> sns.heatmap(data)
<matplotlib.axes._subplots.AxesSubplot object at 0x118de8a20>
>>> plt.show()
>>> #数据准备
>>> labels = np.array['空间', '想象', '抽象', '推理', '计算', '记忆']
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    labels = np.array['空间', '想象', '抽象', '推理', '计算', '记忆']
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> labels = np.array(['空间', '想象', '抽象', '推理', '计算', '记忆'])
>>> stats = [4,4,3,2,2,2]
>>> #画图准备数据，角度，状态值
>>> angles = np.linspace(0,2*np.pi , len(labels), endpoint=False)
>>> stats = np.concatenate((stats,stats[0]))
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    stats = np.concatenate((stats,stats[0]))
ValueError: all the input arrays must have same number of dimensions
>>> stats = np.concatenate((stats, [stats[0]]))
>>> angles = np.concatenate((angles,[angles[0]]))
>>> #画蜘蛛图
>>> fig = plt.figure()
>>> ax = fig.add_subplot(111,polar = True)
>>> ax.plot(angles, stats, 'o-', linewidth=2)
[<matplotlib.lines.Line2D object at 0x125a7e080>]
>>> font = FontProperties(fname=r"/System/Library/Fonts/STHeiti Light.ttc",size = 14)
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    font = FontProperties(fname=r"/System/Library/Fonts/STHeiti Light.ttc",size = 14)
NameError: name 'FontProperties' is not defined
>>> from matplotlib.font_manager import FontProperties
>>> font = FontProperties(fname=r"/System/Library/Fonts/STHeiti Light.ttc",size = 14)
>>> ax.set_thetagrids(angles *180/np.pi, labels, FontProperties=font)
(<a list of 14 Line2D ticklines objects>, <a list of 7 Text major ticklabel objects>)
>>> plt.show()
>>> #二元变量分布
>>> tips = sns.load_dataset("tips")
Traceback (most recent call last):
  File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/urllib/request.py", line 1318, in do_open
    encode_chunked=req.has_header('Transfer-encoding'))
  File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/http/client.py", line 1239, in request
    self._send_request(method, url, body, headers, encode_chunked)
  File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/http/client.py", line 1285, in _send_request
    self.endheaders(body, encode_chunked=encode_chunked)
  File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/http/client.py", line 1234, in endheaders
    self._send_output(message_body, encode_chunked=encode_chunked)
  File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/http/client.py", line 1026, in _send_output
    self.send(msg)
  File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/http/client.py", line 964, in send
    self.connect()
  File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/http/client.py", line 1400, in connect
    server_hostname=server_hostname)
  File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/ssl.py", line 407, in wrap_socket
    _context=self, _session=session)
  File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/ssl.py", line 814, in __init__
    self.do_handshake()
  File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/ssl.py", line 1068, in do_handshake
    self._sslobj.do_handshake()
  File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/ssl.py", line 689, in do_handshake
    self._sslobj.do_handshake()
ssl.SSLError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed (_ssl.c:833)

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    tips = sns.load_dataset("tips")
  File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/seaborn/utils.py", line 428, in load_dataset
    urlretrieve(full_path, cache_path)
  File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/urllib/request.py", line 248, in urlretrieve
    with contextlib.closing(urlopen(url, data)) as fp:
  File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/urllib/request.py", line 223, in urlopen
    return opener.open(url, data, timeout)
  File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/urllib/request.py", line 526, in open
    response = self._open(req, data)
  File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/urllib/request.py", line 544, in _open
    '_open', req)
  File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/urllib/request.py", line 504, in _call_chain
    result = func(*args)
  File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/urllib/request.py", line 1361, in https_open
    context=self._context, check_hostname=self._check_hostname)
  File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/urllib/request.py", line 1320, in do_open
    raise URLError(err)
urllib.error.URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed (_ssl.c:833)>
>>> import ssl
>>> ssl._create_default_https_context = ssl._create_unverified_context
>>> tips = sns.load_dataset("tips")
>>> print (tips.head(10))
   total_bill   tip     sex smoker  day    time  size
0       16.99  1.01  Female     No  Sun  Dinner     2
1       10.34  1.66    Male     No  Sun  Dinner     3
2       21.01  3.50    Male     No  Sun  Dinner     3
3       23.68  3.31    Male     No  Sun  Dinner     2
4       24.59  3.61  Female     No  Sun  Dinner     4
5       25.29  4.71    Male     No  Sun  Dinner     4
6        8.77  2.00    Male     No  Sun  Dinner     2
7       26.88  3.12    Male     No  Sun  Dinner     4
8       15.04  1.96    Male     No  Sun  Dinner     2
9       14.78  3.23    Male     No  Sun  Dinner     2
>>> sns.jointplot(x="total_bill", y = "tip", data = tips, kind='kde')
<seaborn.axisgrid.JointGrid object at 0x12742ebe0>
>>> sns.jointplot(x="total_bill",y="tip",data=tips,kind='hex')
<seaborn.axisgrid.JointGrid object at 0x1260d4780>
>>> plt.show()
>>> iris = sns.load_dataset('iris')
>>> sns.pairplot(iris)
<seaborn.axisgrid.PairGrid object at 0x131a0f898>
>>> plt.show()
>>> car_crashes = sns.load_dataset('car_crashes')
>>> print (car_crashes(10))
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    print (car_crashes(10))
TypeError: 'DataFrame' object is not callable
>>> print (car_crashes.columns)
Index(['total', 'speeding', 'alcohol', 'not_distracted', 'no_previous',
       'ins_premium', 'ins_losses', 'abbrev'],
      dtype='object')
>>> sns.jointplot(x='total',y='speeding',data=car_crashes,kind='scatter')
<seaborn.axisgrid.JointGrid object at 0x1259d7d68>
>>> plt.show()
>>> sns.jointplot(x='total',y='speeding',data=car_crashes,kind='kde')
<seaborn.axisgrid.JointGrid object at 0x129fe9ba8>
>>> plt.show()
>>> sns.jointplot(x='total',y='speeding',data=car_crashes,kind='hex')
<seaborn.axisgrid.JointGrid object at 0x12ff26eb8>
>>> plt.show()
>>> sns.jointplot(x='total',y='alcohol',data=car_crashes,kind='scatter')
<seaborn.axisgrid.JointGrid object at 0x131b19550>
>>> plt.show()
>>> sns.jointplot(x='total',y='alcohol',data=car_crashes,kind='kde')
<seaborn.axisgrid.JointGrid object at 0x129f5a630>
>>> plt.show()
>>> sns.jointplot(x='total',y='alcohol',data=car_crashes,kind='hex')
<seaborn.axisgrid.JointGrid object at 0x12605c630>
>>> plt.show()
>>> sns.pairplot(car_crashes)
<seaborn.axisgrid.PairGrid object at 0x125a9cdd8>
>>> plt.show()
>>> 
