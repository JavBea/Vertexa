#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：Vertexa 
@File    ：config.py.py
@IDE     ：PyCharm 
@Author  ：Sean Han
@Date    ：2025/7/3 14:02 
"""

class Config:

    # 数据库相关配置
    SQLALCHEMY_DATABASE_URI = 'mysql://root:192508Qp!@47.94.95.8/vertexa'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'your-secret-key'  # 用于会话安全

    # 设置上传文件保存目录
    UPLOAD_FOLDER = 'tmp'
