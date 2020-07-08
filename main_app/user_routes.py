import os
import secrets
from datetime import datetime
from flask import render_template, url_for, redirect, request,flash
from main_app import app, db, current_user,login_user, logout_user,login_required
from main_app.models import Message, Announcement, Testimony, Book, Gallery, User


#index page
@app.route("/")
def index():
    return render_template("user/index.html")

#gallery page
@app.route("/rcffutminna/galleries", methods=['GET','POST'])
def view_gallery():
    page = request.args.get('page', 1, type=int)
    galleries = Gallery.query.order_by(Gallery.id.desc()).paginate(page=page,per_page=9)
    return render_template("user/gallery.html",galleries=galleries)