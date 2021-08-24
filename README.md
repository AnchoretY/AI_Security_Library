# AI_And_Security_Library

&emsp;&emsp;Ai与安全相关资料的总结库，并附上自身对各个资料内容的总结与看法，不定期更新。

## 分类

主要关注的文章类型包括使用AI技术解决下面的安全问题:

#### AI赋能安全

1. AI辅助防御
   - [AI IDS](./AI_to_Sec/AI_to_defense/Web/AI_IDS.md)
     - [Webshell检测](./AI_to_Sec/AI_to_defense/Web/webshell.md)
     - [XSS检测](./AI_to_Sec/AI_to_defense/Web/XSS.md)
     - 恶意域名检测
       - [DGA域名检测](./AI_to_Sec/AI_to_defense/Web/mal_domain_detection/mal_domain_detection.md)
     - [加密恶意流量检测](./AI_to_Sec/AI_to_defense/Web/encrypted_mal_traffic_detection/encrypted_mal_traffic_detection.md)
     - [扫描器检测](./AI_to_Sec/AI_to_defense/Web/Scan.md)
     - 僵尸网络检测
   - 恶意代码
     - 恶意软件检测

2. AI辅助攻击
   - [AI辅助渗透测试](./AI_to_Sec/AI_attack/AI_exploit.md)
   - [漏洞挖掘](./AI_to_Sec/AI_attack/AI_Vulnerability_Mining.md)
   - [AI辅助恶意软件混淆](./AI_to_Sec/AI_attack/AI_mal_evasion.md)

3. 异常检测
   - [UEBA](./AI_to_Sec/AI_to_OD/UEBA.md)

#### AI自身的安全问题

1. 对抗攻击

2. 后门攻击

3. 数据投毒

4. 模型窃取

   

## 近期更新

#### 2021.8.24

【恶意软件检测】Malware Detection by Eating a Whole EXE【AAAI workshop, 2018】

【恶意软件检测】HYDRA- A Multimodal Deep Learning Framework for Malware Classification`待更新`【2020】

【恶意软件检测】Zero-day malware detection using transferred generative adversarial networks based on deep autoencoders`待更新`【Information Sciences，2018】

#### 2021.5.12

