AI_And_Web_Security_Library

&emsp;&emsp;Ai与Web安全相关资料的总结库，并附上自身对各个资料内容的总结与看法，不定期更新。

## 近期更新

#### 2020.7.1
&emsp;&emsp;[WAF建设运营及AI应用实践](https://mp.weixin.qq.com/s?__biz=MjM5NzE1NjA0MQ==&mid=2651199346&idx=1&sn=99f470d46554149beebb8f89fbcb1578&chksm=bd2cf2d48a5b7bc2b3aecb501855cc2efedc60f6f01026543ac2df5fa138ab2bf424fc5ab2b0&scene=21#wechat_redirect)

#### 2020.7.2
&emsp;&emsp;[门神WAF众测总结](https://mp.weixin.qq.com/s/w5TwFl4Ac1jCTX0A1H_VbQ)

#### 2020.7.15
&emsp;&emsp;[基于PU-Learning的恶意URL检测](https://xz.aliyun.com/t/2190)

#### 2020.7.16
&emsp;&emsp;[在网络安全领域应用机器学习的困难和对策](https://www.freebuf.com/articles/neopoints/234939.html) `待更新`

#### 2020.7.17
&emsp;&emsp;[机器学习与威胁情报的融合：一种基于AI检测恶意域名的方法](https://www.freebuf.com/articles/es/187451.html)  
&emsp;&emsp;[AI in WAF | 腾讯云网站管家 WAF AI 引擎实践](https://www.freebuf.com/articles/web/179436.html)

#### 2020.7.21

&emsp;&emsp;【工具】[publicsuffixlist]()
&emsp;&emsp;【工具】[Gibberish-Detector](https://github.com/rrenaud/Gibberish-Detector)  
&emsp;&emsp;[使用社区发现算法从企业内部无效域名中挖掘DGA](http://webber.tech/posts/%E4%BD%BF%E7%94%A8%E7%A4%BE%E5%8C%BA%E5%8F%91%E7%8E%B0%E7%AE%97%E6%B3%95%E4%BB%8E%E4%BC%81%E4%B8%9A%E5%86%85%E9%83%A8%E6%97%A0%E6%95%88%E5%9F%9F%E5%90%8D%E4%B8%AD%E6%8C%96%E6%8E%98DGA/)



主要关注的文章类型包括使用AI技术解决下面的安全问题:

1. [Webshell](./webshell/webshell.md)
2. [DGA](./mal_domain_detection/mal_domain_detection.md)
3. [加密恶意流量检测](encrypted_mal_traffic_detection/encrypted_mal_traffic_detection.md)
4. [入侵检测](./IDS/IDS.md)
5. [UEBA](UEBA/UEBA.md)
6. [XSS](XSS/XSS.md)
7. 渗透测试

## 资料

1. [华为AI安全白皮书]https://github.com/AnchoretY/AI_And_Web_Security_Library/blob/master/book/ai-security-white-paper-cn.pdf



## 工具
1. #### [Gibberish-Detector](https://github.com/rrenaud/Gibberish-Detector)
  &emsp;&emsp;一个使用2字符级别的马尔科夫链进行乱码检测的项目，在安全领域可以使用该项目进行DGA域名检测的辅助工具。
  
2. #### [publicsuffixlist]()
  &emsp;&emsp;FireFox发布的共有顶级域名列表构成的列表项目，可以直接使用pip进行安装，直接输入域名，如果在官方发布的顶级域名列表中返回顶级域名，如果不在返回None。  
  ~~~
    from publicsuffixlist import PublicSuffixList
    
    psl = PublicSuffixList(accept_unknown=False)    # accept_unknown设置为False不接受不在官方列表中的顶级域名
    
    psl.publicsuffix("www.ssss.com")    # 返回“com”
    psl.publicsuffix("www.ffff.sssss")  # 返回None
  ~~~



 

## 渗透测试

### 项目

1. #### [GyoiThon](https://github.com/gyoisamurai/GyoiThon)

   &emsp;&emsp;一款**基于机器学习得自动化渗透测试工具**，该工具可以根据**响应包中的cookie、Etag、特定HTML标签等方面训练一个机器学习模型识别出服务器端软件**，然后调用**Metasploit**进行渗透测试。这里还有一篇详细的[使用介绍](https://www.freebuf.com/sectool/173476.html)

2. #### [Deep Exploit](https://github.com/13o-bbr-bbq/machine_learning_security/tree/master/DeepExploit)

   使用深度强化学习进行自动化渗透测试工具。

### Paper









5. #### 


## DNS隐蔽信道
### Blog
#### 1. [DNS Tunnel隧道隐蔽通信实验 && 尝试复现特征向量化思维方式检测](https://www.cnblogs.com/LittleHann/p/8656621.html#_label3_1_4_0)
&emsp;&emsp;阿里云的在进行DNS隐蔽信道时写的一篇记录文章，文章中首先比较系统的讲述了`IP直连型DNS隐蔽信道、域名型因隐蔽信道两种常见的隐蔽信道`，然后`使用Powershell+dnscat2实现DNS隐蔽隧道反弹Shell进行实际的隐蔽信道木马搭建，获取通信过程的隐蔽信道流量进行分析`，最后`非常全面的讲述了进行DNS隐蔽信道检测可以采用的特征`，其中的`ZIf定律、FQDN数`等都是非常新颖的特征，是一篇做DNS隐蔽信道检测难得的好文。

&emsp;&emsp;在该文章中还提到了在DNS隐蔽信道检测的实际应用中的一个比较核心的问题：`如何区分DNS隐蔽信道和DNS Flood攻击`。

> 1. ZIf定律
>
> &emsp;&emsp;`根据Zif定律，在自然语言的语料库里，词频往往会集中于某些小子集中，并且高频词到低频次的频率逐渐下降`。而在DNS Tunneling中由于域名做了编码，不符合Zipf定律，整个分布趋于平稳。因此可以通过`通过检测排序后的词频平均斜率`来检测input string是否符合zipf law规律。
>
> 2. FQDN
>
> &emsp;&emsp;域名有全称和简称的区别。全称的域名，直译为"完全的合格的域名"(FQDN，Fully Qualified Domain Name)，表现为由"·"隔开的点分式层次结构，叫名称空间， 它指定了一台主机和它所属域的隶属关系，而简称通常就是这台主机的计算机名，在域名的最左边。`FQDN(完全合格的域名)，是域加计算机名的总称`。比如: www.microsoft.com 这个FQDN 中，www 是主机名，microsoft.com 是域。 www+microsoft.com 组合在一块就成了一个完整的域名(FQDN)。可以通过分析一定时间窗口内所产生的FQDN数，`通常DNS Tunneling的FQDN数在一定时间窗口内会远高于正常的DNS流量`。

