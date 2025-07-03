#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：Vertexa 
@File    ：PickerItemDao.py
@IDE     ：PyCharm 
@Author  ：Sean Han
@Date    ：2025/7/3 15:56 
"""
from functools import singledispatch
from typing import Optional
from src.app.extensions import db
from src.models.Picker.PickerItem import PickerItem

@singledispatch
def insert(name: str, list_id: int, probability: Optional[float] = None) -> int:
    """
    插入新的 PickerItem 记录

    参数:
        name: 项目名称
        list_id: 关联的列表ID
        probability: 可选的概率值

    返回:
        成功时返回新记录的ID，失败时返回-1
    """
    # 配置数据库连接（根据你的实际情况调整）

    try:
        # 创建新记录（不需要指定id，因为它是自增的）
        new_item = PickerItem(
            name=name,
            list_id=list_id,
            probability=probability
        )

        # 添加到会话并提交
        db.session.add(new_item)
        db.session.commit()

        # 刷新对象以获取生成的ID
        db.session.refresh(new_item)

        # 返回新记录的ID
        return new_item.id

    except Exception as e:
        # 发生错误时回滚并打印错误信息
        db.session.rollback()
        print(f"插入 PickerItem 失败: {str(e)}")
        return -1