【入侵检测基础】[中传信安网络安全wiki课本](https://c4pr1c3.gitee.io/cuc-ns/chap0x09/main.html)

【IDS】[Use Model to Deconstruct Threats: Detect Intrusion by Statistical Learning](https://published-prd.lanyonevents.com/published/rsaus19/sessionsFiles/13922/AIR-F01-Use-Model-to-Deconstruct-Threats-Detect-Intrusion-by-Statistical-Learning-FINAL.pdf)【阿里，RSA 2019】

【课程】[网络异常行为分析](https://www.aqniukt.com/goods/show/163?targetId=353&preview=0)

【课程】[加密威胁事件检测与响应实践](https://www.aqniukt.com/goods/show/428?targetId=11731&preview=0)

【webshell,污点传播理论】[洋葱webshell检测实践与思考](https://www.freebuf.com/articles/system/238691.html)

#### 2021.5.6

【malware】[SIGL: Securing Software Installations Through Deep Graph Learning](https://www.usenix.org/system/files/sec21summer_han-xueyuan.pdf)`待更新`【unisex,2020】

【theory】[CADE: Detecting and Explaining Concept Drift Samples for Security Applications](https://www.usenix.org/conference/usenixsecurity21/presentation/yang-limin)`待更新`【unisex,2020】

【email】[Weak Links in Authentication Chains: A Large-scale Analysis of Email Sender Spoofing Attacks]()`待更新`【清华，usenix,2020】

【IDS】[ATLAS: A Sequence-based Learning Approach for Attack Investigation]()`待更新`【】

【IDS】[Defeating DNN-Based Traffic Analysis Systems in Real-Time With Blind Adversarial Perturbations](https://www.usenix.org/conference/usenixsecurity21/presentation/nasr)s

#### 2021.4.30

【IDS】[Use Model to Deconstruct Threats: Detect Intrusion by Statistical Learning](AI_to_Sec/AI_to_defense/Web/AI_IDS.md) 【RSA 2019】

【IDS】[MADE: Security Analytics for Enterprise Threat Detection](AI_to_Sec/AI_to_defense/Web/AI_IDS.md)

#### 2021.4.8

[网络攻防新前沿：加密流量对抗](https://www.secrss.com/articles/12314)

#### 2021.3.11

Classification of Malicious Web Code by Machine Learning - Komiya et al.

SQL Injection Detection using Machine Learning

SQLiGoT: Detecting SQL injection attacks using graph of tokens and SVM

#### 2021.3.7

VulDeePecker:ADeep Learning-Based System for Vulnerability Detection.

Automated vulnerability detection in source code using deep representation learning.2018

Neural network-based graph embedding for cross-platform binary code similarity detection。

Modeling and discovering vulnerabilities with code property graphs.2014

#### 2021.3.3

[浅谈DDoS攻防对抗中的AI实践](https://security.tencent.com/index.php/blog/msg/144)

[AI繁荣下的隐忧——Google Tensorflow安全风险剖析](https://security.tencent.com/index.php/blog/msg/130)

#### 2021.2.25

[Adversarial Malware in Machine Learning Detectors: Our MLSEC 2020’s SECRETs](https://secret.inf.ufpr.br/2020/09/29/adversarial-malware-in-machine-learning-detectors-our-mlsec-2020-secrets/#defenders)`待更新`

【github】[2020 Machine Learning Security Evasion Competition](https://github.com/Azure/2020-machine-learning-security-evasion-competition)

【kaggle】[Microsoft Malware Prediction](https://www.kaggle.com/c/microsoft-malware-prediction/code)



#### 2021.1.25

[图卷积神经网络在企业侧网络安全运营中的应用](https://mp.weixin.qq.com/s?__biz=MzIyODYzNTU2OA==&mid=2247488182&idx=1&sn=c94808f60a30779d414d85aa07a10e8a&chksm=e84fb469df383d7f4f9f76b42b618bef698bf37b022f7eec5e1bcf91ed61fc1c6c0a38bcfac7&scene=21#wechat_redirect)

[基于机器学习的敏感信息泄露治理探索](https://mp.weixin.qq.com/s/9ZOSyPJdyxgrbsY4FIvgXw)

#### 2020.12.10

[探秘-基于机器学习的DNS隐蔽隧道检测方法与实现](https://blog.riskivy.com/探秘-基于机器学习的dns隐蔽隧道检测方法与实现/)`待更新`

[基于机器学习的Webshell检测方法与实现（上）](https://blog.riskivy.com/基于机器学习的webshell检测方法与实现（上）/)`待更新`

#### 2020.9.22

&emsp;&emsp;[Webshell检测——日志分析](http://www.91ri.org/14841.html)`待更新`

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
&emsp;&emsp;【DGA域名检测】[使用社区发现算法从企业内部无效域名中挖掘DGA](http://webber.tech/posts/%E4%BD%BF%E7%94%A8%E7%A4%BE%E5%8C%BA%E5%8F%91%E7%8E%B0%E7%AE%97%E6%B3%95%E4%BB%8E%E4%BC%81%E4%B8%9A%E5%86%85%E9%83%A8%E6%97%A0%E6%95%88%E5%9F%9F%E5%90%8D%E4%B8%AD%E6%8C%96%E6%8E%98DGA/) 


#### 2020.7.31

&emsp;&emsp;【论文】[Manos Antonakakis, Damballa Inc. and Georgia Institute of Technology. "From Throw-Away Traffic to Bots: Detecting the Rise of DGA-Based Malware",2012. (DGA,图，谱聚类)](https://www.usenix.org/system/files/conference/usenixsecurity12/sec12-final127.pdf)`待更新`


#### 2020.8.13
&emsp;&emsp;[DNS安全皮毛](https://xz.aliyun.com/t/5991)


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

3. #### [Log Parser](https://www.microsoft.com/en-us/download/details.aspx?id=24659)

&emsp;&emsp;Log Parser是微软公司出品的日志分析工具，它功能强大，使用简单，可以分析基于文本的日志文件、XML 文件、CSV（逗号分隔符）文件，以及操作系统的事件日志、注册表、文件系统、Active Directory。它可以像使用 SQL 语句一样查询分析这些数据，甚至可以把分析结果以各种图表的形式展现出来。

~~~sql
Logparser.exe –i:EVT –o:DATAGRID "SELECT * FROM c:\xx.evtx"
~~~

&emsp;&emsp;更多的实例可以看[这里](https://mlichtenberg.wordpress.com/2011/02/03/log-parser-rocks-more-than-50-examples/)

