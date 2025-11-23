from flask import render_template, Blueprint, request, jsonify

def register_routes(app):
    @app.route('/')
    def home():
        return render_template('home.html')

    @app.route('/catalogue')
    def catalogue():
        return render_template('catalogue.html')

    @app.route('/customize')
    def customizer():
        return render_template('customizer_page.html')
