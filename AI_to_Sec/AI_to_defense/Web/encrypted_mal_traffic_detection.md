## 加密流量检测



### 加密恶意流量识别方法概述

1. #### 解密

   一般用于企业出口，已知私钥

   解密方式：

   - 代理解密（传统）

   - 云端IAP（identity-aware proxy）
   - 会话密钥转发（从主机内存中获取加密秘钥对）

   缺陷：

   1. 并不适用所有加密，入站加密流量无法进行解密(很大的一个盲点)
   2. 削弱了用户的隐私
   3. 计算密集

2. #### 不解密

   加密流量推断（encrypted traffic inference, ETI）

   加密流量元数据：

   - DNS元数据
   - TLS元数据
   - HTTP头部元数据

   检测角度：

   - 客户端以及服务器指纹

   &emsp;&emsp;未来比较有前景的方式：ETI技术与解密流量检测技术相结合。举例而言，企业可以使用ETI解决方案对入站流量做一个第一步检测。大部分流量会被认为是安全的，但依然有一小部分流量会被判定为可疑流量——这部分流量就会被解密做深度包检测。这样的结合会减少对解密的需求，降低解密相关的成本，并且在日益混合的架构中实现更灵活的部署。



### 加密流量识别方法

#### 方案一：flow角度进行特征提取

角度：以（source IP, destination IP, destination port, protocol）四元组为单位构建成flow，以flow为单位构建统计特征。

工具：使用Bro提取con.log、ssl.log、certificate.log三个日志文件从中进行特征提取，在conn中的ssl连接都有唯一的连接字符串，可以使用连接字符串关联到ssl.log的ssl通信信息，ssl.log中会包含使用其使用的证书链id，利用证书链id可以从x509.log来查找相关证书的详细信息

![image](https://raw.githubusercontent.com/AnchoretY/images/master/blog/image.59b9sgqtzfb.png)

特征:

| 特征名称                          | 特征来源 |      |
| --------------------------------- | -------- | ---- |
| flow中报文数量                    | conn     |      |
| flow连接持续的时间的平均值        | conn     | ？   |
| flow连接持续时间的标准差          | conn     |      |
|                                   |          |      |
| 发送方发送的bytes总数             | con      |      |
| 响应方接受的bytes总数             | con      |      |
| 响应方发送的bytes占通信总量的比例 | con      |      |
| 建立连接的百分比                  | con      | ？   |
| 入向包占比                        |          |      |
| 出向包占比                        |          |      |
| 连接的周期的平均值                |          |      |
| 连接的周期的标准差                |          |      |
| 使用ssl与非ssl记录的比例          | ssl      |      |
| 平均秘钥长度                      | ssl      |      |
| 使用TLS记录的比例                 | ssl      |      |
| SSL记录中使用SNI的比例            | ssl      |      |
| 自签名证书的比例                  | ssl      |      |
| ssl中使用不同SNI的比例            | ssl      |      |
| ssl连接中使用不同subject的比例    | ssl      |      |
| ssl连接中使用不同issuser          | ssl      |      |
| 具有相同subject的ssl比例          | ssl      |      |
| 具有相同issuser的比例             | ssl      |      |
| SNI是否为顶级域名                 | ssl      |      |
| 证书长度的平均值                  | 证书     |      |
| 证书长度的标准差                  | 证书     |      |
| 证书是否为有效证书（第一个证书）  | 证书     |      |
| 证书的数量                        | 证书     |      |
| 证书中包含域名的数量              | 证书     |      |
| Number of signed paths            | 证书     |      |
| ssl log中使用x509的比例           | 证书     |      |
| 是否启用SAN DNS                   | 证书     | ？   |
| SAN中是否全部都为common names     | 证书     |      |
| subjects比例                      | 证书     |      |
| issusers比例                      | 证书     |      |
| SAN DNS比例                       | 证书     |      |
| CN和SNI是否相同                   | 证书     |      |
| Average exponent                  | 证书     |      |
| 证书路径是否有效                  | 证书     |      |

#### 方案二：基于背景流量的恶意加密流量检测方法

&emsp;&emsp;Andersion等人提出了一种拓展流记录以包含与加密流相关的所有元数据，这种拓展是**通过指向上下文流的指针来加入DNS、HTTP背景流量**实现。Anderson等人**将DNS上下文流定义为基于目标IP地址与TLS流相关的DNS响应，HTTP上下文定义为源自5min窗口内的相同源IP地址的HTTP流**。









> 
>
> X509:
>
> 
>







### 数据集







### Blog

1. #### [一篇报告了解国内首个针对加密流量的检测引擎](https://mp.weixin.qq.com/s/HTrQ5BK-mhXfJmMlwHD04w)

   观成科技

2. #### [恶意软件加密通信概要分析](https://mp.weixin.qq.com/s/8nnfSjPVmWbThKrSlqNriQ)

   观成科技

3. ####  [火眼金睛：利用机器学习识别加密流量中的恶意软件](https://mp.weixin.qq.com/s/qngs8-jjHVcdMco1MQfs9Q)

   思科在加密流量检测中的检测方案

4. #### [基于机器学习的恶意软件加密流量检测研究分享](https://blog.riskivy.com/%E5%9F%BA%E4%BA%8E%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0%E7%9A%84%E6%81%B6%E6%84%8F%E8%BD%AF%E4%BB%B6%E5%8A%A0%E5%AF%86%E6%B5%81%E9%87%8F%E6%A3%80%E6%B5%8B/)

   斗象科技

5. #### [特征工程之加密流量安全检测](https://www.secrss.com/articles/12415)

6. #### [Cisco-Detecting Encrypted Malware Traffic ](https://blogs.cisco.com/security/detecting-encrypted-malware-traffic-without-decryption)

   

   



