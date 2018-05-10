图解HTTP read mark

#1.请求报文构成
   
![](https://github.com/onlyAngelia/Read-Mark/blob/master/HTTP/_image/请求报文.png)

#2.响应报文构成
![](https://github.com/onlyAngelia/Read-Mark/blob/master/HTTP/_image/响应报文.png)        
 HTTP1.0/1.1 报文面向文本  所以才会有我们熟悉的XML、json、txt等传输

#3.HTTP 无状态协议，为此引入了Cookie

#4.HTTP方法

##GET： 获取资源

请求获取指定资源，若是文本直接返回，接收其它格式返回处理后结果；
安全、幂等(幂等是指同一个请求方法执行多次和仅执行一次的效果完全相同)；
可缓存；
报文主题没有任何语义（可打开Postman这样的工具，会发现body体不让设置）;
参数拼接在url中，明文传输;
![](https://github.com/onlyAngelia/Read-Mark/blob/master/HTTP/_image/GET请求.png)
##POST:传送实体

传送实体，根据报文主题对指定资源做出处理
不安全、不幂等；
不可缓存（大部分情况下）；
通过header请求,明文传输；
![](https://github.com/onlyAngelia/Read-Mark/blob/master/HTTP/_image/POST请求.png)
较于GET请求，POST 多了Content_Length字段

##PUT:传输文件

不安全、幂等；
资源整体更新；

![](https://github.com/onlyAngelia/Read-Mark/blob/master/HTTP/_image/PUT请求.png)
较于POST请求，多了Content-Type 字段

##DELETE:删除文件

不安全、幂等；

##HEAD:获取指定资源，但不返回报文主体，只用于确认URI的有效性以及资源更新

安全、幂等；
![](https://github.com/onlyAngelia/Read-Mark/blob/master/HTTP/_image/HEAD请求.png)
HEAD请求与GET请求一样，不同的是返回只返回首部，不返回报文主体

##OPTIONS:询问支持方法

向服务器查询请求URI指定资源支持的方法；

安全、幂等;
![](https://github.com/onlyAngelia/Read-Mark/blob/master/HTTP/_image/OPTIONS.png)

##TRACE:路径追踪

服务器将之前的请求通信回还给客户端；
可以查询发送出的信息加工和被篡改情况；
容易受到跨站追踪攻击；

![](https://github.com/onlyAngelia/Read-Mark/blob/master/HTTP/_image/TRACE.png)
追踪方法是首部字段Max-Forwards 填入数值，经过一次服务器时减1

##CONNECT:隧道协议连接代理


##PATCH：更新资源 （HTTP/1.1之后增加）

不安全、不幂等；
更新服务器部分资源；
资源不存在，会创建新资源；








