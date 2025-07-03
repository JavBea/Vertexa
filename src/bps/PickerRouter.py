#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：Vertexa 
@File    ：PickerRouter.py
@IDE     ：PyCharm 
@Author  ：Sean Han
@Date    ：2025/7/3 13:29 
"""
from flask import Blueprint,request
from src.services import PickerService

picker_bp = Blueprint('picker', __name__)

# 获取所有的名单
@picker_bp.route('/all_lists', methods=['GET'])
def get_all_lists():
    return PickerService.get_all_lists()

# 获取指定名单中所有的项
@picker_bp.route('/all_items/<int:list_id>', methods=['GET'])
def get_all_items(list_id):
    return PickerService.get_all_items(list_id)

# 上传处理excel文件
@picker_bp.route('/upload', methods=['POST'])
def upload_file():
    return PickerService.upload_file(request)

# 建立新名单
@picker_bp.route('/insert_list', methods=['GET','POST'])
def insert_list():
    return PickerService.insert_list()

# 重命名名单
@picker_bp.route('/rename_list/<int:list_id>/<str:name>', methods=['GET','POST'])
def rename_list(list_id,name):
    return PickerService.delete_list(list_id)

# 删除名单
@picker_bp.route('/delete_list/<int:list_id>', methods=['GET','POST'])
def delete_list(list_id):
    return PickerService.delete_list(list_id)