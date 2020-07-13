
##1.python怎么读database
import MySQLdb
db = MySQLdb.connect(
#### 使用cursor()方法获取操作游标
cursor = db.cursor()
#### 使用execute方法执行SQL语句
cursor.execute("SELECT VERSION()")
#### 使用 fetchone() 方法获取一条数据
data = cursor.fetchone()
#### 关闭数据库连接
db.close()

>fetchone(): 该方法获取下一个查询结果集。结果集是一个对象
>
>fetchall():接收全部的返回结果行.
>
>rowcount: 这是一个只读属性，并返回执行execute()方法后影响的行数。



###2.python read/readline/readlines的区别
>read([size])方法从文件当前位置起读取size个字节，若无参数size，则表示读取至文件结束为止，它范围为字符串对象
>readline 从字面意思可以看出，该方法每次读出一行内容，所以，读取时占用内存小，比较适合大文件，该方法返回一个字符串对象
>readlines()方法读取整个文件所有行，保存在一个列表(list)变量中，每行作为一个元素，但读取大文件会比较占内存。

#### python 字符串转换
>int(x) 将x转换为一个整数。
float(x) 将x转换到一个浮点数。
complex(x) 将x转换到一个复数，实数部分为 x，虚数部分为 0。
complex(x, y) 将 x 和 y 转换到一个复数，实数部分为 x，虚数部分为 y。x 和 y 是数字表达式。

#### python 运算
>在整数除法中，除法 / 总是返回一个浮点数，
>如果只想得到整数的结果，丢弃可能的分数部分，可以使用运算符 // ：
>
>17 / 3  # 整数除法返回浮点型  >5.666666666666667

>17 // 3  # 整数除法返回向下取整后的结果  > >5

>17 % 3  # ％操作符返回除法的余数  >>2

>5 * 3 + 2    >>>17



####4.OSI七层，数据链路层传输单位
物理层（bit)-->Data Link Layer（frame)(ARP，RARP，MTU)-->network layber( packaet)(IP，ICMP，RIP，OSPF，BGP，IGMP)->transport layber(TCP/UDP)-->Session-->presentation-->application 
网络层数据包（packet）——数据链路层：数据帧（frame）——物理层：比特流（bit）
####tcp UDP 区别
TCP/UDP协议
TCP(Transmission Control Protocol)和UDP(User Datagram Protocol)协议属于传输层协议。
其中TCP提供IP环境下的数据可靠传输，它提供的服务包括数据流传送、可靠性、有效流控、全双工操作和多路复用。
通过面向连接、端到端和可靠的数据包发送。通俗说，它是事先为所发送的数据开辟出连接好的通道，然后再进行数据发送;
而UDP则不为IP提供可靠性、流控或差错恢复功能。一般来说，TCP对应的是可靠性要求高的应用，而UDP对应的则是可靠性要求低、传输经济的应用。
TCP支持的应用协议主要有：Telnet、FTP、SMTP等;UDP支持的应用层协议主要有：NFS(网络文件系统)、SNMP(简单网络管理协议)、DNS(主域名称系统)、TFTP(通用文件传输协议)等。
TCP/IP协议与低层的数据链路层和物理层无关，这也是TCP/IP的重要特点。

