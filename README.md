# LIVE DEMO
You can access the live demo here https://cipjuscodin-geminisql.streamlit.app/    
(Working deployment last checked on 14-05-2024)

# Installation Instructions
1. Begin by installing all the necessary libraries with ```pip install -r requirements.txt```
2. Create a file named ```.env``` in the cloned repository and  type ```GOOGLE_API_KEY="Your api key"```
3. Once the installation is complete, you can locally execute it by entering ```streamlit run app.py```

# Introduction
GeminiSQL is a revolutionary web application leveraging AI technology to simplify SQL querying through natural language input. Designed with usability and efficiency in mind, GeminiSQL provides users with a seamless experience for executing SQL queries effortlessly. Whether you're a seasoned SQL developer or a newcomer to database querying, GeminiSQL offers a user-friendly interface powered by Google's Gemini Pro model, making database interaction intuitive and accessible.

# Features

+ Natural Language SQL Querying: GeminiSQL allows users to input SQL queries in natural language, abstracting away the complexities of traditional query syntax. With the power of Google's Gemini Pro model, users can simply type or speak their queries, enabling rapid data retrieval without the need for extensive SQL knowledge.
+ Streamlit Powered Backend: Developed using Python and Streamlit, GeminiSQL's backend ensures smooth operation and rapid deployment. Streamlit's intuitive framework accelerates development, facilitating seamless integration of AI-powered natural language processing into the application.
+ Efficient Database Management with SQLite: GeminiSQL utilizes SQLite for its database backend, offering simplicity and compatibility for storing and retrieving data. A single table named STUDENT is designed to store student records, featuring columns for name, class, section, and marks, ensuring efficient data management for various use cases.
# Functionality Overview
GeminiSQL caters to both novices and experts in SQL querying, offering a user-friendly interface and powerful backend capabilities.

1. Intuitive User Interface:
With GeminiSQL's intuitive interface, users can effortlessly input natural language queries and receive SQL responses in real-time. The interface features input fields for query submission and dynamic content generation, ensuring a seamless interaction experience.
2. Efficient Query Processing:
Upon receiving natural language queries, GeminiSQL processes them efficiently using Google's Gemini Pro model, generating corresponding SQL queries promptly. Users can retrieve data without the need for manual SQL syntax, streamlining the querying process for enhanced productivity.
3. Fast Response Times:
GeminiSQL prioritizes fast response times, ensuring users receive query results promptly. By harnessing the power of AI-driven natural language processing and Streamlit's rapid development framework, the application delivers a seamless user experience with minimal processing time.

# Architecture
+ Frontend: Built using Streamlit to provide a responsive and interactive user interface.
+ Backend: Utilizes SQLite for database management and Google's Gemini Pro model for natural language processing.
+ Integration: Seamlessly integrates natural language processing with SQL querying, providing an intuitive user experience.

# Database Schema
The application uses a single table named STUDENT to store student records:

Columns:

NAME - VARCHAR(25)

CLASS - VARCHAR(25)

SECTION - VARCHAR(25)

MARKS - INT

# Troubleshooting
1. Database Initialization Issues:
Ensure that sqlite.py is executed successfully to initialize the database.
2. API Key Errors:
Verify that the Google API key is correctly set in the .env file.
3. Dependency Problems:
Run pip install -r requirements.txt to install all required dependencies.
