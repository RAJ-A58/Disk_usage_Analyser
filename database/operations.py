from database.config import get_connection


def insert_file(data):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
    INSERT IGNORE INTO files (name, size, type, modified_time, path)
    VALUES (%s, %s, %s, %s, %s)
    """

    cursor.execute(query, data)
    conn.commit()

    cursor.close()
    conn.close()


def get_largest_files():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT name, size FROM files
    ORDER BY size DESC LIMIT 5
    """)

    results = cursor.fetchall()

    cursor.close()
    conn.close()

    return results 


def get_file_types():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT type, COUNT(*) FROM files
    GROUP BY type
    """)

    results = cursor.fetchall()

    cursor.close()
    conn.close()

    return results


def total_size():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT SUM(size) FROM files")
    result = cursor.fetchone()

    cursor.close()
    conn.close()

    return result[0] if result[0] else 0


def search_file(name):
    conn = get_connection()
    cursor = conn.cursor()

    query = "SELECT name, path FROM files WHERE name LIKE %s"
    cursor.execute(query, ('%' + name + '%',))

    results = cursor.fetchall()

    cursor.close()
    conn.close()

    return results


def clear_table():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM files")

    conn.commit()
    cursor.close()
    conn.close()