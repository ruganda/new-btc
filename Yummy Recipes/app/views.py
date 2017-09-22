
from functools import wraps
from flask import Flask, render_template, session, flash, redirect, url_for, request
from models import User
from . import app


@app.route('/')
def index():
    return render_template ('home.html')  


 

