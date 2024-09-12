from utils import db

class capitais(db.Model):
  __tablename__= "capitais"
  id = db.Column(db.Integer, primary_key = True)
  regiao = db.Column(db.String(100))
  estado = db.Column(db.String(100))
  sigla = db.Column(db.String(100))
  capital = db.Column(db.String(100))


  def __init__(self, regiao, estado, sigla, capital):
    self.regiao = regiao
    self.estado = estado
    self.sigla= sigla
    self.capital = capital

