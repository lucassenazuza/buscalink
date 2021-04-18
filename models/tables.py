from app import db


class Element(db.Model):
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    elementName = db.Column(db.String(100))

    def __init__(self,elementName):
        self.elementName = elementName
    def __repr__(self):
        return "<Element %r>" % self.elementName

class Link(db.Model):
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    element_id=db.Column(db.Integer,db.ForeignKey('element.id'))
    link = db.Column(db.String(150))
    def __init__(self,link,element_id):
        self.link=link
        self.element_id=element_id
    def __repr__(self):
        return "<Link %r>" % self.link


