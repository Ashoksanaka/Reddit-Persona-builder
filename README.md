# Reddit Persona Builder 🧠

This project was built as part of an assignment for the **AI/LLM Engineer Intern** position at **BeyondChats**. It scrapes a Reddit user’s public posts and comments, then analyzes them using a large language model (LLM) to generate a **user persona**, along with citations from the source content.

---

## 🧩 Features

- Takes a Reddit username as input (e.g., `kojied`)
- Fetches their latest Reddit **posts** and **comments**
- Uses a free **LLM via Hugging Face** (`zephyr-7b-beta`) to analyze:
  - Personality
  - Motivations
  - Behaviors & Habits
  - Frustrations
  - Goals
- Outputs the analysis in a structured **text file**
- **Cites** the source post or comment for each insight

---

## 🚀 Technologies Used

- **Python 3**
- **PRAW** – Reddit API wrapper
- **Hugging Face Chat API** – for Zephyr LLM
- **Requests**, **dotenv**, **JSON** – for API communication and file handling

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Ashoksanaka/reddit-persona-builder.git
cd reddit-persona-builder
```

### 2. Create a Virtual Environment and Activate It

```bash
python3 -m venv persona_venv
source persona_venv/bin/activate  # On Windows: persona_venv\Scripts\activate
```

### 3. Install the Requirements

```bash
pip install -r requirements.txt
```

### 4. Configure the `.env` File

Create a `.env` file in the root directory and add your credentials:

```env
REDDIT_CLIENT_ID=your_client_id
REDDIT_CLIENT_SECRET=your_client_secret
REDDIT_USER_AGENT=RedditPersonaBuilder/0.1 by your_reddit_username
REDDIT_USERNAME=your_reddit_username
REDDIT_PASSWORD=your_reddit_password

HF_API_KEY=your_huggingface_api_token
```

> 🔐 Your Reddit credentials are needed for authenticated scraping using the Reddit API.  
> 🔑 Your Hugging Face token is used to access Zephyr-7B through the free Chat API.

---

## 🧪 How to Run the Script

```bash
python main.py
```

The script will:
- Scrape posts/comments of users
- Generate their persona
- Save both the raw data and the persona output

---

## 👥 Sample Users Tested (as per assignment)

- [`kojied`](https://www.reddit.com/user/kojied/)
- [`Hungry-Move-6603`](https://www.reddit.com/user/Hungry-Move-6603/)

---

## 📁 Output Structure

All outputs are saved in the `/output` directory:

```bash
output/
├── kojied_data.json             # Raw scraped Reddit content
├── kojied_persona.txt           # LLM-generated persona with citations
├── Hungry-Move-6603_data.json
├── Hungry-Move-6603_persona.txt
```

Each `.txt` file includes:
- Basic Info (Age, Occupation, Archetype, etc.)
- MBTI-style Personality Traits
- Motivations
- Behaviors & Habits
- Frustrations
- Goals
- Citations to each comment or post (e.g., "See POST #3")

---

## 📏 Coding Standards

- Written in **Python 3.10+**
- Follows **PEP-8 guidelines**
- Modular structure:
  - `scraper.py` – Reddit data collection
  - `persona_generator.py` – LLM analysis and formatting
  - `main.py` – Orchestration and file output

---

## 📝 Notes

- All credentials are kept in `.env` (not pushed to GitHub).
- Output is generated using the **free Hugging Face LLM** instead of OpenAI API to avoid paid usage.
