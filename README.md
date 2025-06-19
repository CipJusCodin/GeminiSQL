# GeminiSQL

<div align="center">
  <img src="https://img.shields.io/badge/Python-3.7%2B-blue" alt="Python Version">
  <img src="https://img.shields.io/badge/Streamlit-1.0%2B-FF4B4B" alt="Streamlit">
  <img src="https://img.shields.io/badge/License-MIT-green" alt="License">
  <img src="https://img.shields.io/badge/Status-Active-success" alt="Status">
</div>

<p align="center">
  <strong>Convert natural language queries to SQL using Google's Gemini AI</strong>
</p>

## 📋 Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Demo](#demo)
- [Installation](#installation)
- [Usage](#usage)
- [Environment Variables](#environment-variables)
- [Database Schema](#database-schema)
- [How It Works](#how-it-works)
- [Contributing](#contributing)
- [License](#license)

## 1. Overview
GeminiSQL is a powerful tool that bridges the gap between natural language and SQL queries. Using Google's Gemini AI, it allows users to interact with databases using plain English, making database querying accessible to non-technical users.

## ✨ Features
- **Natural Language Processing**: Convert English questions to SQL queries
- **Real-time Results**: Instantly view query results in the Streamlit interface
- **SQLite Integration**: Works with SQLite databases out of the box
- **User-friendly Interface**: Simple, intuitive design for ease of use
- **Sample Database**: Comes with a pre-configured student database for testing

## 🎬 Demo
Try out the live demo: [GeminiSQL Demo](https://cipjuscodin-geminisql.streamlit.app/)

**Example queries:**
- "Show me all students in Data Science class"
- "What's the average marks of students in section A?"
- "List all students with marks above 80"
- "Count how many students are in each class"
- "Retrieve names of all students containing letter J"

## 🚀 Installation

### Prerequisites
- Python 3.7 or higher
- Google Gemini API key

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/CipJusCodin/GeminiSQL.git
   cd GeminiSQL
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the root directory with your Google Gemini API key:
   ```
   GOOGLE_API_KEY=your_api_key_here
   ```

## 🖥️ Usage
1. Run the Streamlit application:
   ```bash
   streamlit run app.py
   ```

2. Open your web browser and navigate to `http://localhost:8501`

3. Enter your question in natural language and click "Ask the question"

## Environment Variables
- `GOOGLE_API_KEY`: Your Google Gemini API key

## 📊 Database Schema
The application uses a SQLite database with a sample `STUDENT` table:

| Column  | Type      | Description            |
|---------|-----------|------------------------|
| NAME    | VARCHAR   | Student name           |
| CLASS   | VARCHAR   | Class name (e.g., Data Science, DEVOPS) |
| SECTION | VARCHAR   | Class section (A, B, C) |
| MARKS   | INTEGER   | Student's marks        |

## ⚙️ How It Works
1. **User Input**: The user submits a natural language question through the Streamlit interface
2. **AI Processing**: Google's Gemini AI model interprets the question and generates an appropriate SQL query
3. **Database Query**: The generated SQL query is executed against the SQLite database
4. **Result Display**: The query results are formatted and displayed in the Streamlit interface

## 🤝 Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

---

<div align="center">
  <p>Created with ❤️ by <a href="https://github.com/CipJusCodin">CipJusCodin</a></p>
</div>
