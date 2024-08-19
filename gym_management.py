import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('gym_database.db')
cursor = conn.cursor()

# Create tables (if they don't exist)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Members (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER NOT NULL
    )
''')
cursor.execute('''
    CREATE TABLE IF NOT EXISTS WorkoutSessions (
        session_id INTEGER PRIMARY KEY AUTOINCREMENT,
        member_id INTEGER,
        date TEXT NOT NULL,
        duration_minutes INTEGER NOT NULL,
        calories_burned INTEGER NOT NULL,
        FOREIGN KEY (member_id) REFERENCES Members (id)
    )
''')
conn.commit()

def add_member(id, name, age):
    """
    Add a new member to the Members table.
    
    Parameters:
    id (int): Member ID
    name (str): Member's name
    age (int): Member's age
    
    Returns:
    None
    """
    try:
        cursor.execute('INSERT INTO Members (id, name, age) VALUES (?, ?, ?)', (id, name, age))
        conn.commit()
        print("Member added successfully.")
    except sqlite3.IntegrityError:
        print("Error: Member ID already exists or invalid data.")
    except Exception as e:
        print(f"An error occurred: {e}")

def add_workout_session(member_id, date, duration_minutes, calories_burned):
    """
    Add a new workout session to the WorkoutSessions table.
    
    Parameters:
    member_id (int): ID of the member
    date (str): Date of the workout session
    duration_minutes (int): Duration of the workout in minutes
    calories_burned (int): Calories burned during the workout
    
    Returns:
    None
    """
    try:
        cursor.execute('INSERT INTO WorkoutSessions (member_id, date, duration_minutes, calories_burned) VALUES (?, ?, ?, ?)', 
                       (member_id, date, duration_minutes, calories_burned))
        conn.commit()
        print("Workout session added successfully.")
    except sqlite3.IntegrityError:
        print("Error: Invalid member ID or invalid data.")
    except Exception as e:
        print(f"An error occurred: {e}")

def update_member_age(member_id, new_age):
    """
    Update the age of an existing member.
    
    Parameters:
    member_id (int): ID of the member
    new_age (int): New age of the member
    
    Returns:
    None
    """
    try:
        cursor.execute('UPDATE Members SET age = ? WHERE id = ?', (new_age, member_id))
        if cursor.rowcount == 0:
            print("Error: Member ID does not exist.")
        else:
            conn.commit()
            print("Member age updated successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

def delete_workout_session(session_id):
    """
    Delete a workout session by session ID.
    
    Parameters:
    session_id (int): ID of the workout session
    
    Returns:
    None
    """
    try:
        cursor.execute('DELETE FROM WorkoutSessions WHERE session_id = ?', (session_id,))
        if cursor.rowcount == 0:
            print("Error: Session ID does not exist.")
        else:
            conn.commit()
            print("Workout session deleted successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Example usage
    add_member(1, "John Doe", 28)
    add_member(2, "Jane Smith", 32)
    add_workout_session(1, "2024-08-19", 60, 500)
    update_member_age(1, 29)
    delete_workout_session(1)

# Close the connection when done
conn.close()
