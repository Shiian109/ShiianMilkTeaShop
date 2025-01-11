# Chapter 0 - 角色设定

```Markdown
I want you to act as a senior data scientist with the following Background:
- 15+ years experience in data science and analytics
- Expertise in:
  * Statistical analysis and machine learning
  * Data visualization and storytelling
  * Business intelligence and analytics
  * Digital transformation consulting
- Cross-industry experience:
  * E-commerce and retail
  * Finance and banking
  * Healthcare
  * Technology and startups
  * Education
- Track record of translating complex data insights into actionable business strategies
- Known for making data analytics accessible to non-technical stakeholders

Your approach to analysis:
1. Begin with clear problem definition
2. Ensure data quality and reliability
3. Apply appropriate statistical methods
4. Focus on actionable insights
5. Communicate findings in simple terms

For all analyses, you will:
1. Assess data quality and limitations
2. Explain your analytical approach
3. Provide statistical insights
4. Translate findings into business recommendations
5. Suggest next steps and potential areas for deeper analysis
6. Use clear, non-technical language while maintaining analytical rigor
7. Format charts in the McKinsey style, ensuring all titles, legends, and axis labels (X and Y) are presented in English.

Communication style:
- Clear and concise
- Business-oriented
- Educational when explaining concepts
- Balancing technical accuracy with accessibility
- Always use Chinese

Let's begin analyzing our dataset. Please confirm your understanding of this role.
```

# Chapter 1 - 数据清洗与预处理
## 数据清洗
```Markdown
这是一个奶茶店的销售数据集。
帮我检查数据集中是否存在重复值，缺失值或异常值。 
关于异常值，可以从多个维度，比如社会常识，统计学，业务逻辑等判断并找出。
最后输出含有重复值，缺失值或异常值的行数据，并且标注出每行中是哪一个数据有问题。
```

```Markdown 
根据order_id帮我删除这些有问题的数据，更新数据集并生成下载链接。
```

## 描述性统计
```Markdown
对数据进行描述性统计。
```

# Chapter 2 - 数据可视化

```Markdown
选择最合适的可视化图表，呈现平均气温和销售额的关系。
```

```Markdown
选择最合适的可视化图表，呈现工作日vs周末的平均销售额。
并简要分析。
```

```Markdown
选择最合适的可视化图表, 呈现随着时间的销售额变化。
并简要分析。
```

```Markdown
选择最合适的可视化图表, 呈现各奶茶品类销售额占比。
并简要分析。
```

```Markdown
选择最合适的可视化图表, 呈现随着时间，4种饮品的销售额占比的热度。
```

```Markdown
用热力图可视化数据集中的缺失值。
```

```Markdown
用双坐标轴图来表示随着时间推移，销售额和促销折扣的关系。
```

```Markdown
用双坐标轴图来表示随着时间推移，销售额和促销折扣的关系。
将销售额和促销折扣进行周平均的处理后再可视化。
```

# Chapter 3 - 假设检验
## t检验
```Markdown
运用假设检验方法，设定H0, H1之后，再分析周末和工作日的日均销售额差异。
```

## 方差分析ANOVA
```Markdown
运用假设检验方法，设定H0, H1之后，再分析不同促销折扣力度（0%, 10%, 15%, 20%）对日均销售额的影响是否存在显著差异。
```

## 变量间关联性 - 相关性分析
```Markdown
运用假设检验方法，设定H0, H1之后，再分析促销折扣与日销售额是否存在显著的相关关系。
```

## 变量间关联性 - 卡方检验
```Markdown
运用假设检验方法，设定H0, H1之后，列出列联表，再分析在不同天气条件下（晴天、雨天），顾客的饮品选择是否有显著差异。
```

# Chapter 4 - 预测分析
## 回归预测（连续变量预测）
```Markdown
根据我上传的数据集进行预测分析。
目标变量为daily_sales。 
选取适当的特征量，然后用随机森林模型对1/1-3/31的数据进行训练。
再对4/1-4/10的数据进行预测。 
最后将实际数据和预测数据可视化。
```

```Markdown
提取模型里的特征重要性并对所有特征量进行可视化。
```

## 分类预测（离散变量预测）
```Markdown
将连续的销售额转换为二分类问题，选择销售额的中位数作为分类阈值，
高于中位数标记为1（高销售），低于中位数标记为0（低销售）。 
选取适当的特征量，然后用随机森林对1/1-3/31的数据进行训练。 
再对4/1-4/10的数据进行预测。 
最后用可视化后的混淆矩阵评价模型，
根据混淆矩阵用公式计算出准确率并解释。
```

## 时间序列分析（时间维度预测）
```Markdown
目标变量为daily_sales。
选取适当的特征量，然后用时间序列模型对1/1-3/31的数据进行训练。
再对4/1-4/10的数据进行预测。 
最后将实际数据和预测数据可视化。
```

```Markdown
对目标变量进行季节性分解。
```

# Chapter 5 - 降维与聚类
## 降维 - 主成分分析（PCA）
```Markdown
根据我上传的数据集，选取适当的特征量后，进行主成分分析（PCA），并绘制方差累加图。
并标注数值。
```

```Markdown
解释PC1，PC2
```

```Markdown
用散点图可视化PC1，PC2
```

```Markdown
在主成分得分中，选取PC1-PC9生成新的数据集。
```

## 聚类方法
```Markdown
使用K-means对PCA降维后的数据进行聚类，通过肘部法则（Elbow Method）确定最佳聚类数量。
```

```Markdown
设置聚类数量为4，进行K-means分析，并在PC1和PC2空间中按组别可视化，用不同颜色呈现顾客聚类的特征分布。
```

# Chapter 6 - 文本数据分析

词频统计与可视化
```Markdown
对客户反馈的文本数据进行词频统计，并用WordCloud可视化。
```

情感分析
```Markdown
对客户反馈的文本数据进行情感分析，并可视化。
```

文本分类
```Markdown
对客户反馈的文本数据进行主题分类和统计，并可视化。
给我具体的主题内容和与之对应的客户评论。
```
