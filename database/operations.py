from database.config import get_connection


def insert_file(data):  #data is a tuple (name, size, type, modified_time, path)
    conn = get_connection()
    cursor = conn.cursor()  #cursor is a tool to write and execute SQL queries

    query = """
    INSERT IGNORE INTO files (name, size, type, modified_time, path)
    VALUES (%s, %s, %s, %s, %s)
    """
    #insert ignore skips the row if any error exist like duplicate entry.
    cursor.execute(query, data)
    conn.commit()      #commits making the changes permanent.

    cursor.close()    #closing the cursor and connection to free up resources.
    conn.close()      #closing the connection to the database.


def get_largest_files():
    conn = get_connection()  # opening a connection to the database
    cursor = conn.cursor()    #creating a tool to execute SQL queries

    cursor.execute("""
    SELECT name, size FROM files
    ORDER BY size DESC LIMIT 5
    """)

    results = cursor.fetchall()   #return tuple of all the rows in the result set.

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
    #This query groups the files by their type and counts how many files there are of each type. The result will be a list of tuples where each tuple contains a file type and the corresponding count.
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