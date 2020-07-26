## 恶意域名检测

 &emsp;&emsp;现今恶意软件大多采用DGA生成域名的方式来进行域名的生成，因此这里将DGA和恶意域名统称为恶意域名。

### Paper&Blog

1. Hyrum S. Anderson, Jonathan Woodbridge, Bobby Filar. "DeepDGA: Adversarially-Tuned Domain Generation and Detection" [[pdf\]](https://arxiv.org/abs/1610.01969),6 Oct 2016 **(生成对抗网络，DGA检测)** 
2. Jonathan Woodbridge, Hyrum S. Anderson, Anjum Ahuja, Daniel Grant. "Predicting Domain Generation Algorithms with Long Short-Term Memory Networks" [[pdf\]](https://arxiv.org/abs/1611.00791),2 Nov 2016 **(LSTM,DGA检测)**

### Blog

#### [机器学习与威胁情报的融合：一种基于AI检测恶意域名的方法](https://www.freebuf.com/articles/es/187451.html)

  &emsp;&emsp;改文章基于购买的微步的威胁情报中包含的恶意域名作为恶意黑样本构建的恶意域名检测模型，其中采用的一些对比较经典的特征，最终模型**误报率和漏报率均在3%左右**，整体效果还是一般。有构建这方面模型的道友可以将其作为base在其上进行进一步的完善。其中包含的主要特征包括：**Alexa排名、搜狗rank、搜狗与百度的收录数量、必应收录数量、网站首页完整度、是否是主流域名后缀、地理位置、地理位置**。

  其实对于在微步购买的威胁情报中所包含的恶意域名，文章作者已经认识到其标记并不准确，其中也存在包含了alex排名前1000的域名等问题，但是作者并没有在构建训练集时将这些有问题的数据进行剔除，在进行相关任务时应该注意样本集的清洗。

