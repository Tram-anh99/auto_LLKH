from flask import Flask, render_template, request
import pandas as pd
from sqlalchemy import create_engine

app = Flask(__name__)

# Kết nối cơ sở dữ liệu
DATABASE_URI = 'sqlite:///your_database.db'
engine = create_engine(DATABASE_URI)

@app.route('/')
def index():
    data = pd.read_sql('SELECT * FROM your_table WHERE id = 1', engine).iloc[0]
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
