import sqlite3

# Task 1
def task1(cursor):
    query = """
    SELECT p.product_name,
           SUM(li.quantity * p.price) AS total_sales
    FROM line_items li
    JOIN products p ON li.product_id = p.product_id
    GROUP BY p.product_name
    ORDER BY total_sales DESC
    LIMIT 5;
    """
    cursor.execute(query)
    results = cursor.fetchall()

    print("Task 1: Total sales (top 5 products)")
    print("product_name | total_sales")
    print("--------------------------")
    for row in results:
        print(f"{row[0]} | {row[1]:.2f}")
    print()


# Task 2
def task2(cursor):
    query = """
    SELECT p.product_name,
           AVG(sub.total_sales) AS avg_total_sales
    FROM (
        SELECT li.product_id,
               SUM(li.quantity * p.price) AS total_sales
        FROM line_items li
        JOIN products p ON li.product_id = p.product_id
        GROUP BY li.product_id        
    ) AS sub
    JOIN products p ON sub.product_id = p.product_id
    GROUP BY p.product_name;
    """
    cursor.execute(query)
    results = cursor.fetchall()

    print("Task 2: Average sales per product")
    print("product_name | avg_total_sales")
    print("--------------------------")
    for row in results:
        print(f"{row[0]} | {row[1]:.2f}")
    print()

#Task 3
def task3(cursor):
        cursor.execute(
            """
                SELECT product_id
                FROM products
                ORDER BY price ASC
                LIMIT 5;
            """
        )
        product_ids = [row[0] for row in cursor.fetchall()]

        for pid in product_ids:
            cursor.execute(
                """
                    SELECT li.line_item_id, li.quantity, p.product_name
                    FROM line_items li
                    JOIN products p ON li.product_id = p.product_id
                    ORDER BY li.line_item_id DESC
                    LIMIT 5;
                """
            )
            results = cursor.fetchall()

        print("Task 3: Inserted order simulation")
        print("line_item_id | quantity | product_name")
        print("--------------------------")
        for row in results:
            print(f"{row[0]} | {row[1]} | {row[2]}")
        print()  

def task4(cursor):
    query = """
        SELECT e.employee_id,
               e.first_name,
               e.last_name,
               COUNT(o.order_id) AS order_count
        FROM employees e
        JOIN orders o ON e.employee_id = o.employee_id
        GROUP BY e.employee_id, e.first_name, e.last_name
        HAVING COUNT(o.order_id) > 5;
    """ 
    cursor.execute(query) 
    results = cursor.fetchall()   

    print("Task 4: Employees with more than 5 orders")
    print("employee_id | first_name | last_name | order_count")
    print("---------------------------------------------------")
    for row in results:
        print(f"{row[0]} | {row[1]} | {row[2]} | {row[3]}")
    print()
       


def main():
    conn = sqlite3.connect("../db/lesson.db")
    cursor = conn.cursor()

    task1(cursor)
    task2(cursor)
    task3(cursor)
    task4(cursor)
    conn.commit()

    conn.close()


if __name__ == "__main__":
    main()

