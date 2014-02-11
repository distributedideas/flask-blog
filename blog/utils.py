from functools import partial

from flask import render_template

from blog.models import Tag, User, Post, Service

def get_tags():
    return Tag.query.all()

def get_users():
    return User.query.all()

def get_posts():
    return Post.query.all()

render_template_with_models = partial(render_template, users=get_users, tags=get_tags, posts=get_posts)