from database import get_connection

def get_top_products(limit: int = 10):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT product, COUNT(*) AS count
        FROM fct_product_mentions
        GROUP BY product
        ORDER BY count DESC
        LIMIT %s
    """, (limit,))
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return [{"product": row[0], "count": row[1]} for row in rows]

def get_channel_activity(channel_name: str):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT channel_name, COUNT(*) AS message_count,
               MIN(timestamp) AS first_post,
               MAX(timestamp) AS last_post
        FROM fct_messages
        WHERE channel_name = %s
        GROUP BY channel_name
    """, (channel_name,))
    row = cur.fetchone()
    cur.close()
    conn.close()
    if row:
        return {
            "channel_name": row[0],
            "message_count": row[1],
            "first_post": row[2],
            "last_post": row[3]
        }

def search_messages(query: str):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT message_id, content, channel_name, timestamp
        FROM fct_messages
        WHERE content ILIKE %s
        ORDER BY timestamp DESC
        LIMIT 50
    """, (f"%{query}%",))
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return [
        {
            "message_id": row[0],
            "content": row[1],
            "channel_name": row[2],
            "timestamp": row[3]
        }
        for row in rows
    ]
