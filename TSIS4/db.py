import psycopg2

DB = {
    "dbname": "snake_db",
    "user": "postgres",
    "password": "Moonlight!",
    "host": "localhost",
    "port": 5432
}

def connect():
    return psycopg2.connect(**DB)

def get_player(username):
    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT id FROM players WHERE username=%s", (username,))
    row = cur.fetchone()

    if row:
        pid = row[0]
    else:
        cur.execute("INSERT INTO players(username) VALUES(%s) RETURNING id", (username,))
        pid = cur.fetchone()[0]
        conn.commit()

    cur.close()
    conn.close()
    return pid

def save_game(pid, score, level):
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO game_sessions(player_id, score, level_reached)
        VALUES(%s,%s,%s)
    """, (pid, score, level))

    conn.commit()
    cur.close()
    conn.close()

def leaderboard():
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
        SELECT p.username, g.score, g.level_reached, g.played_at
        FROM game_sessions g
        JOIN players p ON p.id=g.player_id
        ORDER BY g.score DESC
        LIMIT 10
    """)

    data = cur.fetchall()
    cur.close()
    conn.close()
    return data

def best_score(pid):
    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT MAX(score) FROM game_sessions WHERE player_id=%s", (pid,))
    res = cur.fetchone()[0]

    cur.close()
    conn.close()
    return res or 0