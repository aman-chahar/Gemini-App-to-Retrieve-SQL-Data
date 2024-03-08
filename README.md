# Gemini-App-to-Retrieve-SQL-Data
Gemini App to Retrieve SQL Data using prompts

Streamlit web APP: https://gemini-app-to-retrieve-sql-data-i26k8wnp3qtdcgtzszxh7y.streamlit.app/

1. **Environment Setup**: You start by importing necessary libraries such as `dotenv` for managing environment variables, `streamlit` for creating web applications, `os` for interacting with the operating system, and `sqlite3` for working with SQLite databases.

2. **Google Generative AI Configuration**: You load the Google Generative AI API key from the environment variables using `dotenv` and configure it for use with the `google.generativeai` module.

3. **Functions**:
    - `get_gemini_response`: This function takes a question and a prompt as input, utilizes the Generative AI model (`gemini-pro`) to generate a response based on the question and prompt, and returns the generated response.
    - `read_sql_query`: This function executes an SQL query on a specified database and returns the result rows. It connects to the database using `sqlite3`, executes the query, fetches the rows, and then closes the connection. Additionally, it prints the fetched rows.

4. **Prompt Definition**: You define a prompt, which is a multi-line string providing instructions and examples for generating SQL queries from English questions.

5. **Streamlit App**:
    - You configure the Streamlit page title and header.
    - You create a text input field (`question`) for users to input their questions.
    - A button (`submit`) is provided to submit the question.
    - Upon clicking the submit button, the `get_gemini_response` function is called to generate a SQL query based on the user's question and the predefined prompt.
    - The generated SQL query is then executed using the `read_sql_query` function, and the result is displayed as a subheader in the Streamlit app.

6. **Displaying Results**: You display the response from the Generative AI model and the retrieved SQL query result rows in the Streamlit app.

This code creates a Streamlit web application that allows users to input English questions related to the SQL database schema and retrieves SQL queries and results dynamically using Google Generative AI and SQLite respectively.
