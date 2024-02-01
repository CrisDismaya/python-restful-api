# main.py
from flask import Flask, jsonify, request
from config.connector import PostgreSQLConnector

app = Flask(__name__)

# Create a route for your API endpoint
@app.route('/api/getTopic', methods=['GET'])
def get_topics():
    try:
        # Your existing database code
        connector = PostgreSQLConnector()
        connector.connect()

        data = request.get_json()
        user_id = data.get('user_id')

        topics_sql = "SELECT id, user_id, title FROM chat_topics WHERE deleted_at IS NULL AND user_id = %s"
        connector.execute_query(topics_sql, (user_id,))
        result = connector.cursor.fetchall()

        # Transform the result into a list of dictionaries
        topic_fromatted = [
            {
                "id": row[0], 
                "user_id": row[1], 
                "title": row[2]
            } for row in result
        ]
        return jsonify({"result": topic_fromatted})

    except Exception as e:
        return jsonify({"error": str(e)})
    
    finally:
        connector.disconnect()


@app.route('/api/getMessageFromTopic', methods=['GET'])
def get_message():
    try:
        connector = PostgreSQLConnector()
        connector.connect()

        data = request.get_json()
        topic_id = data.get('topic_id')

        messages_sql = """
            SELECT cmsg.id, cmsg.topic_id, cmsg.message, cmsg.response 
            FROM chat_messages cmsg
            LEFT JOIN chat_topics ctps ON cmsg.topic_id = ctps.id
            WHERE ctps.deleted_at IS NULL AND cmsg.topic_id = %s
        """
        connector.execute_query(messages_sql, (topic_id,))
        result = connector.cursor.fetchall()

        # Transform the result into a list of dictionaries
        message_formatted = [
            {
                "id": row[0],
                "topic_id": row[1],
                "message": row[2],
                "response": row[3]
            } for row in result
        ]
        return jsonify({"result": message_formatted})

    except Exception as e:
        return jsonify({"error": str(e)})

    finally:
        connector.disconnect()


@app.route('/api/addMessages', methods=['POST'])
def add_messges():
    try:
        # Your existing database code
        connector = PostgreSQLConnector()
        connector.connect()

        # Get data from the request
        data = request.get_json()
        topic_id = data.get('topic_id')
        user_id = data.get('user_id')
        item = data.get('message')

        # topic_id if greater than 0 it means have selected topic else none
        # 0:create a new topic / !0:continue the conversation in previous topic
        if topic_id == 0:
            # Insert data into the database
            topic_sql = "INSERT INTO chat_topics (user_id, title) VALUES (%s, %s) RETURNING id"
            connector.execute_query(topic_sql, (user_id, item))
            last_inserted_id = connector.cursor.fetchone()[0]
        else:
            last_inserted_id = topic_id

        message_sql = "INSERT INTO chat_messages (topic_id, message) VALUES (%s, %s)"
        connector.execute_query(message_sql, (last_inserted_id, item))

        return jsonify({"message": "Data added successfully"})

    except Exception as e:
        return jsonify({"error": str(e)})

    finally:
        connector.disconnect()


@app.route('/api/deleteMessage', methods=['DELETE'])
def delete_message():
    try:
        # Your existing database code
        connector = PostgreSQLConnector()
        connector.connect()

        # Get data from the request
        data = request.get_json()
        topic_id = data.get('topic_id')
        user_id = data.get('user_id')

        if topic_id == 0:
            delete_all = "UPDATE chat_topics SET deleted_at = NOW() WHERE user_id = %s"
            connector.execute_query(delete_all, (user_id,))

        else:
            delete_topic_sql = "UPDATE chat_topics SET deleted_at = NOW() WHERE id = %s"
            connector.execute_query(delete_topic_sql, (topic_id,))

        return jsonify({'result': topic_id})
    
    except Exception as e:
        return jsonify({'error': str(e)})

    finally:
        connector.disconnect()


@app.route('/api/updateTopic', methods=['PUT'])
def update_topic():
    try:
        # Your existing database code
        connector = PostgreSQLConnector()
        connector.connect()

        # Get data from the request
        data = request.get_json()
        topic_id = data.get('topic_id')
        topic_title = data.get('new_topic')

        update_topic_sql = "UPDATE chat_topics SET title = %s WHERE id = %s"
        connector.execute_query(update_topic_sql, (topic_title, topic_id))

        return jsonify({'result': data})
    
    except Exception as e:
        return jsonify({'error': str(e)})

    finally:
        connector.disconnect()

if __name__ == "__main__":
    app.run(port=7000, debug=True)
