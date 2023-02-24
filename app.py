from flask import Flask, make_response, render_template
import csv

#Server files
server_1 = 'svr1.csv'
server_2 = 'svr2.csv'

app = Flask(__name__)

def pinger() -> bool:
    """Ping server for availability"""
    return True

def log_parser(file) -> dict:
    """Reads log file sent by remote server and returns dict of the data"""
    f_list = []
    s_dict = {}
    with open(file) as f:
        csv_f = csv.reader(f, delimiter = ',')
        for row in csv_f:
            f_list.append(row)
    s_head = f_list.pop(0)
    s_dict['name'] = s_head[0]
    s_dict['ip'] = s_head[1]
    s_dict['last_check'] = s_head[2]
    s_dict['avail'] = pinger()
    s_dict['dir'] = f_list
    return s_dict

@app.route('/')
def hello():
    return "<p>Hello World!</p>"

@app.route('/dashboard/')
def dashboard():
    svr_1 = log_parser(server_1)
    svr_2 = log_parser(server_2)
    return render_template('dashboard.html', svr_1 = svr_1, svr_2 = svr_2)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port='8080')