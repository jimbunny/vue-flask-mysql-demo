#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:jingtongyu
# datetime:2020/6/7 10:14 下午
# software: PyCharm

from flask import current_app
from . import db
from .base import BaseModel
from sqlalchemy.exc import SQLAlchemyError
from werkzeug.security import generate_password_hash, check_password_hash


class UsersModel(db.Model, BaseModel):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(250),  unique=True, nullable=False)
    username = db.Column(db.String(250),  unique=True, nullable=False)
    password = db.Column(db.String(250),nullable=False)
    permission = db.Column(db.String(50), default='test', nullable=False)
    avatar = db.Column(db.String(500), default="http://beautiful.panm.cn/vue-admin-beautiful/static/img/user.20010688.gif", nullable=False)
    login_time = db.Column(db.Integer)

    def __init__(self, username, password, email, permission):
        self.username = username
        self.password = password
        self.email = email
        self.permission = permission

    def __str__(self):
        return "Users(id='%s')" % self.id

    def set_password(self, password):
        return generate_password_hash(password)

    def check_password(self, hash, password):
        return check_password_hash(hash, password)

    def get(self, id):
        return self.query.filter_by(id=id).first()

    def add(self, user):
        db.session.add(user)
        return session_commit()

    def update(self):
        return session_commit()

    def delete(self, id):
        self.query.filter_by(id=id).delete()
        return session_commit()


def session_commit():
    try:
        db.session.commit()
    except SQLAlchemyError as e:
        db.session.rollback()
        reason = str(e)
        current_app.logger.info(e)
        return reason
