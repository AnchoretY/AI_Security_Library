AI_And_Web_Security_Library

&emsp;&emsp;Ai与Web安全相关资料的总结库，并附上自身对各个资料内容的总结与看法，不定期更新。

## 近期更新
#### 2020.7.1
&emsp;&emsp;[WAF建设运营及AI应用实践](https://mp.weixin.qq.com/s?__biz=MjM5NzE1NjA0MQ==&mid=2651199346&idx=1&sn=99f470d46554149beebb8f89fbcb1578&chksm=bd2cf2d48a5b7bc2b3aecb501855cc2efedc60f6f01026543ac2df5fa138ab2bf424fc5ab2b0&scene=21#wechat_redirect)

#### 2020.7.2
&emsp;&emsp;[门神WAF众测总结](https://mp.weixin.qq.com/s/w5TwFl4Ac1jCTX0A1H_VbQ)

#### 2020.7.15
&emsp;&emsp;[基于PU-Learning的恶意URL检测](https://xz.aliyun.com/t/2190)



## 资料

1. [华为AI安全白皮书]https://github.com/AnchoretY/AI_And_Web_Security_Library/blob/master/book/ai-security-white-paper-cn.pdf



## Webshell

### 项目

1. #### [WebShell-Detector](https://github.com/flykingmz/WebShell-Detector)

    &emsp;&emsp;全称《基于深度学习与集成学习的可配置webshell检测系统》，是08年大学生信息安全竞赛的一个Webshell检测系统，主要是是**针对Webshell文件**进行检测，采用的方式基本上是比较传统的**静态检测（正则+机器学习）+动态检测技术（深度学习）**的进行检测，然后使用**加权的方式对模型进行组合**，是一个比较基础的实现。

2. #### [CloudWalker](https://github.com/chaitin/cloudwalker)

 &emsp;&emsp;**长亭科技在线的Webshell文件检测项目**，可以本地检测也可以线上检测。

### 数据集

1. #### [webshell-sample](https://github.com/ysrc/webshell-sample)

&emsp;&emsp;&emsp;各种**webshell文件数据**，根据webshell文件类型进行分类，量很大。

2. #### [tennc/webshell](https://github.com/tennc/webshell)

   &emsp;&emsp;一个比较大的的webshell文件收集项目。

### Blog

1. #### [基于机器学习的分布式webshell检测系统-特征工程](https://www.s0nnet.com/archives/fshell-feature-1)

   &emsp;&emsp;该文章主要对采用机器学习方式进行Webshell检测特征选取做出了一系列的总结，包括了**基于日志、基于统计学分析、基于文件的文本属性**三个角度的特征提取过程，还是比较有借鉴意义的一篇文章，作者还提供了实现的[github](https://github.com/Lingerhk/fshell)项目，在实际使用过程中可根据实际情况进行特征的选取。其中比较有借鉴意义的特征包括：

   - parameter的熵值
   - url访问频率
   - parameter的key出现的频率
   - parameter的key关联的页面数
   - 采用fuzz hashing与已知黑名单进行相似度匹配

2. #### [初探机器学习检测 PHP Webshell](https://paper.seebug.org/526/)

   &emsp;&emsp;对PHP Webshell使用opcode作为特征朴素贝叶斯算法进行检测，非常详细的讲解。

## XSS

###  项目



### 数据集

1. #### [xss_payload_2016](https://github.com/7ioSecurity/XSS-Payloads)

&emsp;&emsp;纯xss payload总结，不带任何其他信息

2. #### [xssdb](http://xssdb.net/)

&emsp;&emsp;一个xss payload网络数据库，数据量比较大而且除payload外，还包含了每条payload的相关信息，例如注入名称、描述等，并支持以csv、txt、json等多种形式进行导出。

### 检测规则



## DGA域名检测



### Paper&Blog

1. Hyrum S. Anderson, Jonathan Woodbridge, Bobby Filar. "DeepDGA: Adversarially-Tuned Domain Generation and Detection" [[pdf\]](https://arxiv.org/abs/1610.01969),6 Oct 2016 **(生成对抗网络，DGA检测)** 
2. Jonathan Woodbridge, Hyrum S. Anderson, Anjum Ahuja, Daniel Grant. "Predicting Domain Generation Algorithms with Long Short-Term Memory Networks" [[pdf\]](https://arxiv.org/abs/1611.00791),2 Nov 2016 **(LSTM,DGA检测)**



## 入侵检测

### 项目

1. #### [Seq2Seq for Web Attack Detection](https://github.com/flykingmz/seq2seq-web-attack-detection)

  &emsp;&emsp;使用某银行应用中的数据集进行HTTP Web攻击检测模型项目。该项目检测对象为**HTTP流量**，具有的一个比较特别的点是在**训练阶段不使用攻击样本，而只使用正常样本**，是一种类似异常检测思路，而不是大部分人使用的分类的方式。

2. #### [Sharly](https://github.com/SparkSharly/Sharly)

  &emsp;&emsp;**基于HMM的Web异常参数检测项目**。

### 数据集

1. ####  [Vulnbank_dataset](https://github.com/AnchoretY/AI_And_Web_Security_Library/tree/master/dataset/vulnbank_dataset)

   &emsp;&emsp;KDD大赛的一个竞赛项目，主要目的是使用机器学习得手段建立一个入侵检测器。其中的入侵行为主要包括：DDOS、密码暴力破解、缓冲区溢出、扫描等多种攻击行为。**数据格式为一些基本的统计信息**。

2. #### [KDD CUP 1999 Data]()

3. #### [SecRepo.com](https://www.secrepo.com/)

&emsp;&emsp;一个总结各种与安全数据相关的数据集的网站。**数据格式也非常多样**。

### Blog

1. #### [Web日志安全分析系统实践](https://xz.aliyun.com/t/2136#toc-110)

   &emsp;&emsp;该博客一个比较全面的HTTP流量日志分析系统，是一个比较详细的系统设计，检测部分包括了规则匹配、统计特征检测、机器学习检测三种方法，**机器学习部分采用了tf-idf+ngram等方式进行向量化然后使用SVM进行检测**。是一种非常基础非常简单的安全和AI结合的实践。

2. #### [数据科学在Web威胁感知中的应用](https://www.jianshu.com/p/942d1beb7fdd)

   &emsp;&emsp;楚安大佬在AI安全领域的一篇非常经典的博客。

3. #### [学点算法搞安全之HMM](https://www.freebuf.com/column/132796.html)

   &emsp;&emsp;兜哥写的一篇关于**HMM用于Web参数异常检测**的一篇论述性的文章，并附带了一些基本实现。HMM应用于Web参数异常检测核心思想为使用大量白样本构建HMM模型，使模型能够正确识别正常参数的形式，然后对于新的请求参数使用该HMM模型进行判别，根据得出的概率值判断是否为异常参数。在实际使用中存在的问题也比较明显，**HMM模型要每个URL都要训练一个HMM模型，因此检测的成本巨大，只能用于小站点的防护。**

4. #### [机器学习在Web攻击检测中的应用](https://mp.weixin.qq.com/s/Fuu70rPWyYP5mQSOK3J9_Q)

   &emsp;&emsp;该博客为写成在**将机器学习应用到携程的恶意攻击检测系统中的企业实践**，整个文章论述了将机器学习应用到入侵检测系统中的整体思路以及遇到的各种问题及解决方法。里面一些比较精彩的点：

   - 该文章**将机器学习模型主要用来做效率优化**，构建低误报的模型来进行数据的过滤，然后再使用正则进行确定是否为攻击。

   - 整个系统先使用白名单机制来过滤掉97%的流量。在**param的value部分不包含符号、控制符以及白名单IP的流量都可直接视为白数据**。

   - 机器学习和正则都判为黑的发送到**自动化验证系统验证能否攻击成功**。

5. #### [企业安全数据分析实践与思考]()

      &emsp;&emsp;阿里cdxy大神关于阿里巴巴在将数据分析技术应用到企业安全中的一些思路的分享ppt，配套讲解[视频](https://live.freebuf.com/detail/c5e504cf96a4e1826a609553bf6054f9)。里面有一些做法还是比较特别的。

      - **多层日志进行协同**进行是否**成功入侵判别**。
      - **多层日志协同**进行自动化事件完整过程建模，快速追踪（**入侵链路可视化**）。
      - **随着数据的积累，安全数据分析将基于图结构的高级知识表达方式发展**。
      
6. #### [利用机器学习检测HTTP恶意外连流量](https://www.freebuf.com/column/170483.html)

      360云影实验室
      
7. #### [WAF建设运营及AI应用实践](https://mp.weixin.qq.com/s?__biz=MjM5NzE1NjA0MQ==&mid=2651199346&idx=1&sn=99f470d46554149beebb8f89fbcb1578&chksm=bd2cf2d48a5b7bc2b3aecb501855cc2efedc60f6f01026543ac2df5fa138ab2bf424fc5ab2b0&scene=21#wechat_redirect)
  &emsp;&emsp;本文较为透彻的讲解了**腾讯在进行WAF建设的思路、部署位置等，并且讲述了AI在整个WAF系统中所起的作用**。其中比较记忆深刻的点：1.在流量到来时，应当使用多种方式来对流量进行初筛，流量中正常流量与恶意流量的比例为10000：1，应当**先过滤掉绝对正常的流量**。提到的方法为：先过滤掉公司自己的出口IP，再过敏感攻击特征关键字进行字符串匹配，筛选出疑似流量。   2.对于xss这类语法较为明显的攻击，采用**antlr4**作为词法分析器和文法分析器进行分析，判断是否符合语法。   3.**对于判断符合js语法的请求进一步使用hmm来进行打分，判断是否为xss攻击**
  
8. #### [门神WAF众测总结](https://mp.weixin.qq.com/s/w5TwFl4Ac1jCTX0A1H_VbQ)
   &emsp;&emsp;**腾讯门神WAF进一步完善的一个众测策略，比较有借鉴意义的一个WAF完善方式**。文章中比较详细的分析了整个众测过程中成功绕过门神WAF的各种攻击，对这些攻击按照攻击所**针对防御策略预处理阶段、词法分析阶段、语法分析等不同阶段进行分析**，但是并为直接给出完善措施，需要自己去思考。
   
   
9. #### [基于PU-Learning的恶意URL检测](https://xz.aliyun.com/t/2190)
    &emsp;&emsp;蚂蚁金服在研究**只有少量已经标注的正样本和大量无标注样本时**，使用PU-Learning进行恶意URL检测的原理、效果介绍。**核心**就是其中PU-Learning的具体做法，使用**two-stage strategy**（两个阶段，先进行训练模型，然后根据已有数据找阈值将数据进行标注）和**cost-sensitive strategy**（正例与负例误分类采用不同惩罚系数的损失函数），声称已经通过这个模型发现了新的攻击模式，值得尝试一下的策略。

### Paper

1. Davide, Ariu, and, et al. "HMMPayl: An intrusion detection system based on Hidden Markov Models[J]" [pdf](https://www.sciencedirect.com/science/article/pii/S0167404811000022).**(HMM用于Web参数检测**)

   

## 渗透测试

### 项目

1. #### [GyoiThon](https://github.com/gyoisamurai/GyoiThon)

   &emsp;&emsp;一款**基于机器学习得自动化渗透测试工具**，该工具可以根据**响应包中的cookie、Etag、特定HTML标签等方面训练一个机器学习模型识别出服务器端软件**，然后调用**Metasploit**进行渗透测试。这里还有一篇详细的[使用介绍](https://www.freebuf.com/sectool/173476.html)

2. #### [Deep Exploit](https://github.com/13o-bbr-bbq/machine_learning_security/tree/master/DeepExploit)

   使用深度强化学习进行自动化渗透测试工具。

### Paper





## UEBA

1. #### [唯品会UEBA架构之路系列](https://www.secpulse.com/archives/95668.html)

   ​	比较详细的描述唯品会安全团队UEBA建设的架构以及实现的一些关键点，系列包含了9篇文章，是很具有借鉴意义的系列文章。其中比较好的一些思路有：

   - **域名的白名单**可以根据访问用户的数量**动态建立**，访问的用户数量很大域名加入白名单。
   - 图算法的应用

2. #### [用机器学习检测异常点击流](https://blog.csdn.net/mergerly/article/details/77985089)





## 加密流量检测

### Blog

1. #### [一篇报告了解国内首个针对加密流量的检测引擎](https://mp.weixin.qq.com/s/HTrQ5BK-mhXfJmMlwHD04w)

   观成科技

2. #### [恶意软件加密通信概要分析](https://mp.weixin.qq.com/s/8nnfSjPVmWbThKrSlqNriQ)

   观成科技

3. ####  [火眼金睛：利用机器学习识别加密流量中的恶意软件](https://mp.weixin.qq.com/s/qngs8-jjHVcdMco1MQfs9Q)

   思科在加密流量检测中的检测方案

4. #### [基于机器学习的恶意软件加密流量检测研究分享]([https://blog.riskivy.com/%E5%9F%BA%E4%BA%8E%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0%E7%9A%84%E6%81%B6%E6%84%8F%E8%BD%AF%E4%BB%B6%E5%8A%A0%E5%AF%86%E6%B5%81%E9%87%8F%E6%A3%80%E6%B5%8B/](https://blog.riskivy.com/基于机器学习的恶意软件加密流量检测/))

   斗象科技

5. #### [特征工程之加密流量安全检测](https://www.secrss.com/articles/12415)


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



 
