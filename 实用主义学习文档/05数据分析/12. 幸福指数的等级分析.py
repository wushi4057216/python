# pandas 数据源下载地址：https://video.mugglecode.com/data_pd.zip，下载压缩包后解压即可（数据源与上节课相同）
# -*- coding: utf-8 -*-

"""
    明确任务：
        为幸福指数添加对应的等级
"""
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# 年度全球幸福报告数据文件
report_datafile_path = './data_pd/happiness_report.csv'

# 结果保存路径
output_path = './output'
if not os.path.exists(output_path):
    os.makedirs(output_path)


def collect_data():
    """
        数据获取
    """
    data_df = pd.read_csv(report_datafile_path)
    return data_df


def process_data(data_df):
    """
        数据处理
    """
    data_df.dropna(inplace=True)
    data_df.sort_values(['Year', 'Happiness Score'], ascending=[True, False], inplace=True)
    return data_df


def analyze_data(data_df):
    """
        数据分析
    """
    # # apply()
    # def score2level(score_val):
    #     """
    #         score to level
    #     """
    #     if score_val <= 3:
    #         level = 'Low'
    #     elif score_val <= 5:
    #         level = 'Middle'
    #     else:
    #         level = 'High'
    #     return level
    #
    # data_df['Level'] = data_df['Happiness Score'].apply(score2level)

    # cut()
    data_df['Level'] = pd.cut(data_df['Happiness Score'], bins=[-np.inf, 3, 5, np.inf],
                              labels=['Low', 'Middle', 'High'])

    region_year_level_df = pd.pivot_table(data_df, index='Region', columns=['Year', 'Level'], values=['Country'],
                                          aggfunc='count')

    region_year_level_df.fillna(0, inplace=True)

    return region_year_level_df


def save_plot_results(region_year_level_df):
    """
        结果展示
    """
    region_year_level_df.to_csv(os.path.join(output_path, 'region_year_level_df.csv'))

    for year in [2015, 2016, 2017]:
        region_year_level_df['Country', year].plot(kind='bar', stacked=True, title=year)
        plt.tight_layout()
        plt.savefig(os.path.join(output_path, '{}_level_stats.png'.format(year)))
        plt.show()


def main():
    """
        主函数
    """
    # 数据获取
    data_df = collect_data()

    # 数据处理
    proc_data_df = process_data(data_df)

    # 数据分析
    region_year_level_df = analyze_data(proc_data_df)

    # 结果展示
    save_plot_results(region_year_level_df)


if __name__ == '__main__':
    main()
