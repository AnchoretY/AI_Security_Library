**AI_And_Web_Security_Library**

&emsp;&emsp;Ai与Web安全相关资料的总结库，并附上自身对各个资料内容的总结与看法，不定期更新。

## 分类

主要关注的文章类型包括使用AI技术解决下面的安全问题:

1. [Webshell](./webshell/webshell.md)

2. [DGA](./mal_domain_detection/mal_domain_detection.md)

3. [加密恶意流量检测](encrypted_mal_traffic_detection/encrypted_mal_traffic_detection.md)

4. [入侵检测](./AI_IDS/AI_IDS.md)

5. [UEBA](UEBA/UEBA.md)

6. [XSS](./XSS/XSS.md)

7. [渗透测试](AI_exploit/AI_exploit.md)

8. [扫描器检测](./Scan/Scan.md)

    

## 近期更新

#### 2020.9.22 
&emsp;&emsp;[Webshell检测——日志分析]（http://www.91ri.org/14841.html）`待更新`

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
&emsp;&emsp;[使用社区发现算法从企业内部无效域名中挖掘DGA](http://webber.tech/posts/%E4%BD%BF%E7%94%A8%E7%A4%BE%E5%8C%BA%E5%8F%91%E7%8E%B0%E7%AE%97%E6%B3%95%E4%BB%8E%E4%BC%81%E4%B8%9A%E5%86%85%E9%83%A8%E6%97%A0%E6%95%88%E5%9F%9F%E5%90%8D%E4%B8%AD%E6%8C%96%E6%8E%98DGA/) `待更新`


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





