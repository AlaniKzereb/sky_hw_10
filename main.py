from flask import Flask

from utils import load_candidates, get_all, get_by_pk, get_by_skill

data = get_all(load_candidates("candidates.json"))
app = Flask(__name__)


@app.route('/')
def page_index():
    line = '<pre>'
    for i in data:
        line += f'{i} \n \n'
    line += '</pre>'
    return line


@app.route('/candidates/<int:pk>')
def get_user(pk):
    user = get_by_pk(pk, data)
    if user:
        line = f'<img src="{user.picture}">'
        line += f'<pre> {user} </pre>'
    else:
        line = "NOT FOUND"
    return line


@app.route("/skills/<x>")
def get_users(x):
    x = x.lower()
    users = get_by_skill(x, data)
    if users:
        str = '<pre>'
        for i in users:
            str += f'{i} \n \n'
        str += '</pre>'
    else:
        str = "NOT FOUND"
    return str


if __name__ == '__main__':
    app.run(port=5000)
