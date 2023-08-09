#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2023/8/9 14:13
# @File  : data_preprocess.py
# @Author: 
# @Desc  : 数据预处理
import json

def convert_alpaca_data():
    """
    将alpacha数据转换为本项目所需数据
    """
    json_file = "/Users/admin/git/LLaMA-Efficient-Tuning/data/alpaca_gpt4_data_zh.json"
    # 保存到本地的文件
    train_alpaca_file = "data/train_alpaca.json"
    dev_alpaca_file = "data/dev_alpaca.json"
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    #合并instruction和input为input, output改成target
    new_data = []
    for one in data:
        new_one = {}
        new_one['input'] = one['instruction'] + one['input']
        new_one['target'] = one['output']
        new_data.append(new_one)
    #划分训练集和验证集
    train_data = new_data[:int(len(new_data)*0.8)]
    dev_data = new_data[int(len(new_data)*0.8):]
    #保存到本地
    with open(train_alpaca_file, 'w', encoding='utf-8') as f:
        json.dump(train_data, f, ensure_ascii=False)
    with open(dev_alpaca_file, 'w', encoding='utf-8') as f:
        json.dump(dev_data, f, ensure_ascii=False)

if __name__ == '__main__':
    convert_alpaca_data()