from flask import render_template, request, redirect, flash, url_for
from database import db
from models.usuario import Usuario
from flask import Blueprint
import hashlib

bp_usuario = Blueprint("usuario", __name__, template_folder='templates')

@bp_usuario.route('/recovery')
def recovery():
    dados = Usuario.query.all()
    return 'Aqui vai aparecer os dados de todos os usuários'

@bp_usuario.route('/create', methods=['GET', 'POST'])
def create():
    if request.method=="GET":
        return render_template('usuario_create.html')

    if request.method=="POST":
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']

        #md5 = hashlib.md5()
        #md5.update(senha)
        #senha_cripto = md5.hexdigest().encode('utf-8')

        u = Usuario(nome, email, senha)
        db.session.add(u)
        db.session.commit()
        return redirect(url_for('usuario.recovery'))