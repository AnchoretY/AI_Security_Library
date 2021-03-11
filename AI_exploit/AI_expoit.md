## 渗透测试



### Blog

1. **[AAAI-20论文解读：基于图神经网络的二进制代码分析](https://keenlab.tencent.com/zh/2019/12/10/Tencent-Keen-Security-Lab-Order-Matters/)**

   科恩实验室在使用图神经网络进行大规模二进制代码相似性分析的成果，发布在人工智能顶级会议AIII-20上。

2. [Automatic Generation of Injection Codes using Genetic Algorithm](https://www.mbsd.jp/blog/20170921.html)

   日本MBSD公司使用遗传算法进行XSS注入攻击。

### 论文

1. Finding Bugs Using Your Own Code: Detecting Functionally-similar yet Inconsistent Code

   *Northeastern University*使用graph-embedding对



【2】[Order Matters: Semantic-Aware Neu for Binary Code Similarity Detection](https://keenlab.tencent.com/en/whitepapers/Ordermatters.pdf)



### 项目

1. #### [GyoiThon](https://github.com/gyoisamurai/GyoiThon)

   &emsp;&emsp;一款**基于机器学习得自动化渗透测试工具**，该工具可以根据**响应包中的cookie、Etag、特定HTML标签等方面训练一个机器学习模型识别出服务器端软件**，然后调用**Metasploit**进行渗透测试。这里还有一篇详细的[使用介绍](https://www.freebuf.com/sectool/173476.html)

2. #### [Deep Exploit](https://github.com/13o-bbr-bbq/machine_learning_security/tree/master/DeepExploit)

   使用深度强化学习进行自动化渗透测试工具,使用强化学习来对metsploit中的payload进行选择。404NotFoud对这个工具做出了很专业的分析，需要的朋友可以点击[这里](https://4o4notfound.org/index.php/archives/215/)。
   
   

3. #### [DeepGenerator](https://github.com/13o-bbr-bbq/machine_learning_security/tree/master/Generator)

   &emsp;&emsp;使用**GA(遗传算法)**和**GAN**来**自动生成针对网络应用的注入攻击（目前只是xss）的payload的工具**，使用该工具可以自动产生全新的，可以绕过WAF检测的注入攻击payload。注入攻击生成的流程如下：

   1. 收集注入代码攻击代码个部分的可选项。
   2. 使用遗传算法创建少量注入攻击payload。
   3. 使用遗传算法产生的少量样本输入到GAN中生成大量攻击payload样本。

   &emsp;&emsp;遗传算法的使用具体使用在[这里](https://www.mbsd.jp/blog/20170921.html)，其核心思想为首先搜集各种html和javascript代码，然后将其切分为最小的组成成分，作为基因，然后随机组合形成个体，**根据每个个体的html结构完整性、js语义合理性和是否能够绕过WAF进行注入攻击进行评分**，淘汰其中评分过低的个体，剩余的个体进行部分基因的随机交换，最后在随机选择一部个体进行基因突变（随机更换其中的基因），不断重复这个过程，最终即可生成全新的、可绕过WAF的样本。在作者的实验中，作者使用了349次迭代才产生了具有合理语法结构的样本，6307次迭代后首次产生能够成功绕过WAF的注入攻击。

   &emsp;&emsp;使用GAN进行大量攻击样本生成的过程作者并没有做详细介绍。

   ![image](https://raw.githubusercontent.com/AnchoretY/images/master/blog/image.l48tlxvk09b.png)

4. #### PyRecommender

&emsp;&emsp;**使用从已有xss攻击payload**中**推荐可用攻击payload的工具**，该工具优先使用一定对目标系统进行访问，然 

![image](https://raw.githubusercontent.com/AnchoretY/images/master/blog/image.zj3efxzi9p8.png)

5. #### [WAF Evasion Environment for OpenAI Gym](https://github.com/SaneBow/gym-waf)

&emsp;&emsp;使用强化学习来混淆xss payload使其能够绕过WAF检测的项目，作者的实验中可以达到40%左右的成果绕过率。

![image](https://raw.githubusercontent.com/AnchoretY/images/master/blog/image.bewohm1fvh.png)



3. #### [Adversarial-Threat-Detector](https://github.com/gyoisamurai/Adversarial-Threat-Detector)

&emsp;&emsp;2021年黑帽黑客大会上提出出的AI对抗威胁检测器，检测器主要分为下面四步：

1. 检测器首先通过执行大量已知的攻击攻击待检测的分类模型，观察模型是否成功被攻击

2. 对攻击攻击的情况生成脆弱性报告以及重播该漏洞的ipynb文件（供研究人员了解该漏洞）

3. 自动修复（当前还是人工修复）

4. 对修复漏洞后的模型重新进行检测

&emsp;&emsp;目前，该工具还只支持keras的Evasion攻击。主讲人说后续会持续加入数据投毒攻击、模型投毒、模型窃取等攻击方式的检测。

![image](https://raw.githubusercontent.com/AnchoretY/images/master/blog/image.8kp1i4nl69.png)