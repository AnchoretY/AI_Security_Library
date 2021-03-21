

### 工具

#### [Adversarial-Threat-Detector](https://github.com/gyoisamurai/Adversarial-Threat-Detector)

&emsp;&emsp;2021年黑帽黑客大会上提出出的AI对抗威胁检测器，检测器主要分为下面四步：

1. 检测器首先通过执行大量已知的攻击攻击待检测的分类模型，观察模型是否成功被攻击

2. 对攻击攻击的情况生成脆弱性报告以及重播该漏洞的ipynb文件（供研究人员了解该漏洞）

3. 自动修复（当前还是人工修复）

4. 对修复漏洞后的模型重新进行检测

&emsp;&emsp;目前，该工具还只支持keras的Evasion攻击。主讲人说后续会持续加入数据投毒攻击、模型投毒、模型窃取等攻击方式的检测。

![image](https://raw.githubusercontent.com/AnchoretY/images/master/blog/image.8kp1i4nl69.png)