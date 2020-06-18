from sql_alchemy import banco

class CausaModel(banco.Model):
    __tablename__ = 'causas'

    causa_id = banco.Column(banco.Integer, primary_key=True)
    nome = banco.Column(banco.String(80))
    autor = banco.Column(banco.String(80))
    meta = banco.Column(banco.Integer)
    descricao = banco.Column(banco.String(200))

    def __init__(self, causa_id, nome, autor, meta, descricao):
        self.causa_id = causa_id
        self.nome = nome
        self.autor = autor
        self.meta = meta
        self.descricao = descricao

    def json(self):
        return {
            'causa_id': self.causa_id,
            'nome': self.nome,
            'autor': self.autor,
            'meta': self.meta,
            'descricao': self.descricao
        }

    @classmethod
    def find_causa(cls, causa_id): 
        causa = cls.query.filter_by(causa_id=causa_id).first()
        if causa:
            return causa
        return None

    def save_causa(self):
        banco.session.add(self)
        banco.session.commit()

    def update_causa(self, nome, autor, meta, descricao):
        self.nome = nome
        self.autor = autor
        self.meta = meta
        self.descricao = descricao

    def delete_causa(self):
        banco.session.delete(self)
        banco.session.commit()