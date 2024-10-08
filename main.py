from sqlalchemy.orm import Session
from app import models, database, user_management, query_processor

# Create tables
models.Base.metadata.create_all(bind=database.engine)

def main():
    db = next(database.get_db())
    
    # Example usage
    username = "example_user"
    email = "user@example.com"
    password = "securepassword123"
    
    # Create a new user
    user = user_management.create_user(db, username, email, password)
    print(f"Created user: {user.username}")
    
    # Authenticate user
    authenticated_user = user_management.authenticate_user(db, username, password)
    if authenticated_user:
        print(f"Authenticated user: {authenticated_user.username}")
        
        # Process a query
        natural_language_query = "Show me all sales from last month"
        result = query_processor.process_query(db, authenticated_user.user_id, natural_language_query)
        print(f"SQL Query: {result['sql_query']}")
        print(f"Result: {result['result']}")
        print(f"Explanation: {result['explanation']}")
        
        # Get user's query history
        history = user_management.get_user_query_history(db, authenticated_user.user_id)
        print(f"Query history: {history}")
    else:
        print("Authentication failed")

if __name__ == "__main__":
    main()