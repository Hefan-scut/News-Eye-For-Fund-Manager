# 基金经理新闻眼
## ——为基金管理者提供实时、科学、详细的新闻预警

### 痛点
1.在信息时代，各大媒体每日股市新闻成千上万条，基金经理难以从成千上万条新闻中识别到对自己有用的新闻。

2.基金经理同时持仓多个股票或多个基金，难以快速确定新闻中是否包含自己所持仓的股票或新闻。

3.新闻可能单纯只对某一支股票有影响，但一支股票会对某个行业或者其他股票产生影响，基金经理难以快速甄别。

### 解决方案
1.设计实时爬虫爬取各大媒体新闻，并存储到数据库中。

2.填写基金经理所持仓股票，并存储到数据库中。

3.构建新闻情感分类模型甄别正负类新闻，将大于一定置信度的正负类新闻进行提取。

4.构建实体识别模型，识别正负类新闻的股票信息、公司信息或基金信息。

5.构建股市行业知识图谱，将识别出的股票、公司、基金信息去做进一步的关联。

6.设计Demo，前后端、数据库与模型交互，方便基金经理进行操作。


### 参考资料
[1]陶恺,陶煌.一种基于深度学习的文本分类模型[J].太原师范学院学报(自然科学版),2020,19(04):45-51.

[2]Moirangthem Dennis Singh,Lee Minho. Hierarchical and lateral multiple timescales gated recurrent units with pre-trained encoder for long text classification[J]. Expert Systems With Applications,2021,165.

[3]何铠. 基于自然语言处理的文本分类研究与应用[D].南京邮电大学,2020.

[4]张军莲,张一帆,汪鸣泉,黄永健.基于图卷积神经网络的中文实体关系联合抽取[J/OL].计算机工程:1-10[2021-01-04].https://doi.org/10.19678/j.issn.1000-3428.0059574.
[5]Santiso Sara,Pérez Alicia,Casillas Arantza. Adverse Drug Reaction extraction: Tolerance to entity recognition errors and sub-domain variants[J]. Computer Methods and Programs in Biomedicine,2021,199.

[6]武国亮,徐继宁.基于命名实体识别任务反馈增强的中文突发事件抽取方法[J/OL].计算机应用:1-8[2021-01-04].http://kns.cnki.net/kcms/detail/51.1307.TP.20201209.1334.006.html.

[7]李建,靖富营,刘军.基于改进BERT算法的专利实体抽取研究——以石墨烯为例[J].电子科技大学学报,2020,49(06):883-890.

[8]Gong Fan,Wang Meng,Wang Haofen,Wang Sen,Liu Mengyue. SMR: Medical Knowledge Graph Embedding for Safe Medicine Recommendation[J]. Big Data Research,2021,23.

[9]刘胜京,高庆和,邓楹君,杜冠潮,郭俊,赵丰,王浩,郭军.基于知识图谱中医药诊治慢性前列腺炎研究现状分析[J/OL].中国中西医结合杂志:1-6[2021-01-04].http://kns.cnki.net/kcms/detail/11.2787.R.20201229.1500.002.html.

[10]路威,赵丽君.兵要知识图谱的构建与应用研究[J/OL].测绘地理信息:1-6[2021-01-04].https://doi.org/10.14188/j.2095-6045.2020094.

https://github.com/Determined22/zh-NER-TF


### 数据来源
通联数据