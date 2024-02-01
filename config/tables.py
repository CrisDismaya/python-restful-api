# main.py
from config.connector import PostgreSQLConnector

def create_default_table():
    connector = PostgreSQLConnector()
    connector.connect()
    
    # Perform your database operations here
    try:
        # Execute the provided query
        create_topics_table = """
            CREATE TABLE IF NOT EXISTS public.chat_topics
            (
                id SERIAL PRIMARY KEY,
                user_id int,
                title text COLLATE pg_catalog."default",
                created_at timestamp with time zone DEFAULT CURRENT_TIMESTAMP,
                deleted_at timestamp with time zone
            );
        """
        connector.execute_query(create_topics_table)

        create_messages_table = """
            CREATE TABLE IF NOT EXISTS public.chat_messages
            (
                id SERIAL PRIMARY KEY,
                topic_id int,
                message text COLLATE pg_catalog."default",
                response text COLLATE pg_catalog."default",
                created_at timestamp with time zone DEFAULT CURRENT_TIMESTAMP
            );
        """
        connector.execute_query(create_messages_table)

    except Exception as e:
        print(f"Error: {e}")

    finally:
        connector.disconnect()

if __name__ == "__main__":
    create_default_table()
