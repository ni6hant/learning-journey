from flask import render_template, url_for, flash, redirect, request, abort, Blueprint, jsonify
from flask_login import current_user, login_required
from flaskblog import db
from flaskblog.models import Post, AuditLog
from flaskblog.posts.forms import PostForm

posts=Blueprint('posts', __name__)


@posts.route("/post/new", methods=['POST', 'GET'])
@login_required
def new_post():
    form=PostForm()
    if form.validate_on_submit():
        post=Post(title=form.title.data, content=form.content.data, author=current_user)
        db.session.add(post)
        db.session.commit()

        #audit log
        audit_log=AuditLog(action_type='create_post',user_id=current_user.id, old_data={}, new_data=post.to_dict())
        db.session.add(audit_log)
        db.session.commit()

        flash('Your post has been created!', 'success')
        return redirect(url_for('main.home'))
    return render_template('create_post.html', title='New Post', form=form,legend='Update Post')

@posts.route("/post/<int:post_id>", methods=['POST', 'GET'])
def post(post_id):
    post=Post.query.get_or_404(post_id)
    return render_template('post.html', post=post, title=post.title)

@posts.route("/post/<int:post_id>/update", methods=['POST', 'GET'])
@login_required
def update_post(post_id):
    post=Post.query.get_or_404(post_id)
    if post.author!=current_user:
        abort(403)
    form=PostForm()
    if form.validate_on_submit():
        old_data=post.to_dict()
        post.title=form.title.data
        post.content=form.content.data
        db.session.commit()

        #audit log
        audit_log=AuditLog(action_type='update_post',user_id=current_user.id, old_data=old_data, new_data=post.to_dict())
        db.session.add(audit_log)
        db.session.commit()

        flash('Your post has been updated!', 'success')
        return redirect(url_for('posts.post', post_id=post.id))
    elif request.method=='GET':
        form.title.data=post.title
        form.content.data=post.content
    
    return render_template('create_post.html', title='Update Post', form=form ,legend='Update Post')


@posts.route("/post/<int:post_id>/delete", methods=['POST'])
@login_required
def delete_post(post_id):
    post=Post.query.get_or_404(post_id)
    old_data=post.to_dict()
    if post.author!=current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()

    #audit log
    audit_log=AuditLog(action_type='delete_post',user_id=current_user.id, old_data=old_data, new_data={})
    db.session.add(audit_log)
    db.session.commit()

    flash('Your post has been deleted!', 'success')
    return redirect(url_for('main.home'))


