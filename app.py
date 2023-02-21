from flask import Flask, make_response, render_template
import csv

server_1 = 'svr1.csv'
server_2 = 'svr2.csv'

app = Flask(__name__)

def log_parser(file):
    f_list = []
    with open(file) as f:
        csv_f = csv.reader(f, delimiter = ',')
        for row in csv_f:
            f_list.append(row)
    s_head = f_list.pop(0)
    return s_head, f_list

@app.route('/')
def hello():
    return "<p>Hello World!</p>"

@app.route('/dashboard/')
def dashboard():
    s1_head, s1_cont = log_parser(server_1)
    s2_head, s2_cont = log_parser(server_2)
    return render_template(
        'dashboard.html', 
        s1_head = s1_head,
        s1_cont = s1_cont,
        s2_head = s2_head,
        s2_cont = s2_cont
        )

if __name__ == '__main__':
    app.run(host='127.0.0.1', port='8080')