# Foodie_ECommerce_V1.0/app/routes.py

from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from .models import Product, get_mock_products

# Crea un Blueprint para las rutas principales (Vistas)
main = Blueprint('main', _name_)

@main.route('/')
def home():
    """Ruta para la página principal."""
    return render_template('home.html', title='Inicio - Foodie Co.')

@main.route('/catalogue')
def catalogue():
    """Ruta para el catálogo de productos."""
    # Simulación de obtención de productos desde la DB (usando mock)
    products = get_mock_products()
    return render_template('catalogue.html', products=products, title='Catálogo de Platos')

@main.route('/customizer')
def customizer_page():
    """Ruta para la herramienta de personalización de platos."""
    # Podrías cargar datos iniciales de ingredientes aquí
    return render_template('customizer_page.html', title='Personaliza tu Plato')

# --- Rutas Legales ---

@main.route('/legal/claims-book')
def claims_book():
    """Ruta para el Libro de Reclamaciones."""
    return render_template('legal/claims_book.html', title='Libro de Reclamaciones')

@main.route('/legal/shipping-policy')
def shipping_policy():
    """Ruta para la Política de Envíos."""
    return render_template('legal/shipping_policy.html', title='Política de Envíos')

# --- Rutas de Usuario (Simuladas) ---

@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Lógica de autenticación (simulación)
        username = request.form.get('username')
        password = request.form.get('password')
        if username == 'test' and password == '123':
            session['logged_in'] = True
            session['user_id'] = 'mock_user_123'
            flash('Inicio de sesión exitoso.', 'success')
            return redirect(url_for('main.home'))
        else:
            flash('Usuario o contraseña incorrectos.', 'danger')
    return render_template('login.html', title='Iniciar Sesión')

@main.route('/logout')
def logout():
    session.pop('logged_in', None)
    session.pop('user_id', None)
    flash('Sesión cerrada.', 'info')
    return redirect(url_for('main.home'))