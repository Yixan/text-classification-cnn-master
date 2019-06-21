# -*- coding: utf-8 -*-
# @Time    : 2019/6/20 21:07
# @Author  : zhangyx
# @FileName: plot.py
# @Software: PyCharm
import matplotlib.pyplot as plt
import pandas as pd
#coding:utf-8
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
#有中文出现的情况，需要u'内容'
df1=pd.read_csv('plot\\data1_256_5.csv',sep=',')
# print(df.columns)
acc_val1=df1['acc_val'][18:-1]
acc_test1=df1['acc_test'][18:-1]
# testlist1=df1['test_f']

df2=pd.read_csv('plot\\data1_256_10.csv',sep=',')
# print(df.columns)
acc_val2=df2['acc_val'][18:-1]
acc_test2=df2['acc_test'][18:-1]

df3=pd.read_csv('plot\\data1_512_5.csv',sep=',')
# print(df.columns)
acc_val3=df3['acc_val'][18:-1]
acc_test3=df3['acc_test'][18:-1]

df4=pd.read_csv('plot\\data1_512_10.csv',sep=',')
acc_val4=df4['acc_val'][18:-1]
acc_test4=df4['acc_test'][18:-1]




x1=[i+18 for i in range(0,len(acc_val1))]
x2=[i+18 for i in range(0,len(acc_val2))]
x3=[i+18 for i in range(0,len(acc_val3))]
x4=[i+18 for i in range(0,len(acc_val4))]


# plt.figure(1)
# plt.plot(x1, acc_val1, color=(float(255/255),float(140/255),0), linestyle="-", linewidth=2, label=u"实验1验证集准确率")
# plt.plot(x2, acc_val2, color=(float(210/255),float(105/255),float(30/255)), linestyle="-", linewidth=2, label=u"实验2验证集准确率")
# plt.plot(x3, acc_val3, color=(float(255/255),float(215/255),0), linestyle="-", linewidth=2, label=u"实验3验证集准确率")
# plt.plot(x4, acc_val4, color=(float(189/255),float(183/255),float(107/255)), linestyle="-", linewidth=2, label=u"实验4验证集准确率")
# plt.grid(color="k", linestyle=":")
# plt.legend(loc='center right')
# plt.title(u"实验1-4验证集准确率对比图")
# plt.xlabel(u"训练轮数")
# plt.savefig("plot\\实验1-4验证集准确率对比图.png")
# plt.show()
# plt.figure(2)
# plt.plot(x1, acc_test1, color=(0,0,float(205/255)), linestyle="-", linewidth=2, label=u"实验1测试集准确率")
# plt.plot(x2, acc_test2, color=(float(65/255),float(155/255),float(225/255)), linestyle="-", linewidth=2, label=u"实验2测试集准确率")
# plt.plot(x3, acc_test3, color=(float(143/255),float(188/255),float(143/255)), linestyle="-", linewidth=2, label=u"实验3测试集准确率")
# plt.plot(x4, acc_test4, color=(float(95/255),float(158/255),float(160/255)), linestyle="-", linewidth=2, label=u"实验4测试集准确率")
# plt.grid(color="k", linestyle=":")
# plt.legend(loc='center right')
# plt.title(u"实验1-4测试集准确率对比图")
# plt.xlabel(u"训练轮数")
# plt.savefig("plot\\实验1-4测试集准确率对比图.png")
# plt.show()

# plt.figure(3)
# plt.plot(x1, testlist1, color=(0,float(128/255),0), linestyle="-", linewidth=2, label=u"组合1测试集F值")
# plt.plot(x2, testlist2, color=(0,float(139/255),float(139/255)), linestyle="-", linewidth=2, label=u"组合2测试集F值")
# plt.plot(x3, testlist3, color=(float(60/255),float(179/255),float(113/255)), linestyle="-", linewidth=2, label=u"组合3测试集F值")
# plt.plot(x4, testlist4, color=(float(50/255),float(205/255),float(50/255)), linestyle="-", linewidth=2, label=u"组合4测试集F值")
# plt.grid(color="k", linestyle=":")
# plt.legend(loc='center right')
# plt.title(u"LSTM-CWS模型分词测试集F1值对比图.png")
# plt.xlabel(u"训练轮数")
# plt.savefig("LSTM-CRF模型分词测试F1值对比图png")
# plt.show()
df5=pd.read_csv('plot\\data2_256_5.csv',sep=',')
p1=df5['P'][18:-1]
r1=df5['R'][18:-1]
f1=df5['F1'][18:-1]

df6=pd.read_csv('plot\\data2_256_10.csv',sep=',')
p2=df6['P'][18:-1]
r2=df6['R'][18:-1]
f2=df6['F1'][18:-1]

