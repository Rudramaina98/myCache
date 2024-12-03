from flask import Flask
import mysql.connector

app = Flask(__name__)

# MySQL Configuration
mysql_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Login@123',
    'database': 'Childcare_DB'
}

# Establishing a MySQL connection
conn = mysql.connector.connect(**mysql_config)
cursor = conn.cursor()

# Route to test the database connection
@app.route('/')
def test_db_connection():
    try:
        cursor.execute("SELECT 1")
        return "Connected to the database successfully!"
    except mysql.connector.Error as e:
        return f"Failed to connect to the database: {e}"

if __name__ == '__main__':
    app.run(debug=True)
