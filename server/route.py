from flask import (Flask, make_response, render_template, 
    request, redirect, url_for, session,flash,abort)

app=Flask(__name__)
app.secret_key='inirandom'

@app.errorhandler(401)
def not_login(e):
    return render_template('admin/401.html'),401

@app.route('/')
def utama():
    return render_template ('home.html')

@app.route('/produk')
def produk():
    return render_template ('produk.html')

@app.route('/keranjang')
def keranjang():
    return render_template ('keranjang.html')

@app.route('/notifikasi')
def notifikasi():
    return render_template ('notifikasi.html')

@app.route('/trans')
def trans():
    return render_template ('admin/transaksi.html')




@app.route('/akun',methods=['GET','POST'])
def akun():
    if request.method=='POST':
        email=request.form['txtnumber']
        passnya=request.form['txtpass']
        session['username'] =request.form['txtnumber']
        if email=='20201347' and passnya=='20201347':
            flash('Anda Berhasil Log in')
            return render_template('admin/index.html',username=session['username'])
        else: 
            abort(401)
            #return redirect(url_for('akun'))
    return render_template ('akun.html')

app.route('/logout')
def logout():
    session.pop('username',None)
    return render_template('home.html')


@app.route('/admin')
def administrator():
    return render_template ('admin/index.html')
