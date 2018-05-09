图解HTTP read mark

1.请求报文构成
   |   方法     ——               |   URI ——————                 |协议版本
`post ` `/form/entry` ` HTTP/1.1`
|请求首部
```
Host:hackr.jp
Connection:keep -alive
Content -Type: application/x-www-form-urlencoded
Content -Length:16
```
 |内容实体
`name = ueno&age=18`

2.响应报文构成
   |  协议版本  |  状态码  |状态码描述短语
 `HTTP/1.1`  `200`    `OK`
|响应首部
```
|  Date: Tue, 10 Iul 2018 11:12:20 GMT
| Content -Length: 362
| Content -Type: text/html 
```
|响应主体
```
 <html> 
 、、、、、、、、
```              
3.HTTP 无状态协议，为此引入了Cookie
4.HTTP方法
GET：                                                                                         




