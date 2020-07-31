## 恶意域名检测

 &emsp;&emsp;现今恶意软件大多采用DGA生成域名的方式来进行域名的生成，因此这里将DGA和恶意域名统称为恶意域名。

### Paper&Blog

1. Hyrum S. Anderson, Jonathan Woodbridge, Bobby Filar. "DeepDGA: Adversarially-Tuned Domain Generation and Detection" [[pdf\]](https://arxiv.org/abs/1610.01969),6 Oct 2016 **(生成对抗网络，DGA检测)** 
2. Jonathan Woodbridge, Hyrum S. Anderson, Anjum Ahuja, Daniel Grant. "Predicting Domain Generation Algorithms with Long Short-Term Memory Networks" [[pdf\]](https://arxiv.org/abs/1611.00791),2 Nov 2016 **(LSTM,DGA检测)**
3. Manos Antonakakis, Damballa Inc. and Georgia Institute of Technology.  "From Throw-Away Traffic to Bots: Detecting the Rise of DGA-Based Malware",2012. **(DGA,图，谱聚类)**

### Blog

#### 1. [机器学习与威胁情报的融合：一种基于AI检测恶意域名的方法](https://www.freebuf.com/articles/es/187451.html)

  &emsp;&emsp;改文章基于购买的微步的威胁情报中包含的恶意域名作为恶意黑样本构建的恶意域名检测模型，其中采用的一些对比较经典的特征，最终模型**误报率和漏报率均在3%左右**，整体效果还是一般。有构建这方面模型的道友可以将其作为base在其上进行进一步的完善。其中包含的主要特征包括：**Alexa排名、搜狗rank、搜狗与百度的收录数量、必应收录数量、网站首页完整度、是否是主流域名后缀、地理位置、地理位置**。

  其实对于在微步购买的威胁情报中所包含的恶意域名，文章作者已经认识到其标记并不准确，其中也存在包含了alex排名前1000的域名等问题，但是作者并没有在构建训练集时将这些有问题的数据进行剔除，在进行相关任务时应该注意样本集的清洗。

#### 2. [DNS Tunnel隧道隐蔽通信实验 && 尝试复现特征向量化思维方式检测](https://www.cnblogs.com/LittleHann/p/8656621.html#_label3_1_4_0)

&emsp;&emsp;阿里云的在进行DNS隐蔽信道时写的一篇记录文章，文章中首先比较系统的讲述了`IP直连型DNS隐蔽信道、域名型因隐蔽信道两种常见的隐蔽信道`，然后`使用Powershell+dnscat2实现DNS隐蔽隧道反弹Shell进行实际的隐蔽信道木马搭建，获取通信过程的隐蔽信道流量进行分析`，最后`非常全面的讲述了进行DNS隐蔽信道检测可以采用的特征`，其中的`ZIf定律、FQDN数`等都是非常新颖的特征，是一篇做DNS隐蔽信道检测难得的好文。

&emsp;&emsp;在该文章中还提到了在DNS隐蔽信道检测的实际应用中的一个比较核心的问题：`如何区分DNS隐蔽信道和DNS Flood攻击`。

> 1. ZIf定律
>
> &emsp;&emsp;`根据Zif定律，在自然语言的语料库里，词频往往会集中于某些小子集中，并且高频词到低频次的频率逐渐下降`。而在DNS Tunneling中由于域名做了编码，不符合Zipf定律，整个分布趋于平稳。因此可以通过`通过检测排序后的词频平均斜率`来检测input string是否符合zipf law规律。
>
> 2. FQDN
>
> &emsp;&emsp;域名有全称和简称的区别。全称的域名，直译为"完全的合格的域名"(FQDN，Fully Qualified Domain Name)，表现为由"·"隔开的点分式层次结构，叫名称空间， 它指定了一台主机和它所属域的隶属关系，而简称通常就是这台主机的计算机名，在域名的最左边。`FQDN(完全合格的域名)，是域加计算机名的总称`。比如: www.microsoft.com 这个FQDN 中，www 是主机名，microsoft.com 是域。 www+microsoft.com 组合在一块就成了一个完整的域名(FQDN)。可以通过分析一定时间窗口内所产生的FQDN数，`通常DNS Tunneling的FQDN数在一定时间窗口内会远高于正常的DNS流量`。


#### 3. [图/Louvain/DGA乱谈](https://www.cdxy.me/?p=805)


#### 4. [使用社区发现算法从企业内部无效域名中挖掘DGA](http://www.webber.tech/posts/%E4%BD%BF%E7%94%A8%E7%A4%BE%E5%8C%BA%E5%8F%91%E7%8E%B0%E7%AE%97%E6%B3%95%E4%BB%8E%E4%BC%81%E4%B8%9A%E5%86%85%E9%83%A8%E6%97%A0%E6%95%88%E5%9F%9F%E5%90%8D%E4%B8%AD%E6%8C%96%E6%8E%98DGA/)

