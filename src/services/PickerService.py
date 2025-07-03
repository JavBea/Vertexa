#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：Vertexa
@File    ：PickerService.py
@IDE     ：PyCharm
@Author  ：Sean Han
@Date    ：2025/7/2 21:00
"""
from typing import Union, List, Tuple

from flask import jsonify
from sqlalchemy  import select
from werkzeug.utils import secure_filename
import os
import pandas as pd  # 用于处理Excel文件

from src.app.extensions import db
from src.models.Picker.PickerItem import PickerItem
from src.models.Picker.PickerList import PickerList
from src.dao.picker import PickerListDao
from src.dao.picker import PickerItemDao

# 获取所有的名单
def get_all_lists():
    try:
        # 执行查询
        stmt = select(PickerList)
        lists = db.session.scalars(stmt).all()

        # 将结果转换为字典列表
        lists_data = [
            {
                "id": list0.id,
                "name": list0.name,
                "availability": list0.availability,
                "created_time": list0.created_time,
            }
            for list0 in lists
        ]

        # 构建响应
        response = {
            "success": True,
            "message": "Items retrieved successfully",
            "data": lists_data,
            "count": len(lists_data)
        }

        return jsonify(response)

    except Exception as e:
        # 错误处理
        error_response = {
            "success": False,
            "message": f"Failed to retrieve lists: {str(e)}",
            "data": [],
            "count": 0
        }
        return jsonify(error_response), 500


# 获取指定名单中所有的项
def get_all_items(list_id):
    try:
        # 执行查询
        stmt = select(PickerItem).where(PickerItem.list_id == list_id)
        items = db.session.scalars(stmt).all()

        # 将结果转换为字典列表
        items_data = [
            {
                "id": item.id,
                "name": item.name,
                "list_id": item.list_id,
                "probability": item.probability
            }
            for item in items
        ]

        # 构建响应
        response = {
            "success": True,
            "message": "Items retrieved successfully",
            "data": items_data,
            "count": len(items_data)
        }

        return jsonify(response)

    except Exception as e:
        # 错误处理
        error_response = {
            "success": False,
            "message": f"Failed to retrieve items: {str(e)}",
            "data": [],
            "count": 0
        }
        return jsonify(error_response), 500

# 接受上传文件
def upload_file(request):
    if 'excel_file' not in request.files:
        return jsonify({'error': '没有文件部分'}), 400

    file = request.files['excel_file']

    if file.filename == '':
        return jsonify({'error': '未选择文件'}), 400

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        os.makedirs('tmp', exist_ok=True)
        filepath = os.path.join('tmp', filename)
        file.save(filepath)

        # 使用pandas读取Excel
        try:
            df = pd.read_excel(filepath)
            # 处理数据...

            list_id = PickerListDao.insert()
            if list_id == -1:
                return jsonify({'error': '新建名单失败'}), 400

            process_excel_file(df, list_id)

            return jsonify({
                'message': '文件上传成功',
                'filename': filename,
                'data_preview': df.head().to_dict('records')
            })
        except Exception as e:
            return jsonify({'error': f'处理Excel文件出错: {str(e)}'}), 500

    return jsonify({'error': '文件类型不允许'}), 400


# 判断文件后缀
def allowed_file(filename):
    allowed_extensions = {'xlsx', 'xls'}
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in allowed_extensions


# 处理excel文件内容
def process_excel_file(df,list_id) -> Union[int, Tuple[List[str], List[float]]]:
    """
    处理包含"名称"和"权重"列的Excel文件

    参数:
        file_path: Excel文件路径

    返回:
        成功时返回 (名称列表, 权重列表) 的元组
        失败时返回 -1
    """
    try:

        # 提取第一列名称列（字符串）
        name_list = df.iloc[:, 0].tolist()

        # 提取权重列（float），处理可能的格式错误
        try:
            weight_list = df.iloc[:, 1].astype(float).tolist()
        except ValueError as e:
            print(f"权重列包含非数字值: {e}")
            return -1

        # 检查两列长度是否一致
        if len(name_list) != len(weight_list):
            print("错误: 名称和权重列的行数不一致")
            return -1

        for n, w in zip(name_list, weight_list):
            # print(n,w)
            res = PickerItemDao.insert(name=n, probability=w,list_id=list_id)
            if res == -1:
                return -1

        return 1

    except Exception as e:
        print(f"处理文件时发生错误: {e}")
        return -1



# 插入新名单
def insert_list():
    return PickerListDao.insert()

# 删除名单(置不可用)
def delete_list(list_id):
    return PickerListDao.obsolete(list_id)

# 重命名名单
def rename_list(list_id,new_name):
    return PickerListDao.rename(list_id,new_name)

# 使用示例
if __name__ == "__main__":
    result = process_excel_file(pd.read_excel(r"C:\Users\Me\Desktop\ds.xlsx"),10001)
    print(result)