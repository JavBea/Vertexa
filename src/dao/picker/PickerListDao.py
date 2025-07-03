#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：Vertexa 
@File    ：PickerListDao.py
@IDE     ：PyCharm 
@Author  ：Sean Han
@Date    ：2025/7/3 15:56 
"""
import datetime

from src.app.extensions import db
from src.models.Picker.PickerList import PickerList
from flask import jsonify

# 新建
def insert():
    """
    插入新的 PickerList 记录

    参数:

    返回:
        成功时返回新记录的ID，失败时返回-1
    """
    # 配置数据库连接（根据你的实际情况调整）

    try:
        # 创建新记录（不需要指定id，因为它是自增的）
        new_list = PickerList(
            name="新建名单",
            availability='available',
            created_time=datetime.datetime.now()
        )

        # 添加到会话并提交
        db.session.add(new_list)
        db.session.commit()

        # 刷新对象以获取生成的ID
        db.session.refresh(new_list)

        # 返回新记录的ID
        return jsonify({'success': 'true','id':new_list.id}), 200

    except Exception as e:
        # 发生错误时回滚并打印错误信息
        db.session.rollback()
        print(f"插入 PickerList 失败: {str(e)}")

        return jsonify({'success': 'false','error': '插入名单失败'}), 400

# 重命名
def rename(list_id: int,name: str):
    """
    重命名 PickerList 记录

    参数:

    返回:
        成功时返回1，失败时返回-1
    """
    # 配置数据库连接（根据你的实际情况调整）

    try:

        # 查询要更新的记录
        picker_list = db.session.query(PickerList).filter(PickerList.id == list_id).first()

        if not picker_list:
            print(f"错误: 未找到 ID 为 {list_id} 的 PickerList")
            return None

        # 更新字段
        picker_list.name = name
        db.session.commit()
        return jsonify({'success': 'true'}), 200

    except Exception as e:
        # 发生错误时回滚并打印错误信息
        db.session.rollback()
        print(f"删除 PickerList 失败: {str(e)}")

        return jsonify({'success': 'false','error': f'删除名单失败: {str(e)}'}), 400

# 废弃
def obsolete(list_id: int):
    """
    删除 PickerList 记录

    参数:

    返回:
        成功时返回1，失败时返回-1
    """
    # 配置数据库连接（根据你的实际情况调整）

    try:

        # 查询要更新的记录
        picker_list = db.session.query(PickerList).filter(PickerList.id == list_id).first()

        if not picker_list:
            print(f"错误: 未找到 ID 为 {list_id} 的 PickerList")
            return None

        # 更新字段
        picker_list.availability = 'unavailable'
        db.session.commit()
        return jsonify({'success': 'true'}), 200

    except Exception as e:
        # 发生错误时回滚并打印错误信息
        db.session.rollback()
        print(f"删除 PickerList 失败: {str(e)}")

        return jsonify({'success': 'false','error': f'删除名单失败: {str(e)}'}), 400