df7=pd.read_csv('plot\\data2_512_5.csv',sep=',')
p3=df7['P'][18:-1]
r3=df7['R'][18:-1]
f3=df7['F1'][18:-1]

df8=pd.read_csv('plot\\data2_512_10.csv',sep=',')
p4=df8['P'][18:-1]
r4=df8['R'][18:-1]
f4=df8['F1'][18:-1]

df9=pd.read_csv('data_ft_1.csv',sep=',')
p9=df9['P'][1:-1]
r9=df9['R'][1:-1]
f9=df9['F1'][1:-1]

df10=pd.read_csv('data_ft_2.csv',sep=',')
p10=df10['P'][1:-1]
r10=df10['R'][1:-1]
f10=df10['F1'][1:-1]

x5=[i+18 for i in range(0,len(p1))]
x6=[i+18 for i in range(0,len(p2))]
x7=[i+18 for i in range(0,len(p3))]
x8=[i+18 for i in range(0,len(p4))]
x9=[(i*4+18) for i in range(0,len(p9))]
x10=[(i*4+18) for i in range(0,len(p10))]

plt.figure(1)
plt.plot(x5, p1, color=(float(255/255),float(140/255),0), linestyle="-", linewidth=2, label=u"实验1测试集准确率")
plt.plot(x6, p2, color=(float(210/255),float(105/255),float(30/255)), linestyle="-", linewidth=2, label=u"实验2测试集准确率")
plt.plot(x7, p3, color=(float(255/255),float(215/255),0), linestyle="-", linewidth=2, label=u"实验3测试集准确率")
plt.plot(x8, p4, color=(float(189/255),float(183/255),float(107/255)), linestyle="-", linewidth=2, label=u"实验4测试集准确率")
plt.plot(x9, p9, linestyle="-", linewidth=2, label=u"基线1-1gram")
plt.plot(x10, p10, color=(float(25/255),float(25/255),float(112/255)), linestyle="-", linewidth=2, label=u"基线2-2gram")
plt.grid(color="k", linestyle=":")
plt.legend(loc='upper right')
plt.title(u"实验1-4测试集准确率对比图")
plt.xlabel(u"训练轮数")
plt.savefig("plot\\实验1-4测试集准确率对比图.png")
plt.show()

plt.figure(2)
plt.plot(x5, r1, color=(float(255/255),float(140/255),0), linestyle="-", linewidth=2, label=u"实验1测试集召回率")
plt.plot(x6, r2, color=(float(210/255),float(105/255),float(30/255)), linestyle="-", linewidth=2, label=u"实验2测试集召回率")
plt.plot(x7, r3, color=(float(255/255),float(215/255),0), linestyle="-", linewidth=2, label=u"实验3测试集召回率")
plt.plot(x8, r4, color=(float(189/255),float(183/255),float(107/255)), linestyle="-", linewidth=2, label=u"实验4测试集召回率")
plt.plot(x9, r9, linestyle="-", linewidth=2, label=u"基线1-1gram")
plt.plot(x10, r10, color=(float(25/255),float(25/255),float(112/255)),linestyle="-", linewidth=2, label=u"基线2-2gram")
plt.legend(loc='upper right')
plt.grid(color="k", linestyle=":")
plt.title(u"实验1-4测试集召回率对比图")
plt.xlabel(u"训练轮数")
plt.savefig("plot\\实验1-4测试集召回率对比图.png")
plt.show()

plt.figure(3)
plt.plot(x5, f1, color=(float(255/255),float(140/255),0), linestyle="-", linewidth=2, label=u"实验1测试集F1值")
plt.plot(x6, f2, color=(float(210/255),float(105/255),float(30/255)), linestyle="-", linewidth=2, label=u"实验2测试集F1值")
plt.plot(x7, f3, color=(float(255/255),float(215/255),0), linestyle="-", linewidth=2, label=u"实验3测试集F1值")
plt.plot(x8, f4, color=(float(189/255),float(183/255),float(107/255)), linestyle="-", linewidth=2, label=u"实验4测试集F1值")
plt.plot(x9, f9, linestyle="-", linewidth=2, label=u"基线1-1gram")
plt.plot(x10, f10, color=(float(25/255),float(25/255),float(112/255)),linestyle="-", linewidth=2, label=u"基线2-2gram")
plt.grid(color="k", linestyle=":")
plt.legend(loc='upper right')
plt.title(u"实验1-4测试集F1值对比图")
plt.xlabel(u"训练轮数")
plt.savefig("plot\\实验1-4测试集F1值对比图.png")
plt.show()