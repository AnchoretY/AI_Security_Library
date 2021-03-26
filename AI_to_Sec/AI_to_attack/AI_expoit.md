## 渗透测试



### Blog

1. [Automatic Generation of Injection Codes using Genetic Algorithm](https://www.mbsd.jp/blog/20170921.html)

日本MBSD公司使用遗传算法进行XSS注入攻击。

### 论文

1. 《The Agent Web Model—Modelling web hacking for reinforcement learning》
2. 《Modeling penetration testing with reinforcement learning using capture-the-flag challenges and tabular Q-learning.》
3. 《Reinforcement learning for efficient network penetration testing.》
4. 《Adversarial reinforcement learning in a cyber security simulation》2018 博士论文
5. 《Using Markov decision processes and reinforcement learning to guide penetration testers in the search for web vul- nerabilities》2019
6. 《Smart security audit: Reinforcement learning with a deep neural network approximator.》2020
7. 《Reinforcement Learning for Intelligent Penetration Testing》2018
8. 《Simulated Penetration Testing and cMitigation Analysis》
9. 《Automated penetration testing based on a threat model》2016 
10. 《Attack planning in the real world》 2013

11. 《Automatic generation algorithm of penetration graph inpenetration testing》2014 攻击图决策树



### 相关竞赛

1. **Cyber Grand Challenge Event  2016**  **DARPA**





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

&emsp;&emsp;使用强化学习来混淆sql payload使其能够绕过WAF检测的项目。

![image](https://raw.githubusercontent.com/AnchoretY/images/master/blog/image.bewohm1fvh.png)



3. ####
