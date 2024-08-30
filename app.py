from flask import Flask, render_template, request
import pandas as pd
from sqlalchemy import create_engine

app = Flask(__name__)

# Kết nối cơ sở dữ liệu
from sqlalchemy import create_engine

# Tạo engine kết nối đến cơ sở dữ liệu PostgreSQL
engine = create_engine('postgresql+psycopg2://username:password@localhost/your_database')


@app.route('/')
def index():
    data = pd.read_sql('SELECT * FROM your_table WHERE id = 1', engine).iloc[0]
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
