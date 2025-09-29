import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import sqlite3

import sqlite3




conn = sqlite3.connect("../db/lesson.db")
cursor = conn.cursor()



query = """
    SELECT e.last_name, SUM(p.price * l.quantity) AS revenue
FROM employees e
JOIN orders o ON e.employee_id = o.employee_id
JOIN line_items l ON o.order_id = l.order_id
JOIN products p ON l.product_id = p.product_id
GROUP BY e.employee_id;

"""

employee_results = pd.read_sql(query, conn)

conn.close()

plt.figure(figsize=(12,6))
sns.barplot(
    x="last_name",
    y="revenue",
    data=employee_results,
    hue="last_name",
    palette="viridis"


)

plt.title("Revenue by Employee", fontsize=16)
plt.xlabel("Employee Last Name", fontsize=12)
plt.ylabel("Revenue", fontsize=12)
plt.xticks(rotation=54)
plt.show()


