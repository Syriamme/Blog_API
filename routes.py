# routes.py
from flask import request, jsonify
from app import app, bcrypt, session, db
from models import User, BlogPost
from helpers import create_jwt_token, jwt_login_required

@app.route('/register', methods=['POST'], endpoint='register')
def register():
    data = request.get_json()
    hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')
    user = User(username=data['username'], password=hashed_password)
    session.add(user)
    session.commit()
    return jsonify(message='User registered successfully'), 201

@app.route('/login', methods=['POST'], endpoint='login')
def login():
    data = request.get_json()
    user = session.query(User).filter_by(username=data['username']).first()
    if user and bcrypt.check_password_hash(user.password, data['password']):
        access_token = create_jwt_token(user)
        return jsonify(access_token=access_token), 200
    return jsonify(message='Invalid credentials'), 401

@app.route('/blogposts', methods=['GET'], endpoint='get_blogposts')
def get_blogposts():
    blogposts = session.query(BlogPost).all()
    result = [{'id': post.id, 'title': post.title, 'content': post.content, 'author': post.author, 'timestamp': post.timestamp} for post in blogposts]
    return jsonify(result), 200

@app.route('/blogpost/<int:post_id>', methods=['GET'], endpoint='get_blogpost')
def get_blogpost(post_id):
    post = session.query(BlogPost).get(post_id)
    if post:
        result = {'id': post.id, 'title': post.title, 'content': post.content, 'author': post.author, 'timestamp': post.timestamp}
        return jsonify(result), 200
    return jsonify(message='Blog post not found'), 404

@app.route('/blogpost', methods=['POST'], endpoint='create_blogpost')
@jwt_login_required
def create_blogpost(current_user):
    data = request.get_json()
    post = BlogPost(title=data['title'], content=data['content'], author=current_user.username)
    session.add(post)
    session.commit()
    return jsonify(message='Blog post created successfully'), 201

@app.route('/blogpost/<int:post_id>', methods=['PUT'], endpoint='update_blogpost')
@jwt_login_required
def update_blogpost(current_user, post_id):
    post = session.query(BlogPost).get(post_id)
    if post and post.author == current_user.username:
        data = request.get_json()
        post.title = data['title']
        post.content = data['content']
        session.commit()
        return jsonify(message='Blog post updated successfully'), 200
    return jsonify(message='Blog post not found or unauthorized'), 404

@app.route('/blogpost/<int:post_id>', methods=['DELETE'], endpoint='delete_blogpost')
@jwt_login_required
def delete_blogpost(current_user, post_id):
    post = session.query(BlogPost).get(post_id)
    if post and post.author == current_user.username:
        session.delete(post)
        session.commit()
        return jsonify(message='Blog post deleted successfully'), 200
    return jsonify(message='Blog post not found or unauthorized'), 404
