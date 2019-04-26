from _init_ import app
from models import Blog
from flask import request, url_for, redirect, render_template

@app.route('/', methods=['GET', 'POST'])
def index():
    page = int(request.args.get('page', 1))
    paginate = Blog.query.paginate(page, 3)
    arts = paginate.items
    id = request.args.get('id')
    if id == None:
        return render_template('index.html', arts=arts, paginate=paginate)
    return redirect(url_for('artice', result_id = str(id)))

@app.route('/?id=<path:result_id>/')
def artice(result_id):
    if result_id:
        data = Blog.query.all()
        url_root = request.url_root
        for u in data:
            if int(result_id) == u.id:
                return render_template('artice.html', data=u, url_index=url_root)
    else:
        render_template('artice.html')

@app.route('/index')
def index1():
    return redirect(url_for('index'))

@app.route('/category')
def category():
    return render_template('category.html')

@app.route('/artice')
def artice1():
    return redirect(url_for('artice'))

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/information')
def information():
    return render_template('information.html')

if __name__ == '__main__':
    app.debug = app.config['DEBUG']
    app.run(host='127.0.0.1', port=8888)
