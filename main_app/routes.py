import os
import secrets
from datetime import datetime
from flask import render_template, url_for, redirect, request,flash
from main_app import app, db
from main_app.models import Message, Announcement


#middleware - save audiofiles
def save_audio(media, media_title):
    _, f_ext = os.path.splitext(media.filename)
    media_fn = media_title + f_ext
    media_path = os.path.join(app.root_path, 'static/message_audios', media_fn)
    media.save(media_path)
    return media_fn

#middleware - save image files
def save_img(img):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(img.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/church_img', picture_fn)
    img.save(picture_path)
    return picture_fn

#dashboard routes
@app.route("/")
def index():
    return render_template("admin/index.html")

@app.route("/admin/announcement", methods=['GET','POST'])
def announcement():
    announcements = Announcement.query.all()
    if request.method == "POST":
        image = save_img(request.files['imganounc'])
        new_announcement = Announcement(annouce=request.form['announce'], image=image, content=request.form['content'])
        new_announcement.save_to_database()
        flash("Annoucement Created Successfully", "success")
        return redirect(url_for('announcement'))
    return render_template('admin/announcement.html', announcements=announcements)

@app.route('/admin/announcement/<int:id>/edit', methods=['GET','POST'])
def edit_announcement(id):
    announcement = Announcement.find_by_id(id)
    if request.method == "POST":
        if request.form['announce'] and request.form['content'] and request.files['imganounc']:
            image = save_img(request.files['imganounc'])
            announcement.annouce = request.form['announce']
            announcement.image = image
            announcement.content = request.form['content']
            db.session.commit()
            flash('Announcement Updated', "success")
            return redirect(url_for('announcement'))
        elif request.form['announce'] and request.form['content']:
            announcement.annouce = request.form['announce']
            announcement.content = request.form['content']
            db.session.commit()
            flash('Announcement Updated', "success")
            return redirect(url_for('announcement'))
    return render_template('admin/edit_announcement.html', announcement=announcement)

@app.route('/admin/announcement/<int:id>/delete')
def delete_announcement(id):
    announce = Announcement.find_by_id(id)
    announce.remove_from_database()
    flash("Annoucement Deleted Successfully","danger")
    return redirect(url_for('announcement'))

@app.route('/admin/books')
def books():
    return render_template('admin/books.html')

@app.route('/admin/gallery')
def gallery():
    return render_template('admin/gallery.html')

@app.route('/admin/messages', methods=['GET','POST'])
def messages():
    messages = Message.query.all()
    if request.method == "POST":
        print(request.form['date'])
        message_audio = save_audio(request.files['audio'], request.form['title'])
        message = Message(
            minister=request.form['author'], 
            title=request.form['title'], 
            tag=request.form['tag'], 
            message=request.form['message'],
            audio=message_audio.replace(" ","")
            )
        message.save_to_database()
        flash("Message Added Successfully", "success")
        return redirect(url_for('messages'))
    return render_template('admin/message.html', messages=messages)

@app.route('/admin/messages/<int:id>/edit', methods=['GET','POST'])
def edit_message(id):
    message = Message.find_by_id(id)
    if request.method == "POST":
        if request.form['author'] and request.form['title'] and request.form['tag'] and request.files['audio'] and request.form['message']:
            message_audio = save_audio(request.files['audio'], request.form['title'])
            message.minister = request.form['author']
            message.title = request.form['title']
            message.tag = request.form['tag']
            message.audio = message_audio
            message.message = request.form['message']
            db.session.commit()
            flash('Message Updated', "success")
            return redirect(url_for('messages'))
        elif request.form['author'] and request.form['title'] and request.form['tag'] and request.form['message']:
            message.minister = request.form['author']
            message.title = request.form['title']
            message.tag = request.form['tag']
            message.message = request.form['message']
            db.session.commit()
            flash('Message Updated', "success")
            return redirect(url_for('messages'))
    return render_template('admin/edit_message.html', message=message)

@app.route('/admin/messages/<int:id>/delete')
def delete_message(id):
    message = Message.find_by_id(id)
    message.remove_from_database()
    flash("Message Deleted Successfully","danger")
    return redirect(url_for('messages'))

@app.route('/admin/testimonies')
def testimony():
    return render_template('admin/testimony.html')

