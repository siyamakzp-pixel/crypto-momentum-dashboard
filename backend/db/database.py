import os
import sqlite3


DEFAULT_DB_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "crypto.db")


def get_latest_momentum_scores(db_path=None):
    """Return the latest momentum score row for each coin."""
    database_path = db_path or os.environ.get("CRYPTO_DB_PATH") or DEFAULT_DB_PATH

    if not os.path.exists(database_path):
        return []

    connection = sqlite3.connect(database_path)
    connection.row_factory = sqlite3.Row

    try:
        query = """
        SELECT
            c.symbol,
            c.name,
            ms.score AS momentum_score
        FROM momentum_scores ms
        JOIN coins c ON c.id = ms.coin_id
        JOIN (
            SELECT coin_id, MAX(computed_at) AS latest_computed_at
            FROM momentum_scores
            GROUP BY coin_id
        ) latest
            ON latest.coin_id = ms.coin_id
           AND latest.latest_computed_at = ms.computed_at
        ORDER BY momentum_score DESC
        """
        rows = connection.execute(query).fetchall()
    except sqlite3.OperationalError:
        rows = []
    finally:
        connection.close()

    return [
        {
            "symbol": row["symbol"],
            "name": row["name"],
            "momentum_score": row["momentum_score"],
        }
        for row in rows
    ]
