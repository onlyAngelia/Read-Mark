图解HTTP read mark


#一.请求报文构成

![](https://github.com/onlyAngelia/Read-Mark/blob/master/HTTP/_image/请求报文.png)

    客户端的HTTP报文叫做请求报文

请求报文首部包含：

    1.请求行：用户请求的方法，请求URI 和HTTP版本号。如图中所示POST /form/entry  HTTP/1.1

    2.首部字段：请求的各种条件和属性
       首部字段包含以下信息：
       请求首部字段（Request Header Fields）：
        (1)Accept:通知服务器客户端能够处理的媒体类型及优先级
        (2)Accept-Charset:通知服务器用户代理支持的字符集以及字符集的相对优先顺序
        (3)Accept-Encoding:告知服务器用户代理支持的内容编码以及优先级顺序
        (4)Accept-Language:告知服务器用户代理能够处理的自然语言集
        (5)Authorization: 告知服务器用户代理的认证信息
        (6)Expect:告知服务器期望出现的某种特定行为
        (7)Form:告知服务器使用用户代理的用户的电子邮件地址
        (8)Host:告知服务器请求资源所处的互联网主机名和端口号
        (9)IF-match:告知服务器匹配资源的实体比较（Etag）值
        (10)If-Modified-Since:该字段指定日期时间后，资源发生了更新，则服务器接受请求
        (11)If-None-Match:只有在该字段值与ETage值不一致时，可处理该请求
        (12)If-Range:若该字段的ETag值或时间和请求资源服务器的ETag或时间一致，则作为范围请求处理，反之则返回全部资源
        (13)If-Unmodified-Since:告知服务器在指定时间之后未发生更新才能处理请求
        (14)Max-Forwards:十进制数字整数形式指定经过的服务器最大数目
        (15)Proxy-Authorization:告知服务器认证所需要的信息，发生在客户端与代理之间
        (16)Range:范围请求的资源范围
        (17)Referer:告知服务器请求的原始资源的URI
        (18)TE:告知服务器客户端能够处理响应的传输编码格式以及相对优先级，和Accept-Encoding类似，但用于传输编码格式
        (19)User-Agent:用于传达浏览器的种类
        
       通用首部字段（General Header Fields）：请求报文和响应报文双方都会使用的首部
        (1) Cache-Control：控制缓存行为
        (2) Connection：管理持久连接，控制不再转发给代理的首部字段 
       （3）Date：创建HTTP报文的日期和时间
        (4）Pragma:只用在客户端，为了1.1版本之前的协议向后兼容
       （5）Trailer:事先说明在报文主体后记录了哪些首部字段，可应用于类似分段传输时
        (6) Transfer-Encoding：规定传输报文主体时采用的编码格式 HTTP1.1的传输编码仅对分块传输编码有效
        (7) Upgrade：用于检测HTTP协议以及其它协议是否可使用更高版本的协议进行通信
        (8) Via：用于追踪报文的转发，可避免请求回环的发生，通常与Trace关联使用
        (9) Warning:告知用户一些与缓存相关的问题警告
        
       实体首部字段 (Entity Header Fields) ：
       (1)Allow:告知客户端能够支持的所有HTTP方法
       (2)Content-Encoding:告知客户端服务器对实体的主体部分选用的内容编码方式
       (3)Content-Language:告知客户端实体主体使用的自然语言
       (4)Content-Length:表明了实体主体部分的大小（单位是字节）
       (5)Content-Location:表示报文主体返回资源对应的URI
       (6)Content-MD5:一串报文主体由MD5算法生成的值
       (7)Content-Range:告知客户端作为响应返回的实体的哪个部分符合范围请求
       (8)Content-Type:说明实体主体内对象的媒体类型
       (9)Expires:将资源失效日期告知客户端
       (10)Last-Modified:指明资源最终修改的时间
       
    3.其它：RFC里未定义的首部（如Cookie）
       为Cookie服务的首部字段
      (1)Set-Cookie：开始状态管理所使用的Cookie信息

#二.响应报文构成
![](https://github.com/onlyAngelia/Read-Mark/blob/master/HTTP/_image/响应报文.png)     

服务器端的HTTP报文叫做响应报文

响应报文首部包含：

    1.状态行 ：包含HTTP 版本号 、响应结果状态码 、原因短语。如图中所示HTTP/1.1 200 OK

    2.首部字段： 响应的各种条件和属性
    
    响应首部字段 (Response Header Fields):
    (1)Accept-Ranges:告知客户端是否能处理范围请求
    (2)Age:告知客户端服务器多久前创建的响应，单位为秒
    (3)ETag:告知客户端实体标识
    (4)Location:将响应接收方引导至某个与请求URI位置不同的资源
    (5)Proxy-Authenticate:把由代理服务器所要求的认证信息发送给客户端
    (6)Retry-After:告知客户端多久之后再次发送请求
    (7)Server:告知客户端当前服务器上安装的HTTP服务器应用程序的信息
    (8)Vary:对缓存进行控制
    (9)WWW-Authenticate:用于HTTP访问认证，告知客户端请求URI指定资源的认证方案和带参数提示的质询
    
    通用首部字段（General Header Fields）：
    （1）Cache-Control：控制缓存行为
     (2) Connection：管理持久连接，控制不再转发给代理的首部字段 
    （3）Date：创建HTTP报文的日期和时间
    （4）Trailer:事先说明在报文主体后记录了哪些首部字段，可应用于类似分段传输时
     (5) Transfer-Encoding：规定传输报文主体时采用的编码格式 HTTP1.1的传输编码仅对分块传输编码有效
     (6) Upgrade：用于检测HTTP协议以及其它协议是否可使用更高版本的协议进行通信
     (7) Via：用于追踪报文的转发，可避免请求回环的发生，通常与Trace关联使用
     (8) Warning:告知用户一些与缓存相关的问题警告
     
    实体首部字段 (Entity Header Fields) ：
    
    3.其它： RFC里未定义的首部（如Cookie）

HTTP1.0/1.1 报文面向文本  所以才会有我们熟悉的XML、json、txt等传输

#三.HTTP 无状态协议
    
    HTTP是无状态协议，不会对之前的请求做状态记录。同样的用户请求在每次请求时会重新登录或跳转。
    为此引入了Cookie机制
    Cookie是在请求和响应报文中写入Cookie信息控制客户端状态。
    客户端第一次请求的响应报文中首部会返回字段Set-Cookie，客户端根据该字段信息存储；
    Cookie存储在客户端，服务器不存储Cookie；
    Cookie信息因保存在客户端，所以更换服务器时Cookie信息会失效。

#四.HTTP方法

##GET： 获取资源

    请求获取指定资源，若是文本直接返回，接收其它格式返回处理后结果；
    安全、幂等(幂等是指同一个请求方法执行多次和仅执行一次的效果完全相同)；
    可缓存；
    报文主题没有任何语义（可打开Postman这样的工具，会发现body体不让设置）;
    参数拼接在url中，明文传输;

![](https://github.com/onlyAngelia/Read-Mark/blob/master/HTTP/_image/GET请求.png)

##POST:传送实体

    传送实体，根据报文主体对指定资源做出处理；
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

##CONNECT:与代理服务器通信时建立隧道

    隧道协议进行TCP通信；
    使用SSL、TLS 协议加密；

    方法格式为：
    CONNECT 代理服务器名：端口号  HTTP版本

##PATCH：更新资源 （HTTP/1.1之后增加）

    不安全、不幂等；
    更新服务器部分资源；
    资源不存在，会创建新资源；

#五.HTTP持久连接

    HTTP每次请求之后断开TCP连接，下次连接重新进行TCP握手。
    为减少每次TCP连接建立和断开而带来的通信量开销，提出了HTTP keep=alive 即轮询机制。
    若任一端没有明确提出断开连接，则保持TCP连接状态。


    HTTP/1.0 之前没有持久连接；
    HTTP/1.1 连接默认是持久连接；
    HTTP/2.0 持久连接；

##管线化（pipelining）

    管线化基于持久连接，与持久连接不同的是，持久连接发送请求得到响应之后再发送下次HTTP请求，而管线化不用等待可以直接发送下一个请求。


HTTP持久连接如图

![](https://github.com/onlyAngelia/Read-Mark/blob/master/HTTP/_image/keep-alive.png)


管线化如图

![](https://github.com/onlyAngelia/Read-Mark/blob/master/HTTP/_image/pipelining.png)

#六.HTTP传输及返回

1.报文&实体

报文：HTTP通信基本单位，8位组字节流组成

实体：请求或响应的有效载体，由实体首部和实体主体组成

     两者在一般情况下会保持一致，但若在传输中经过了编码操作时，会出现报文不等于实体。常用的编码有
     
内容编码：一般会将内容进行压缩

分块传输编码：将实体分成多个部分。每一块会用十六进制标记块的大小，而实体主体的最后一块会用“0（CR+LF）”标记

2.范围请求：获取部分范围，之情范围发送Range Request

3.多种对象集合：包含文字、图片、音视频等

    multipart/form-data

    multipart/byteranges

4.内容协商机制：客户端和服务端就响应资源进行协商，返回最合适的内容

    example：web页面默认为英文则返回英文数据，若默认为中文则返回中文数据

     技术有以下三种类型
    服务器驱动协商：由服务器进行内容协商

    客户端驱动协商：由客户端进行内容协商

    透明协商：服务器和客户端结合协商

5.状态码详解

状态码类型：


    1XX   Informational (信息性状态码)  接收的请求正在处理

    2XX   Success（成功状态码） 请求正常处理完毕

    3XX   Redirection（重定向状态码） 需要进行附加操作以完成请求

    4XX  Client Error（客户端错误状态码） 服务器无法处理请求

    5XX  Server Error （服务器错误状态码） 服务器处理请求出错

常用的状态码：

    200   OK    客户端发送的请求在服务器端正常处理

    204    No Content   服务器处理请求成功，但无资源返回

    206    Partial Content   客户端进行范围请求，服务器成功相应

    301    Moved Permanently   永久性重定向，服务器资源已更新，客户端需重新保存

    302    Found  临时性重定向   服务器资源已更新，但有可能会改回，返回对应的URI

    303   See Other  对应资源存在另一个URI，务必使用GET方法定向获取请求资源

    304   Not Modified  客户端发送的请求附带条件，服务器找到资源但未符合条件

    307   Temprary Redirect 临时重定向  与302相比不会将POST变GET，但每种浏览器会出现不同的情况

    400 Bad Request   请求报文中存在语法错误

    401 Unauthorized  需要有HTTP认证，若已经发送过请求表示认证失败

    403 Forbiddern  请求资源的访问被服务器拒绝

    404 Not Found  服务器上没有请求的资源

    500  Internal Server Error 服务器在执行请求时发生错误

    503  Service Unavaliable  服务站处于超负荷状态或停机 ，无法处理此次请求

#七 HTTP 与服务器

1.DNS域名解析

     客户端访问服务器时经常采用类似主机名和域名，但是服务器识别的是IP地址，中间的映射则需要通过DNS服务
 
 2.Host首部内完整指定主机名和域名URI 
 
    因为一台HTTP服务器可以创建多台虚拟主机，这就造成了相同IP下，虚拟主机可以寄存多个不同主机名和域名的Web网站，所以需要Host 首部指定主机名和域名URI。

3.数据转发

从客户端到服务端整个数据传输，中间会经过一些应用程序和服务器。

代理服务器：

    接收客户端发送的请求转发给其它服务器，不改变URI，到达持有资源的实体服务器（即源服务器），之后再从源服务器经过一层层代理服务器返回给客户端。
 
    代理服务器类型基本有 （1）是否使用缓存  （2）是否修改报文
  
缓存代理（Caching Proxy）预先将资源副本缓存在代理服务器上，再次接收相同资源请求时，就可以不从源服务器获取资源，直接将缓存资源作为响应返回 
  
    ![](https://github.com/onlyAngelia/Read-Mark/blob/master/HTTP/_image/缓存代理.png)
  
透明代理  转发请求或响应时，不对报文做任何加工的代理，对报文内容进行加工的代理是非透明代理
  
    理由：利用缓存技术减少网络带宽，组织内部特定网站的访问控制，获取访问目的
  
网关：为服务器提供非HTTP协议服务

    优点：提高通信安全性，在客户端和网关之间线路上加密
 
隧道：使用SSL加密手段 建立起与其它服务器通信线路
         
     隧道不解析HTTP请求，保持原样中转给之后服务器。在通信双方断开连接时结束。

缓存：指代理服务器或客户端在磁盘内保存的资源副本。

       优点：减少对资源服务器的访问，节省通信流量和通信时间。
       期限：受服务器更新和客户端请求条件限制，会向服务器确认资源的有效性，若失效则重新从资源服务器上获取"新"资源
       客户端缓存：临时网络文件，若资源有效，则不必请求，从本地磁盘读取

#八、首部字段指令

 -------
  通用首部指令


 1、Cache-Control 指令
 
       缓存请求指令：
        no-cache（强制验证无缓存，会向服务器确认资源有效期）；
        no-store （不缓存请求或响应的任何内容）；
        max-age = [秒]（响应最大Age值）；
        max-stale （接收已过期的响应，若未指定参数值，则无论过多久，客户端都会接收响应，若指定了具体数值，则接收处于max-stale指定时间内的数据）；
        min-fresh = [秒] (要求缓存服务器返回至少还未过指定时间的缓存资源);
        no-transfor （代理不可更改媒体类型，防止缓存或代理压缩图片等类似操作）；
        only-if-cached （仅从缓存服务器获取资源，缓存服务器若无响应，则返回状态码504）；
        cache-extension （新指令标记，可扩展Cache-Control首部字段）；
       缓存响应指令
       public （可向任意方提供响应的缓存）；
       private（仅向特定用户返回响应）；
       no-cache （缓存前必须先确认其有效性）；
       no-store（不缓存请求或响应的任何内容）；
       no-transform（代理不可更改媒体类型，防止缓存或代理压缩图片等操作）；
       must-revalidate（可缓存但必须再向源服务器进行确认）；
       proxy-revalidate（要求中间缓存服务器对缓存的响应有效性再进行确认）；
       max-age = [秒] （响应的最大Age值）；
       s-maxage= [秒] （公共缓存服务器想用的最大Age值，适用于多位用户使用公共缓存代理服务器）；
       cache-extension （新指令标记，可扩展Cache-Control首部字段）；
       
2、Connection
       
       close：关闭持久连接
       Keep - Alive：保持长久连接
       其它需要代理服务忽视的字段 
       Connection：需要忽视字段
       
3、Upgrade
  
      Upgrade首部字段产生作用的Upgrade对象仅限于客户端和邻接服务器之间，在使用字段Upgrade时需要额外指定Connection：Upgrade。而对于应用了该字段的请求，服务器可用101 Switching Protocols状态码作为响应返回。
      
4、Warning
       
       Warning首部格式如下，最后日期时间部分可省略
       warning：[警告码][警告的主机：端口号]"[警告内容]"([日期时间])
    警告码以及警告说明如图：
    
    ![](https://github.com/onlyAngelia/Read-Mark/blob/master/HTTP/_image/HTTP1.1警告码.png)

------
 请求首部字段指令
 
1.Accept
        
         文本文件
         text/html，text/plain,text/css ...
         图片文件
         image/jpeg,image/gif,image/png...
         视频文件
         video/mpeg,video/quicktime ...
         应用程序使用的二进制文件
         applicaion/octet-stream,application/zip...
        
        quality factor:质量数，权重
        媒体类型的优先级，q=0~1（范围为0~1，可精确到小数点后三位）;
2.Accept-Charset

        可用来通知服务器用户代理支持的字符集以及相对优先顺序，与Accept一样可以通过设置权重q表示相对优先级
3.Accept-Encoding
   
          .gzip
          由文件压缩程序gzip生成的编码格式（RFC1952）采用Lempel-Ziv算法及32位循环校验
          .compress
          由UNIX文件压缩程序compress生成的编码格式，采用Lempel-Ziv-Welch算法
          .deflate
          组合使用zlib格式（RFC1950）及deflate压缩算法生成的编码格式
          .identity
          不执行压缩或不会变化的默认编码格式
          *.通配符，代表任意格式编码
4.Expect
          
        告知服务器希望出现的特定行为，若服务器无法理解客户端的期望，则返回状态码417
           HTTP/1.1只定义该字段一个指令：100-continue

5.Form
     
        告知服务器用户代理使用的电子邮件地址。使用目的是为了显示搜索引擎等用户代理的负责人的电子邮件联系方式。使用代理时，尽可能包含From首部字段，但因代理不同，通常将电子邮件地址记录在User-Agent 首部字段内
           
6.If-Match
      
       If-Match 告知拂去我匹配资源的实体标记值，服务器比较资源和IF-Match的ETag值，只有两者一致时才会执行请求。若不满足则返回412状态码
       
7.If-None-Match
       
       与IF-Match首部字段作用相反，当IF-None-Match字段值的实体标记与请求资源的Etage不一致时，告知服务器处理该请求，在GET或HEAD方法中使用该字段可获取最新的资源。
       
![](https://github.com/onlyAngelia/Read-Mark/blob/master/HTTP/_image/IF-None-Match.png)
       
8.If-Modified-Since

        If-Modified-Since 会告知服务器若该字段值早于资源的更新时间，则希望能处理该请求，而再指定时间之后，如果请求的资源没有更新过，则返回304 Not modified的响应，主要用来确认代理或客户端拥有的本地资源的有效性。

9.If-Unomodified-Since

        与If-Modified-Since字段相反，该字段告知服务器，请求的指定资源在字段值内指定的日期之后，未发生更新，才能处理请求。若在指定日期之后发生更新，则以状态码412作为响应返回
             
10.If-Range
 
        If-Range 告知服务器若ETag值或时间匹配则作为范围请求，若不匹配，则返回全部资源。这样的好处是可以避免二次请求。若不使用If-Range则在不匹配的情况下，服务器返回状态码412 Precondition Failed，催促客户端再次发送请求。
          
11.Range

        Range指定范围请求的资源范围，接收到附带Range首部字段请求的服务器，会在响应之后返回206的响应，无法处理该范围请求时，则返回状态码200 OK的响应以及全部资源
        
12.TE
     
          TE用来指定传输编码，另外可指定伴随trailer的分块传输编码方式。
          TE:trailers

-------
响应首部字段指令

1.Accept-Ranges

        Accept-Ranges告知客户端能否处理范围请求，可处理范围请求则Accept-Ranges：bytes，
        若不能请求范围请求，则返回Accept-Ranges：None
        
2.ETag

        ETag是可将资源以字符串形式做唯一标识的方式。当资源更新时，ETag值也需要更新，另外生成ETag值并没有统一的算法规则，仅仅由服务器来分配。
           资源被缓存时会被分配唯一标识，而因为返回协商机制服务器相同资源不同版本对应的URI一致，当协商返回时仅凭URI指定缓存资源无法做到，所以会依据ETag值返回。在下载过程中出现连接中断、再连接的情况，都会依照ETag值来获取资源。
            
            强ETag值&弱ETag值
            ETag："usagi-1234"  不论实体发生多么细微的变化都会改变其值
            ETag：W/"usagi-1234" 只有资源发生了根本改变产生差异时才会改变ETag值
           
3.Location

        Location可以将响应接收方引导至某个不同URI，配合3xx 提供重定向URI，基本情况下浏览器在接收到包含首部字段Location的响应后会强制性地尝试对已提示的重定向资源的访问

4.Vary

        Vary可对缓存进行控制，源服务器会向代理服务器传达关于本地缓存使用方法的命令。代理服务器接收到源服务器返回的包含Vary指定项的响应之后，若再进行缓存，则仅仅对请求中包含相同Vary指定首部字段的返回进行缓存。哪怕相同资源发起请求，若Vary指定的首部字段不同的话，也必须要从源服务器重新获取资源。
-----
实体首部字段指令

1.Content-Location

          Content-Location给出与报文主体部分对应的URI，当返回的页面内容与实际请求的对象不同时，首部字段Content-Location内会写明URI

2.Content-MD5

              Content-MD5字段值是对报文主体执行MD5算法获得的128位二进制数，再通过Base64编码后的结果。这样做的目的在于检验报文主体在传输过程中是否保持完整以及确认传输到达。
-------
为Cookie服务的字段指令
1.Set-Cookie
        
        expires：指定浏览器可发送Cookie的有效期
        path：限制指定Cookie的发送范围的文件目录
        domain：指定的域名可做到与结尾匹配一致
        secure：限制Web页面仅在HTTPS安全连接时可以发送Cookie
        HttpOnly：
