import sqlite3

def get_members_in_age_range(start_age, end_age):
    """
    Retrieve the details of members whose ages fall between start_age and end_age.
    """
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect('gym_database.db')
        cursor = conn.cursor()

        # SQL query to select members within the age range
        query = '''
        SELECT id, name, age
        FROM Members
        WHERE age BETWEEN ? AND ?
        '''
        cursor.execute(query, (start_age, end_age))
        members = cursor.fetchall()

        # Print the result
        if not members:
            print(f"No members found in the age range {start_age} to {end_age}.")
        else:
            print(f"Members between ages {start_age} and {end_age}:")
            for member in members:
                print(f"ID: {member[0]}, Name: {member[1]}, Age: {member[2]}")
        
        return members
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        conn.close()

def count_members_by_age_group():
    """
    Count the number of members in different age groups.
    """
    age_groups = {
        '20-24': 0,
        '25-29': 0,
        '30-34': 0,
        '35-39': 0,
        '40-44': 0,
        '45-49': 0,
        '50+': 0
    }

    try:
        # Connect to the SQLite database
        conn = sqlite3.connect('gym_database.db')
        cursor = conn.cursor()

        # Loop through each age group and count members
        for age_group in age_groups.keys():
            if age_group == '50+':
                query = '''
                SELECT COUNT(*)
                FROM Members
                WHERE age >= 50
                '''
            else:
                start_age, end_age = map(int, age_group.replace('+', '').split('-'))
                query = '''
                SELECT COUNT(*)
                FROM Members
                WHERE age BETWEEN ? AND ?
                '''
                cursor.execute(query, (start_age, end_age))
            
            count = cursor.fetchone()[0]
            age_groups[age_group] = count

        # Print the results
        print("Number of members by age group:")
        for age_group, count in age_groups.items():
            print(f"{age_group}: {count} members")
        
        return age_groups
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        conn.close()

# Example usage
if __name__ == "__main__":
    print("Fetching members in age range 25 to 35:")
    get_members_in_age_range(25, 35)
    
    print("\nCounting members by age group:")
    count_members_by_age_group()
