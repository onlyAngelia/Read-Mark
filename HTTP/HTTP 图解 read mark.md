图解HTTP read mark

#1.请求报文构成
   
![](https://github.com/onlyAngelia/Read-Mark/blob/master/HTTP/_image/屏幕快照%202018-05-09%2013.00.01.png)

#2.响应报文构成
![](https://github.com/onlyAngelia/Read-Mark/blob/master/HTTP/_image/响应报文.png)        
 HTTP1.0/1.1 请求体部面向文本  所以才会有我们熟悉的XML、json、txt等传输

#3.HTTP 无状态协议，为此引入了Cookie

#4.HTTP方法

##GET： 获取资源

请求获取指定资源，若是文本直接返回，接收其它格式返回处理后结果；
安全、幂等(幂等是指同一个请求方法执行多次和仅执行一次的效果完全相同)；
可缓存；
报文主题没有任何语义（可打开Postman这样的工具，会发现body体不让设置）;
参数拼接在url中，明文传输;

##POST:传送实体

传送实体，根据报文主题对指定资源做出处理
不安全、不幂等；
不可缓存（大部分情况下）；
通过header请求,明文传输；

有关GET和POST的区别可以祥见该知乎讨论[GET和POST的区别](https://www.zhihu.com/question/28586791)


##PUT:

##DELETE:






