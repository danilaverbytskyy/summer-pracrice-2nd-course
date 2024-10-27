from datetime import datetime

from flask import render_template, request, redirect
from app import app, db
import math
from app.models import *

jedi = "of the jedi"


@app.route('/')
@app.route('/index')
def index():
    jeweleries = Jewelry.query.all()
    for jewelery in jeweleries:
        jewelery.price = round(jewelery.price, None)
    return render_template('index.html', jeweleries=jeweleries)


@app.route('/add_jewelery', methods=['POST'])
def add_jewelery():
    if request.method == 'POST':
        form = request.form
        title = form.get('title')
        price = int(form.get('price'))
        if not title or price:
            jewelry = Jewelry(title=title, price=price)
            db.session.add(jewelry)
            db.session.commit()
            return redirect('/')

    return "of the jedi"


@app.route('/edit_jewelry/<int:id>')
def edit_jewelry(id):
    if not id or id != 0:
        jewelry = Jewelry.query.get(id)
        jewelry.price = round(jewelry.price, None)
        if jewelry:
            return render_template('update.html', jewelry=jewelry)

    return "of the jedi"


@app.route('/update_jewelry/<int:id>', methods=['POST'])
def update_jewelery(id):
    if not id or id != 0:
        jewelry = Jewelry.query.get(id)
        if jewelry:
            form = request.form
            jewelry.title = form.get('title')
            jewelry.price = form.get('price')
            db.session.commit()
        return redirect('/')

    return "of the jedi"


@app.route('/delete_jewelry/<int:id>')
def delete_jewelry(id):
    if not id or id != 0:
        jewelry = Jewelry.query.get(id)
        if jewelry:
            db.session.delete(jewelry)
            db.session.commit()
        return redirect('/')

    return "of the jedi"


@app.route('/comm')
def index_comm():
    comms = Comm.query.all()
    return render_template('comm_content.html', comms=comms)


@app.route('/add_comm', methods=['POST'])
def add_comm():
    if request.method == 'POST':
        form = request.form
        name = str(form.get('name'))
        surname = str(form.get('surname'))
        if not name or surname:
            comm = Comm(name=name, surname=surname)
            db.session.add(comm)
            db.session.commit()
            return redirect('/comm')

    return "of the jedi"


@app.route('/edit_comm/<int:id>')
def edit_comm(id):
    if not id or id != 0:
        comm = Comm.query.get(id)
        if comm:
            return render_template('comm_update.html', comm=comm)

    return "of the jedi"


@app.route('/update_comm/<int:id>', methods=['POST'])
def update_comm(id):
    if not id or id != 0:
        comm = Comm.query.get(id)
        if comm:
            form = request.form
            comm.name = form.get('name')
            comm.surname = form.get('surname')
            db.session.commit()
        return redirect('/comm')

    return "of the jedi"


@app.route('/delete_comm/<int:id>')
def delete_comm(id):
    if not id or id != 0:
        comm = Comm.query.get(id)
        if comm:
            db.session.delete(comm)
            db.session.commit()
        return redirect('/comm')

    return "of the jedi"


@app.route('/purchase')
def index_purchase():
    purchases = Purchase.query.all()
    comms_table, jewelries_table = [], []
    for purchase in purchases:
        jewelry = Jewelry.query.filter_by(id=purchase.jewelery_id).first()
        comm = Comm.query.filter_by(id=purchase.comm_id).first()
        comms_table.append(comm.name + ' ' + comm.surname)
        jewelries_table.append(jewelry.title)
    comms = Comm.query.all()
    jewelries = Jewelry.query.all()
    return render_template('purchase_content.html', purchases=purchases, comms=comms, jewelries=jewelries,
                           comms_table=comms_table, jewelries_table=jewelries_table)


