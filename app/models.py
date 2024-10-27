from app import db


class Entry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), index=True, nullable=False)
    description = db.Column(db.String(120), index=True, nullable=False)
    status = db.Column(db.Boolean, default=False)


class Jewelry(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(64), index=True, nullable=False)
    price = db.Column(db.Float, index=True, nullable=False)


class Sale(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    jewelery_id = db.Column(db.Integer, index=True, nullable=False)
    date = db.Column(db.DateTime, index=True, nullable=False)
    status = db.Column(db.Boolean, default=True)


class Purchase(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    jewelery_id = db.Column(db.Integer, index=True, nullable=False)
    comm_id = db.Column(db.Integer, index=True, nullable=False)
    date = db.Column(db.DateTime, index=True, nullable=False)
    status = db.Column(db.Boolean, default=True)


class Comm(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64), index=True, nullable=False)
    surname = db.Column(db.String(64), index=True, nullable=False)