#### 3 way Handshake
[https://media.geeksforgeeks.org/wp-content/uploads/handshake-1.png][https://media.geeksforgeeks.org/wp-content/uploads/handshake-1.png]
>Step 1 (SYN) : In the first step, client wants to establish a connection with server, so it sends a segment with SYN(Synchronize Sequence Number) 
>which informs server that client is likely to start communication and with what sequence number it starts segments with

>Step 2 (SYN + ACK): Server responds to the client request with SYN-ACK signal bits set. 
>Acknowledgement(ACK) signifies the response of segment it received and SYN signifies with what sequence number it is likely to start the segments with

>Step 3 (ACK) : In the final part client acknowledges the response of server 
>and they both establish a reliable connection with which they will start the actual data transfer

#### 4 way handshake to close session
2.TCP断开连接，四次挥手。
当客户端把所有数据传送完毕的时候，给服务端口送一个FIN报文，告知服务端：我这边没有数据可传，希望关闭客户端到服务端方向的连接。之后其状态由原来的
>client ---> Fin--status to ->FIN_WAIT_1
ESTABLISHED 变为FIN_WAIT_1,；

服务端收到客户的FIN报文后，送一个ACK报文给客户端，告知“我服务端知道你客户端口已经没有数据可传，
但是我这边什么关闭连接，还需要等我的数据传完；如果我这里数据也传送完了，我也会给发送一个FIN报文。”。此时服务端发送ACK报文后，状态由之前的ESTABLISHED 变为CLOSE_WAIT
>Server receive "FIN" from client, then send -->ACK to client, also send "FIN" to client 
>server change status "ESTABLISHED" ---》 "close_wait" 

客户端端收到服务的ACK报文，将FIN_WAIT_1置FIN_WAIT_2,同时，继续等来的服务发送FIN报文。
>client rev "server ACK" then change  FIN_WAIT_1---->FIN_WAIT_2

当服务端数据传送也完毕的后，开始给客户端发送FIN包，发送FIN包后，其状态CLOSE_WAIT置为LAST_ACK
>server send all the ate, then send "FIN" to client 
server: "CLOSE_WAIT" -->"LAST_ACK"

客户端口收到了服务的发过来的FIN包后，又给服务端发送ACK。发送ACK后，状态由原来的FIN_WAIT_2置为TIME_WAIT，客户在经过2MSL 时间进入CLOSE状态
>client receive "server FIN" -- then send "ACK"  to sever 
>client (FIN_WAIT_1---->)FIN_WAIT_2---->time_wait
>after 2msl ----> close
服务端口收到客户端发送的ACK后，由LAST_ACK也进入CLOSE

client:
FIN_WAIT_1: 发送FIN给服务端口。
FIN_WAIT_2:收到服务端的ACK报文
TIME_WAIT :收到服务端发过来的FIN报文，发送ACK报文给服务端口。
主动关闭连接端，接收到服务（TIME_WAIT是主动端关闭）之后进入2MSL时间的等待
1MSL around 2 mins
CLOSE：2MSl过后，关闭进入初始化状态。
=== solve time_wait ==
>vim /etc/sysctl.conf
然后，在这个文件中，加入下面的几行内容：
net.ipv4.tcp_syncookies = 1
net.ipv4.tcp_tw_reuse = 1
net.ipv4.tcp_tw_recycle = 1
net.ipv4.tcp_fin_timeout = 30
最后输入下面的命令，让内核参数生效：
 /sbin/sysctl -p
简单的说明下，上面的参数的含义：
net.ipv4.tcp_syncookies = 1 表示开启SYN Cookies。当出现SYN等待队列溢出时，启用cookies来处理，可防范少量SYN***，默认为0，表示关闭；
net.ipv4.tcp_tw_reuse = 1 表示开启重用。允许将TIME-WAIT sockets重新用于新的TCP连接，默认为0，表示关闭；
net.ipv4.tcp_tw_recycle = 1 表示开启TCP连接中TIME-WAIT sockets的快速回收，默认为0，表示关闭；
net.ipv4.tcp_fin_timeout 修改系統默认的 TIMEOUT 时间。
在经过这样的调整之后，除了会进一步提升服务器的负载能力之外，还能够防御一定程度的DDoS、CC和SYN***，是个一举两得的做法。


=== server
CLOSE_WAIT：收到客户端FIN报文，给客户端发送ACK状态后，表示知道客户端要关闭连接请求，服务端可能数据还没有传送完，所以处于等
等待关闭状态。（CLOSE_WAIT是被动端关闭）
LAST_ACK：服务端数据传输完毕，发送FIN报文给客户端，同时等待客户端发ACK报文状态
CLOSE：收到客户端ACK报文后，进入初始化状态

[https://blog.csdn.net/enlaihe/article/details/78900482][https://blog.csdn.net/enlaihe/article/details/78900482]

####5.数据链路层和数据传输层的校验方法的区别
6.长连接和短连接及适用情况
####7.https加密过程    http application layer
https://zhuanlan.zhihu.com/p/115477137
>200 OK - 客户端请求成功
301 - 资源（网页等）被永久转移到其它URL
302 - 临时跳转
400 Bad Request - 客户端请求有语法错误，不能被服务器所理解
401 Unauthorized - 请求未经授权，这个状态代码必须和WWW-Authenticate报头域一起使用
404 - 请求资源不存在，可能是输入了错误的URL
500 - 服务器内部发生了不可预期的错误
503 Server Unavailable - 服务器当前不能处理客户端的请求，一段时间后可能恢复正常。
>502 bad gateway

####5.URI和URL的区别
>HTTP使用统一资源标识符（Uniform Resource Identifiers, URI）来传输数据和建立连接。
URI：Uniform Resource Identifier 统一资源标识符
URL：Uniform Resource Location 统一资源定位符
URI 是用来标示 一个具体的资源的，我们可以通过 URI 知道一个资源是什么。
URL 则是用来定位具体的资源的，标示了一个具体的资源位置。互联网上的每个文件都有一个唯一的URL。

8.4次挥手大量Time_wait的解决方法
9.说说LVS调度算法，优缺点（我只记得前四个，为啥不问我3个模式啊！！！）
####10.乐观锁悲观锁
>乐观锁的思路一般是表中增加版本字段，更新时where语句中增加版本的判断，算是一种CAS（Compare And Swep）操作，商品库存场景中number起到了版本控制（相当于version）的作用（ AND number=#{number}）。

>悲观锁之所以是悲观，在于他认为本次操作会发生并发冲突，所以一开始就对商品加上锁（SELECT ... FOR UPDATE），然后就可以安心的做判断和更新，因为这时候不会有别人更新这条商品库存。

>乐观锁（Optimistic Lock），顾名思义，就是很乐观，每次去拿数据的时候都认为别人不会修改，所以不会上锁，
但是在提交更新的时候会判断一下在此期间别人有没有去更新这个数据。乐观锁适用于读多写少的应用场景，这样可以提高吞吐量。
乐观锁：假设不会发生并发冲突，只在提交操作时检查是否违反数据完整性。

>使用数据版本（Version）记录机制实现，这是乐观锁最常用的一种实现方式。何谓数据版本？即为数据增加一个版本标识，一般是通过为数据库表增加一个数字类型的 “version” 字段来实现。当读取数据时，将version字段的值一同读出，数据每更新一次，对此version值加一。当我们提交更新的时候，判断数据库表对应记录的当前版本信息与第一次取出来的version值进行比对，如果数据库表当前版本号与第一次取出来的version值相等，则予以更新，否则认为是过期数据。

>使用时间戳（timestamp）。乐观锁定的第二种实现方式和第一种差不多，同样是在需要乐观锁控制的table中增加一个字段，名称无所谓，字段类型使用时间戳（timestamp）, 和上面的version类似，也是在更新提交的时候检查当前数据库中数据的时间戳和自己更新前取到的时间戳进行对比，如果一致则OK，否则就是版本冲突。

乐观锁一般来说有以下2种方式：
使用数据版本（Version）记录机制实现，这是乐观锁最常用的一种实现方式。何谓数据版本？即为数据增加一个版本标识，一般是通过为数据库表增加一个数字类型的 “version” 字段来实现。当读取数据时，将version字段的值一同读出，数据每更新一次，对此version值加一。当我们提交更新的时候，判断数据库表对应记录的当前版本信息与第一次取出来的version值进行比对，如果数据库表当前版本号与第一次取出来的version值相等，则予以更新，否则认为是过期数据。
使用时间戳（timestamp）。乐观锁定的第二种实现方式和第一种差不多，同样是在需要乐观锁控制的table中增加一个字段，名称无所谓，字段类型使用时间戳（timestamp）, 和上面的version类似，也是在更新提交的时候检查当前数据库中数据的时间戳和自己更新前取到的时间戳进行对比，如果一致则OK，否则就是版本冲突。

####LB alogreshm
Round Robin
Weighted Round Robin
Least Connection
Weighted Least Connection


k8s网络通信原理（pod内，pod间）
4、docker原理，与虚拟机区别
5、mysql主从原理
HEAP表存在于内存中，用于临时高速存储。
6、编程题：判断string是否有重复字符出现

长短连接
3、OSI网络模型各个层次功能
4、LVS的NAT、TUN、DR原理及区别
5、keeplived高可用原理（VRRP）
6、nginx为什么比httpd快（epoll）
7、四层、七层反向代理的区别
8、iptables原理，工作在几层 
9、k8s架构+网络模型，描述通信过程；假如遇到问题怎么处理
10、redis主从原理
11、描述一个遇到的问题以及处理过程和思路

####GRE VXLAN
>GRE (Generic Routing Encapsulation) is used for tunneling of frames over IP network. 
Here a frame will be encapsulated with IP header where source IP Address corresponds to tunnel Source IP address and
> Destination IP Address corresponds to destination of the tunnel. 
>In addition to IP header a GRE HEADER will also get added. 
>These tunnels are used between Routers and only routing is used before and after the encapsulation and decapsulation. 
>Once frame reaches the tunnel destination, frame will be decapsulated from outer IP and GRE headers, and routed using Inner IP addresses.

>In VXLAN 
>在VXLAN中这类封装和解封的组件有个专有的名字叫做VTEP。相比起VLAN来说，好处在于其突破了VLAN只有4094子网的限制，
a frame including original layer2 header will be encapsulated with IP header, a UDP header and VXLAN header. 
>VxLAN is used widely in Data centers. Devices which do Encapsulation and decapsulation of frames are called VTEP's, 
>they are hybrid devices with both switching and Routing functionality in it. 
>When a frame enters VTEP whole frame including original Ethernet header or layer2 header will also get included. 
>Whereas in GRE Layer2 header will not get included. When frame gets forwarded in VxLAN 
>it looks like as if there were no routers included while forwarding the frame, hence it is also called overlay technology, which works on layer3 underlay.


[https://media.geeksforgeeks.org/wp-content/uploads/handshake-1.png]: https://media.geeksforgeeks.org/wp-content/uploads/handshake-1.png

[https://blog.csdn.net/enlaihe/article/details/78900482]: https://blog.csdn.net/enlaihe/article/details/78900482