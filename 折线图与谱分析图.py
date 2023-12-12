# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
from proplot import rc
import matplotlib.pyplot as plt 
import matplotlib.ticker as mtick
from matplotlib.ticker import ScalarFormatter

plt.rcParams['axes.unicode_minus'] = False 
rc["font.family"] = "TeX Gyre Schola" # 字体
rc['tick.labelsize'] = 10
rc["axes.labelsize"] = 12
rc["tick.labelweight"] = "bold"

def per_response_plot(x,y,xlabel,ylabel,dpi,linewidth=2,legend=False):
    # 绘制折线图
    fig, ax = plt.subplots(dpi=dpi,facecolor='white',)
    # 主网格线
    ax.grid(True, axis='x',linestyle = '--', zorder=0,alpha=0.6,color='black',)
    ax.grid(True, axis='y',linestyle = '--', zorder=0,alpha=0.6,color='black')
    # 副网格线
    ax.grid(True, linestyle='--', which='minor', zorder=0,alpha=0.2)
    ax.grid(True, linestyle='--', which='minor', zorder=0,alpha=0.2)
    # 刻度线粗细
    ax.tick_params(axis="both", which="major", direction="in", width=2, length=4)
    ax.tick_params(axis="both", which="minor", direction="in", width=1, length=2)
    # 副刻度线
    ax.minorticks_on()
    # 显示两位小数
    # 将useMathText设置为True,使得刻度标记显示为科学计数法
    y_formatter = ScalarFormatter(useMathText=True)
    y_formatter.set_powerlimits((-2, 2))  
    ax.yaxis.set_major_formatter(y_formatter)
    ax.xaxis.set_major_formatter(mtick.FormatStrFormatter('%.1f'))
    # 数据绘图
    ax.plot(x,y,linewidth=linewidth,color='#0d33ff', label='sin') 
    # 添加标题和标签
    plt.xlabel(xlabel, fontweight='bold')
    plt.ylabel(ylabel, fontweight='bold')
    # 添加图例
    if legend:
        ax.legend(loc='best',edgecolor='black',fancybox=0,shadow=0,facecolor=None,fontsize=10)
    # 显示图形
    plt.tight_layout()
    plt.show()

def all_response_plot(x,y,xlabel,ylabel,dpi,labels=['case1','case2','case3'],linewidth=2,legend=True):
    # 绘制折线图
    fig, ax = plt.subplots(dpi=dpi,facecolor='white',)
    # 主网格线
    ax.grid(True, axis='x',linestyle = '--', zorder=0,alpha=0.6,color='black',)
    ax.grid(True, axis='y',linestyle = '--', zorder=0,alpha=0.6,color='black')
    # 副网格线
    ax.grid(True, linestyle='--', which='minor', zorder=0,alpha=0.2)
    ax.grid(True, linestyle='--', which='minor', zorder=0,alpha=0.2)
    # 刻度线粗细
    ax.tick_params(axis="both", which="major", direction="in", width=2, length=4)
    ax.tick_params(axis="both", which="minor", direction="in", width=1, length=2)
    # 副刻度线
    ax.minorticks_on()
    # 显示两位小数
    # 将useMathText设置为True,使得刻度标记显示为科学计数法
    y_formatter = ScalarFormatter(useMathText=True)
    y_formatter.set_powerlimits((-2, 2))  
    ax.yaxis.set_major_formatter(y_formatter)
    ax.xaxis.set_major_formatter(mtick.FormatStrFormatter('%.1f'))
    # 数据绘图
    # ax.scatter(x,y.iloc[2,:],s=10,edgecolor='#ff0000',color =None )
    ax.plot(x,y.iloc[2,:],linewidth=linewidth,color='#ff0000', label=labels[2] ,) 
    ax.plot(x,y.iloc[1,:],linewidth=linewidth,color='#0d33ff', label=labels[1] ,) 
    ax.plot(x,y.iloc[0,:],linewidth=linewidth,color='black'  , label=labels[0] ,) 
    
   

    # 添加标题和标签
    plt.xlabel(xlabel, fontweight='bold')
    plt.ylabel(ylabel, fontweight='bold')
    # 添加图例
    if legend:
        ax.legend(loc=4,edgecolor='black',fancybox=0,shadow=0,facecolor=None,fontsize=10)
        plt.savefig(r'E:\Project\TriplyCoupledBeam\graph\three.png')
    # 显示图形
    plt.tight_layout()
    plt.show()
    

def spectral_plot(x,y,xlabel,ylabel,dpi,linewidth=2,legend=False):
    # 绘制折线图
    fig, ax = plt.subplots(dpi=dpi,facecolor='white',)
    # 主网格线
    ax.grid(True, axis='x',linestyle = '--', zorder=0,alpha=0.6,color='black',)
    ax.grid(True, axis='y',linestyle = '--', zorder=0,alpha=0.6,color='black')
    # 副网格线
    ax.grid(True, linestyle='--', which='minor', zorder=0,alpha=0.2)
    ax.grid(True, linestyle='--', which='minor', zorder=0,alpha=0.2)
    # 刻度线粗细
    ax.tick_params(axis="y", which="major", direction="in", width=2, length=4)
    ax.tick_params(axis="y", which="minor", direction="in", width=1, length=2)
    # 副刻度线
    ax.minorticks_on()
    # 显示两位小数
    # 将useMathText设置为True,使得刻度标记显示为科学计数法
    y_formatter = ScalarFormatter(useMathText=True)
    y_formatter.set_powerlimits((-2, 2))  
    ax.yaxis.set_major_formatter(y_formatter)
    ax.xaxis.set_major_formatter(mtick.FormatStrFormatter('%.1f'))
    # 数据绘图
    ax.plot(x,y,linewidth=linewidth,color='#0d33ff') 
    ax.fill_between(x,0,y,color='blue',alpha=0.2)
    # 添加标题和标签
    plt.xlabel(xlabel, fontweight='bold')
    plt.ylabel(ylabel, fontweight='bold')
    # 显示范围
    ax.set_ylim(0) # 限制x范围
    # 显示图形
    plt.tight_layout()
    plt.show()
    
    
    # pandas读取数据，注意x行排列y行排列

    Parameters
    ----------
    x : TYPE excel数据（double）
        DESCRIPTION. 时间
    y : TYPE excel数据（double）
        DESCRIPTION.响应位移
    xlabel : TYPE  srting
        DESCRIPTION. 横坐标名称
    ylabel : TYPE srting
        DESCRIPTION. 纵坐标名称
    dpi : TYPE  图片分辨率，以满足要求
        DESCRIPTION. int （整型数字）
    linewidth : TYPE, optional 线宽
        DESCRIPTION. The default is 2.
    legend : TYPE, optional  是否显示说明图框
        DESCRIPTION. The default is False.
    Returns
    -------
    图片。

    """