import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def generate_sql_query(natural_language_query):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"Convert the following natural language query to SQL:\n{natural_language_query}\n\nSQL query:",
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.7,
    )
    return response.choices[0].text.strip()

def explain_query_results(sql_query, query_results):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"Explain the results of the following SQL query in plain English:\nQuery: {sql_query}\nResults: {query_results}\n\nExplanation:",
        max_tokens=200,
        n=1,
        stop=None,
        temperature=0.7,
    )
    return response.choices[0].text.strip()