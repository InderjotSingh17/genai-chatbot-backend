from app.database import get_connection
def conversation_exists(conversation_id: int) :
    conn=get_connection()
    cur=conn.cursor()
    cur.execute(
        """
        SELECT EXISTS(
            SELECT 1
            FROM conversations
            WHERE id = %s
        )
        """,
        (conversation_id,)
    )
    exists=cur.fetchone()[0];
    cur.close()
    conn.close()
    return exists
def create_conversation(user_id: int):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        """
        INSERT INTO conversations (user_id)
        VALUES (%s)
        RETURNING id
        """,
        (user_id,)
    )
    conversation_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return conversation_id
def get_history(conversation_id: int):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        """
        SELECT role, content
        FROM messages
        WHERE conversation_id = %s
        ORDER BY id ASC
        """,
        (conversation_id,)
    )
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return [
        {
            "role": row[0],
            "content": row[1]
        }
        for row in rows
    ]
def add_to_history(
    conversation_id: int,
    role: str,
    content: str
):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        """
        INSERT INTO messages
        (conversation_id, role, content)
        VALUES (%s, %s, %s)
        """,
        (conversation_id, role, content)
    )
    conn.commit()
    cur.close()
    conn.close()

def conversation_belongs_to_user(
    conversation_id: int,
    user_id: int
):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        SELECT EXISTS(
            SELECT 1
            FROM conversations
            WHERE id = %s
            AND user_id = %s
        )
        """,
        (conversation_id, user_id)
    )

    belongs = cur.fetchone()[0]

    cur.close()
    conn.close()

    return belongs