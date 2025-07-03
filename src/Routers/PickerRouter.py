#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：Vertexa 
@File    ：PickerRouter.py
@IDE     ：PyCharm 
@Author  ：Sean Han
@Date    ：2025/7/3 13:29 
"""
from flask import Blueprint, render_template, request, redirect, url_for
from select import select

from src.Models.Picker.PickerItem import PickerItem

picker_bp = Blueprint('picker', __name__)

# 获取所有的名单
@picker_bp.route('/all_lists', methods=['GET'])
def get_all_lists():
    return 0

# 获取指定名单中所有的项
@picker_bp.route('/all_items/<int:list_id>', methods=['GET'])
def get_all_items(list_id):
    try:
        # 执行查询
        stmt = select(PickerItem).where(PickerItem.list_id == {list_id})
        items = session.scalars(stmt).all()

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