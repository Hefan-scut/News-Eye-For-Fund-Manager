# 利用BiLSTM-CRF做中文的命名实体识别NER

### 介绍
BiLSTM：Bilateral long-term and short-term memory network 双向长短期记忆网络

CRF：Condition random field 条件随机场

NER：Named Entity Recognition 命名实体识别

Bi-LSTM-CRF算法是目前比较流行的NER算法

BiLSTM和CRF可以看做NER模型中的两个不同层

### 算法原理

#### 1.1数据解析

我们有一个句子集，包含三种实体：Person、Location、Organization，每种实体分为开始(Begin)和中间(intermediate)字，如下所示

B-Person（Person的第一个字）

I-Person（Person的中间字）

B-Location（Location的第一个字）

I-Location（Location的中间字）

B-Organization（Organization的第一个字）

I-Organization（Organization的中间字）


另外，其他单词我们用O表示。

举个例子：


![输入图片说明](https://images.gitee.com/uploads/images/2021/0107/160216_11454014_7878388.png "屏幕截图.png")


#### 1.2BiLSTM-CRF model

句子中的每个字会被表示成一个向量(Embedding)，所有的Embedding都会在训练过程中微调。

BiLSTM-CRF模型的输入是这些Embedding，输出是句子中所有字的预测标签。

![输入图片说明](https://images.gitee.com/uploads/images/2021/0107/120053_8175d36f_7878388.png "屏幕截图.png")


#### 1.3BiLSTM layer

BiLSTM的输出是该字对应每一个类别的scores。

![输入图片说明](https://images.gitee.com/uploads/images/2021/0107/120619_d38e8092_7878388.png "屏幕截图.png")

对于w0，BiLSTM节点的输出是1.5(B-Person), 0.9(I-Person), 0.1(B-Organization), 0.08(I-Organization) 以及0.05 (O)。

所有的BiLSTM blocks预测的score都会被喂到CRF layer。

CRF layer中,在所有的label sequence选择预测得分最高的序列作为最佳答案。


#### 1.4CRF layer

你可能会发现，如果没有CRF Layer，也可以只用BiLSTM来训练NER模型。

![输入图片说明](https://images.gitee.com/uploads/images/2021/0107/141845_b3ef8d10_7878388.png "屏幕截图.png")

由于每个word的BiLSTM的输出是labe得分情况. 可以选择每个单词中得分最高的label作为结果。

例如，对于单词w0, “B-Person”得分最高(1.5), 因此可以选择“B-Person” 作为预测label。

尽管这里可以得到正确的预测结果，但是在有些如下面的情况中。

![输入图片说明](https://images.gitee.com/uploads/images/2021/0107/142016_12377443_7878388.png "屏幕截图.png")

很显然，预测的labels是不对的。“I-Organization I-Person”以及 “B-Organization I-Person”.因为两个不同类别的中间词不可能挨着。

而这是CRF layer就起到作用了，它可以对最终的预测labels添加一些限制来确保结果是有效的。

这些限制可以由CRF layer在训练过程中自动的训练数据集中学到，这些限制可以是：


- 句子的第一个单词应该是“B-”或 “O”，不可能是 “I-”。

- “B-Person I-Person”是可以的， “B-Person I-Organization” 是无效的。

- 命名实体的开始应该是 “B-” 而不是 “I-”。

#### 1.5CRF loss function

CRF loss function由真实路径得分和和所有可能路径的总分组成。

真实路径应该具有在可能路径中有最高的分数。

![输入图片说明](https://images.gitee.com/uploads/images/2021/0107/155851_d7c2ab28_7878388.png "屏幕截图.png")


如何定义一条路径的Score?

如何计算所有路径的总Score?

见参考资料。


### 参考资料

1.[Bi-LSTM-CRF算法详解](https://blog.csdn.net/qq_17677907/article/details/88096243)

2.[A simple BiLSTM-CRF model for Chinese Named Entity Recognition](https://github.com/Determined22/zh-NER-TF) 
