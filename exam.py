import sqlite3


def angling(db_file, *fishermen):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    query = '''SELECT p.place, f.catch, b.people FROM Fishing f
    JOIN Places p ON f.place_id = p.id
    JOIN Brownie b ON f.brownie_id = b.id
    WHERE f.fishman IN ({}) AND f.catch > 50'''.format(', '.join(['?'] * len(fishermen)))

    cursor.execute(query, fishermen)
    results = cursor.fetchall()

    conn.close()

    unique_results = list(set(results))
    unique_results.sort(key=lambda x: (-x[1], x[0], x[2]))
    return unique_results
