from flask import Flask, request, redirect, render_template, url_for
import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent.parent / 'tasks.db'

def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT,
        status TEXT NOT NULL DEFAULT 'todo'
    )
    ''')
    conn.commit()
    conn.close()

app = Flask(__name__)
init_db()

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    conn = get_db()
    tasks = conn.execute('SELECT * FROM tasks ORDER BY id DESC').fetchall()
    conn.close()
    return render_template('index.html', tasks=tasks)

@app.route('/task', methods=['POST'])
def create_task():
    title = request.form.get('title','').strip()
    description = request.form.get('description','').strip()
    if not title:
        return "Título é obrigatório", 400
    conn = get_db()
    conn.execute('INSERT INTO tasks (title,description,status) VALUES (?,?,?)', (title, description, 'todo'))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/task/<int:task_id>/delete', methods=['POST'])
def delete_task(task_id):
    conn = get_db()
    conn.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/task/<int:task_id>/toggle', methods=['POST'])
def toggle_task(task_id):
    conn = get_db()
    row = conn.execute('SELECT status FROM tasks WHERE id = ?', (task_id,)).fetchone()
    if not row:
        conn.close()
        return "Not found", 404
    new = 'done' if row['status'] != 'done' else 'todo'
    conn.execute('UPDATE tasks SET status = ? WHERE id = ?', (new, task_id))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