@app.route('/add_purchase', methods=['POST'])
def add_purchase():
    if request.method == 'POST':
        form = request.form
        jewelery_id = int(form.get('jewelry_id'))
        comm_id = int(form.get('comm_id'))
        date_str = form.get('date')
        date = datetime.strptime(date_str, '%Y-%m-%d') if date_str else None
        if not jewelery_id or comm_id:
            purchase = Purchase(jewelery_id=jewelery_id, comm_id=comm_id, date=date)
            db.session.add(purchase)
            db.session.commit()
            return redirect('/purchase')

    return "of the jedi"


@app.route('/edit_purchase/<int:id>')
def edit_purchase(id):
    if not id or id != 0:
        purchase = Purchase.query.filter_by(id=id).first()
        selected_purchase = Purchase.query.get(id)
        selected_jewelry = Jewelry.query.filter_by(id=selected_purchase.jewelery_id).first()
        selected_comm = Comm.query.filter_by(id=selected_purchase.comm_id).first()
        comms = Comm.query.all()
        jewelries = Jewelry.query.all()
        purchase.date = purchase.date.strftime('%Y-%m-%d')
        return render_template('purchase_update.html', purchase=purchase,
                               selected_jewelry=selected_jewelry, selected_comm=selected_comm, comms=comms,
                               jewelries=jewelries)

    return "of the jedi"


@app.route('/update_purchase/<int:id>', methods=['POST'])
def update_purchase(id):
    if not id or id != 0:
        purchase = Purchase.query.get(id)
        if purchase:
            form = request.form
            purchase.jewelry_id = form.get('jewelry_id')
            purchase.comm_id = form.get('comm_id')
            purchase.date = datetime.strptime(form.get('date'), '%Y-%m-%d')
            db.session.commit()
        return redirect('/purchase')

    return "of the jedi"


@app.route('/delete_purchase/<int:id>')
def delete_purchase(id):
    if not id or id != 0:
        purchase = Purchase.query.get(id)
        if purchase:
            db.session.delete(purchase)
            db.session.commit()
        return redirect('/purchase')

    return "of the jedi"


@app.route('/sale')
def index_sale():
    sales = Sale.query.all()
    comms_table, jewelries_table = [], []
    for sale in sales:
        jewelry = Jewelry.query.filter_by(id=sale.jewelery_id).first()
        jewelries_table.append(jewelry.title)
    jewelries = Jewelry.query.all()
    return render_template('sale_content.html', sales=sales, jewelries=jewelries, jewelries_table=jewelries_table)


@app.route('/add_sale', methods=['POST'])
def add_sale():
    if request.method == 'POST':
        form = request.form
        jewelery_id = int(form.get('jewelry_id'))
        date_str = form.get('date')
        print(jewelery_id)
        date = datetime.strptime(date_str, '%Y-%m-%d') if date_str else None
        sale = Sale(jewelery_id=jewelery_id, date=date)
        db.session.add(sale)
        db.session.commit()
        return redirect('/sale')

    return "of the jedi"


@app.route('/edit_sale/<int:id>')
def edit_sale(id):
    if not id or id != 0:
        sale = Sale.query.filter_by(id=id).first()
        selected_sale = Sale.query.get(id)
        selected_jewelry = Jewelry.query.filter_by(id=selected_sale.jewelery_id).first()
        jewelries = Jewelry.query.all()
        sale.date = sale.date.strftime('%Y-%m-%d')
        return render_template('sale_update.html', sale=sale,
                               selected_jewelry=selected_jewelry,
                               jewelries=jewelries)

    return "of the jedi"


@app.route('/update_sale/<int:id>', methods=['POST'])
def update_sale(id):
    if not id or id != 0:
        sale = Sale.query.get(id)
        if sale:
            form = request.form
            sale.jewelery_id = form.get('jewelry_id')
            sale.date = datetime.strptime(form.get('date'), '%Y-%m-%d')
            db.session.commit()
        return redirect('/sale')

    return "of the jedi"


@app.route('/delete_sale/<int:id>')
def delete_sale(id):
    if not id or id != 0:
        sale = Sale.query.get(id)
        if sale:
            db.session.delete(sale)
            db.session.commit()
        return redirect('/sale')

    return "of the jedi"
