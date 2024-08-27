from flask import render_template, request, redirect, flash, url_for
from database import db
from models.diario import Diario
from flask import Blueprint

bp_diario = Blueprint("diario", __name__, template_folder='templates')

@bp_diario.route('/recovery')
def recovery():
    dados = Diario.query.all()
    return render_template('diario_recovery.html', dados=dados)

@bp_diario.route('/create', methods=['GET', 'POST'])
def create():
    if request.method=="GET":
	    return render_template('diario_create.html')

    if request.method=="POST":
        titulo = request.form['titulo']
        disciplina = request.form['disciplina']
        d = Diario(titulo,disciplina)
        db.session.add(d)
        db.session.commit()
        return redirect(url_for('diario.recovery'))

    



