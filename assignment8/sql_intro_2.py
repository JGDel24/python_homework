import sqlite3
import pandas as pd

def main():
    conn = sqlite3.connect("../db/lesson.db")

    query = """
        SELECT li.line_item_id, li.quantity, li.product_id, p.product_name, p.price
        FROM line_items li
        JOIN products p ON li.product_id = p.product_id;
    """

    df = pd.read_sql_query(query, conn)
    print(df.head())

    df['total'] = df['quantity'] * df['price']
    print(df.head())

    summary = df.groupby('product_id').agg({
        'line_item_id': 'count',
        'total': 'sum',
        'product_name': 'first'
    }).reset_index()

    print(summary.head())

    summary = summary.sort_values(by='product_name')

    summary.to_csv("order_summary.csv", index=False)

    conn.close()

if __name__ == "__main__":
    main()