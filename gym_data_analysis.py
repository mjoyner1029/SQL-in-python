import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('gym_database.db')
cursor = conn.cursor()

def get_members_in_age_range(start_age, end_age):
    """
    Retrieve details of members whose ages fall between start_age and end_age.
    
    Parameters:
    start_age (int): The minimum age for the filter.
    end_age (int): The maximum age for the filter.
    
    Returns:
    List of tuples containing member details within the specified age range.
    """
    try:
        # SQL query using BETWEEN clause
        query = '''
            SELECT * FROM Members
            WHERE age BETWEEN ? AND ?
        '''
        cursor.execute(query, (start_age, end_age))
        members = cursor.fetchall()
        
        # Display the results
        if members:
            print(f"Members aged between {start_age} and {end_age}:")
            for member in members:
                print(f"ID: {member[0]}, Name: {member[1]}, Age: {member[2]}")
        else:
            print(f"No members found between the ages of {start_age} and {end_age}.")
            
        return members
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

if __name__ == "__main__":
    # Example usage
    start_age = 25
    end_age = 30
    get_members_in_age_range(start_age, end_age)

# Close the connection when done
conn.close()
