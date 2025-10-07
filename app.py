from flask import Flask, request, jsonify, render_template
import sqlite3

app = Flask(__name__)

# ---------- Home ----------
@app.route('/')
def index():
    return render_template('hello.html')

# ---------- Add a new note ----------
@app.route('/add_note', methods=['POST'])
def add_note():
    data = request.get_json()
    note = data.get('content')

    if not note:
        return jsonify({'error': 'Note cannot be empty'}), 400

    conn = sqlite3.connect('noteapp.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO notes (content) VALUES (?)', (note,))
    conn.commit()
    conn.close()

    return jsonify({'message': 'Note added successfully!'})

# ---------- Get all notes ----------
@app.route('/get_notes', methods=['GET'])
def get_notes():
    conn = sqlite3.connect('noteapp.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id, content FROM notes')
    notes = [{'id': row[0], 'content': row[1]} for row in cursor.fetchall()]
    conn.close()

    return jsonify(notes)

# ---------- Delete a note ----------
@app.route('/delete_note/<int:note_id>', methods=['DELETE'])
def delete_note(note_id):
    conn = sqlite3.connect('noteapp.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM notes WHERE id = ?', (note_id,))
    conn.commit()
    conn.close()

    return jsonify({'message': f'Note {note_id} deleted successfully'})

# ---------- Run the app ----------
if __name__ == '__main__':
    app.run(debug=True)
