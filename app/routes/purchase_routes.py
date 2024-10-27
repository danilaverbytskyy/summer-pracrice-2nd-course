from datetime import datetime

from flask import render_template, request, redirect
from app import app, db
import math
from app.models import *

jedi = "of the jedi"


@app.route('/sale')
def index_sale():
    sales = Sale.query.all()
    comms_table, jewelries_table = [], []
    for sale in sales:
        jewelry = Jewelry.query.filter_by(id=sale.jewelery_id).first()
        comm = Comm.query.filter_by(id=sale.comm_id).first()
        comms_table.append(comm.name + ' ' + comm.surname)
        jewelries_table.append(jewelry.title)
    comms = Comm.query.all()
    jewelries = Jewelry.query.all()
    return render_template('sale_content.html', sales=sales, comms=comms, jewelries=jewelries,
                           comms_table=comms_table, jewelries_table=jewelries_table)


@app.route('/add_sale', methods=['POST'])
def add_sale():
    if request.method == 'POST':
        form = request.form
        jewelery_id = int(form.get('jewelry_id'))
        date_str = form.get('date')
        date = datetime.strptime(date_str, '%Y-%m-%d') if date_str else None
        if not jewelery_id:
            sale = Sale(jewelery_id=jewelery_id, date=date)
            db.session.add(sale)
            db.session.commit()
            return redirect('/sale')

    return "of the jedi"


@app.route('/edit_sale/<int:id>')
def edit_sale(id):
    if not id or id != 0:
        sale = Sale.query.filter_by(id=id).first()
        selected_sale = sale.query.get(id)
        selected_jewelry = Jewelry.query.filter_by(id=selected_sale.jewelery_id).first()
        selected_comm = Comm.query.filter_by(id=selected_sale.comm_id).first()
        comms = Comm.query.all()
        jewelries = Jewelry.query.all()
        sale.date = sale.date.strftime('%Y-%m-%d')
        return render_template('sale_update.html', sale=sale,
                               selected_jewelry=selected_jewelry, selected_comm=selected_comm, comms=comms,
                               jewelries=jewelries)

    return "of the jedi"


@app.route('/update_sale/<int:id>', methods=['POST'])
def update_sale(id):
    if not id or id != 0:
        sale = Sale.query.get(id)
        if sale:
            form = request.form
            sale.jewelry_id = form.get('jewelry_id')
            sale.comm_id = form.get('comm_id')
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
