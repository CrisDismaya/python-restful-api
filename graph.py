import matplotlib
matplotlib.use('Agg')  # Specify non-interactive backend
import matplotlib.pyplot as plt
import mplcursors

from flask import Flask, render_template
import io
import base64
from config.connector import PostgreSQLConnector

app = Flask(__name__)

@app.route('/graph')
def graph():
    connector = PostgreSQLConnector()
    connector.connect()

    stmt = """
        SELECT 
            sub.sports, SUM(sub.price) AS price
        FROM (
            SELECT 
                TRIM(REPLACE(
                    CASE
                        WHEN sports LIKE '%Apparel%' THEN 'Apparel'
                        WHEN sports LIKE '%Sleeve%' THEN 'Apparel'
                        WHEN sports LIKE '%Shirt%' THEN 'Apparel'
                        WHEN sports LIKE '%Short%' THEN 'Apparel'
                        WHEN sports LIKE '%Lacrosse%' THEN 'Apparel'
                    ELSE sports END
                , 'DSG ', '')) sports, price
            FROM public.sales
        ) sub
        GROUP BY sub.sports
        ORDER BY sub.sports
    """
    connector.execute_query(stmt)
    result = connector.cursor.fetchall()

    # Get the column names from the cursor description
    columns = [desc[0] for desc in connector.cursor.description]

    # Create a list of dictionaries where each dictionary represents a row
    result_as_dict = [dict(zip(columns, row)) for row in result]

    # Extract keys and values from the result
    keys = [row['sports'] for row in result_as_dict]
    values = [float("{:.2f}".format(row['price'])) for row in result_as_dict]

    # Plotting using Matplotlib
    with app.app_context():
        plt.figure(figsize=(10, 6)) 
        bars = plt.bar(keys, values, width=0.5)  # Convert values to float for plotting
        plt.xlabel('Sports')
        plt.ylabel('Price')
        plt.xticks(rotation=45)
        plt.tight_layout()

        # for bar, val in zip(bars, values):
        #     plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), val, ha='center', va='bottom')
        
        # mplcursors.cursor(bars, hover=True).connect("add", lambda sel: sel.annotation.set_text(f"{sel.artist.get_height():.2f}"))

        # Save the plot to a BytesIO object
        img_buf = io.BytesIO()
        plt.savefig(img_buf, format='png')
        img_buf.seek(0)
        plt.close()

        # Encode the image as base64 for displaying in HTML
        img_data = base64.b64encode(img_buf.read()).decode('utf-8')

    # Close the database connection
    connector.connection.close()

    # Return HTML page with the embedded image
    return render_template('graph_page.html', graph_data=img_data)

if __name__ == '__main__':
    app.run(port=7000, debug=True)
