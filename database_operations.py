import sqlite3
import os


def combine_sqlite_databases(source_db_path: str, target_db_path: str) -> None:
    """
    Combines data from a source SQLite database into a target SQLite database.

    Tables and their data from the source will be added to the target.
    Existing tables in the target with the same name will be appended to,
    with potential handling for primary key conflicts (using INSERT OR REPLACE).

    Args:
        source_db_path (str): The file path to the source SQLite database.
        target_db_path (str): The file path to the target SQLite database.

    Returns:
        None
    """
    source_conn = None
    target_conn = None
    try:
        source_conn = sqlite3.connect(source_db_path)
        source_cursor = source_conn.cursor()

        target_conn = sqlite3.connect(target_db_path)
        target_cursor = target_conn.cursor()

        # Get all table names from the source database
        source_cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = source_cursor.fetchall()

        for table_name_tuple in tables:
            table_name = table_name_tuple[0]
            print(f"Processing table: {table_name}")

            # Get schema for the table from the source
            source_cursor.execute(f"PRAGMA table_info({table_name});")
            columns_info = source_cursor.fetchall()
            column_names = [col[1] for col in columns_info]
            column_definitions = ", ".join(
                [f"{col[1]} {col[2]}" for col in columns_info]
            )

            # Create table in target if it doesn't exist
            create_table_sql = (
                f"CREATE TABLE IF NOT EXISTS {table_name} ({column_definitions});"
            )
            target_cursor.execute(create_table_sql)

            # Fetch data from source table
            source_cursor.execute(f"SELECT * FROM {table_name};")
            rows = source_cursor.fetchall()

            # Insert data into target table
            if rows:
                placeholders = ", ".join(["?" for _ in column_names])
                insert_sql = f"INSERT OR REPLACE INTO {table_name} ({', '.join(column_names)}) VALUES ({placeholders});"
                target_cursor.executemany(insert_sql, rows)
                target_conn.commit()
                print(
                    f"Inserted {len(rows)} rows into {table_name} in target database."
                )

    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
    finally:
        if source_conn:
            source_conn.close()
        if target_conn:
            target_conn.close()


if __name__ == "__main__":
    # Example usage and verification
    # Note: These files must exist for the code to run successfully.
    source_db = "weather_data.sqlite"
    target_db = "time_series.sqlite"

    # Check if files exist before running to avoid immediate error if this is just a test run
    if os.path.exists(source_db):
        combine_sqlite_databases(source_db, target_db)

        # Verify the combined database
        try:
            conn_combined = sqlite3.connect(target_db)
            cursor_combined = conn_combined.cursor()
            cursor_combined.execute("SELECT name from sqlite_master;")
            print("\nAll Tables in the DB:")
            for row in cursor_combined.fetchall():
                print(row)

            # Check for weather_data table specifically as in original code
            cursor_combined.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='weather_data';")
            if cursor_combined.fetchone():
                cursor_combined.execute("SELECT * FROM weather_data limit 1;")
                print("\nProducts in combined DB:")
                # get column names
                column_names = [description[0] for description in cursor_combined.description]
                print(column_names)
                for row in cursor_combined.fetchall():
                    print(row)
            else:
                 print("\n'weather_data' table not found in target database.")

            conn_combined.close()
        except sqlite3.Error as e:
            print(f"Verification error: {e}")
    else:
        print(f"Source database '{source_db}' not found. Skipping execution.")
