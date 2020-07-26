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

   &emsp;&emsp;蚂蚁金服在研究**只有少量已经标注的正样本和大量无标注样本时**，使用PU-Learning（Positive Unlabled Learning）进行恶意URL检测的原理、效果介绍。**核心**就是其中PU-Learning的具体做法，使用**two-stage strategy**（两个阶段，先进行训练模型，然后根据已有数据找阈值将数据进行标注）和**cost-sensitive strategy**（正例与负例误分类采用不同惩罚系数的损失函数），声称已经通过这个模型发现了新的攻击模式，值得尝试一下的策略。

10. #### [AI in WAF | 腾讯云网站管家 WAF AI 引擎实践](https://www.freebuf.com/articles/web/179436.html)

    &emsp;&emsp;腾讯网站管家WAF在AI WAF方向的实践经验，本文不包含一些具体的技术细节，主要是构建AI WAF的一些大体思路。1.提出降低漏报、误报的思路：two-stage法，第一阶段使用无监督的聚类来进行异常检测（声称可以实时，但是聚类如何进行实时，推测是一个准实时的算法），然第二阶段使用监督学习的方式来将第一阶段监测为异常的作为黑样本数据来进行模型训练。    

### Paper

1. Davide, Ariu, and, et al. "HMMPayl: An intrusion detection system based on Hidden Markov Models[J]" [pdf](https://www.sciencedirect.com/science/article/pii/S0167404811000022).**(HMM用于Web参数检测**)