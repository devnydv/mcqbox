from mcqbox import app

from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from mcqbox.model import db, Category, Subcategory, Question

@app.route('/backend')
def back():
    return 'lolhjghgj'