from sqlalchemy.orm import Session
from . import models, openai_helper

def process_query(db: Session, user_id: int, natural_language_query: str):
    # Generate SQL query
    sql_query = openai_helper.generate_sql_query(natural_language_query)
    
    # Execute SQL query (Note: This is a simplified example. In a real-world scenario,
    # you'd need to implement proper security measures to prevent SQL injection)
    result = db.execute(sql_query).fetchall()
    
    # Generate explanation
    explanation = openai_helper.explain_query_results(sql_query, result)
    
    # Log query history
    query_history = models.QueryHistory(
        user_id=user_id,
        natural_language_query=natural_language_query,
        generated_sql_query=sql_query,
        execution_result=str(result),
        explanation=explanation
    )
    db.add(query_history)
    db.commit()
    
    return {
        "sql_query": sql_query,
        "result": result,
        "explanation": explanation
    }