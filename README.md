# ✈️ TravelGenie AI — A Multi-Agent Travel Planner with LangGraph

An AI-powered travel planner that transforms natural-language trip requests into personalized travel plans with flight suggestions, hotel recommendations, and day-by-day itineraries.

Built using **LangGraph, LangChain, Groq, FastAPI, and PostgreSQL**, TravelGenie AI demonstrates how multiple specialized AI agents can collaborate to solve a real-world planning problem.

## 🌍 Why TravelGenie AI?

Planning a trip often involves switching between multiple websites, comparing flights, researching hotels, and organizing daily activities.

TravelGenie AI simplifies this process by bringing these tasks together through a coordinated multi-agent workflow.

The application consists of four specialized agents:

- ✈️ **Flight Agent:** Retrieves flight-related information using AviationStack.
- 🏨 **Hotel Research Agent:** Searches for hotel recommendations using Tavily.
- 🧠 **Itinerary Agent:** Generates a practical, day-by-day travel itinerary.
- 📝 **Final Response Agent:** Combines the results into a structured travel plan.

These agents work together through a LangGraph workflow to deliver a unified response.

## ✨ Features

- ✈️ Flight research using AviationStack API.
- 🏨 Hotel research and recommendations using Tavily Search.
- 🧠 Multi-agent orchestration using LangGraph.
- 📝 AI-generated day-by-day travel itineraries.
- 💬 Natural-language travel requests.
- 🌐 FastAPI backend with a web-based frontend.
- 💾 Conversation state persistence using PostgreSQL and LangGraph checkpoints.
- ⚡ LLM-powered responses using Groq.
- 🔄 Context-aware conversations using thread-based state management.

## 🛠️ Tech Stack

| Category | Technologies |
|---|---|
| Language | Python 3.11 |
| Backend | FastAPI |
| Frontend | HTML, CSS, JavaScript, Jinja2 |
| Agent Orchestration | LangGraph |
| LLM Framework | LangChain |
| Language Model | Groq |
| Database | PostgreSQL |
| Flight Research | AviationStack API |
| Web Research | Tavily API |
| Deployment | Render |

## 📁 Project Structure

```text
TravelGenie-AI/
│
├── app.py                  # FastAPI application entry point
├── backend.py              # LangGraph multi-agent workflow
├── requirements.txt        # Python dependencies
├── Dockerfile              # Docker configuration
│
├── static/                 # Frontend static assets
├── templates/              # HTML templates
│
└── tools/
    ├── flight_tool.py      # Flight search integration
    └── tavily_tool.py      # Hotel and web research integration
```

## ⚙️ Prerequisites

Before running the project locally, ensure you have:

- Python 3.11
- PostgreSQL database
- Git
- API keys for:
  - [Groq](https://console.groq.com/)
  - [Tavily](https://tavily.com/)
  - [AviationStack](https://aviationstack.com/)

## 🔑 Environment Variables

Create a `.env` file in the project root and configure the following variables:

```env
DATABASE_URL=postgresql://user:password@localhost:5432/travel_db

GROQ_API_KEY=your_groq_api_key
AVIATIONSTACK_API_KEY=your_aviationstack_api_key
TAVILY_API_KEY=your_tavily_api_key

DEFAULT_ORIGIN_IATA=DEL
```

**Note:** Replace the placeholder values with your actual credentials. Never commit your `.env` file or expose API keys publicly.

For a hosted PostgreSQL database, use the connection string provided by your database provider.

## 🚀 Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/bharatch02/TravelGenie-AI---A-Multi-Agent-Travel-Planner.git

cd TravelGenie-AI---A-Multi-Agent-Travel-Planner
```

### 2. Create a virtual environment

**Windows (PowerShell):**

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

**macOS / Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create your `.env` file using the variables described above.

Ensure your PostgreSQL database is accessible before starting the application.

### 5. Start the application

```bash
python app.py
```

Open your browser and navigate to:

**http://127.0.0.1:8000/**

## 🔌 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Serves the web application |
| GET | `/health` | Health check |
| POST | `/api/travel` | Submits a travel request |

### Example API Request

```bash
curl -X POST http://127.0.0.1:8000/api/travel \
  -H "Content-Type: application/json" \
  -d '{"message":"Plan a 3-day trip to Tokyo with a budget of $1200"}'
```

## 🔄 How the Workflow Works

TravelGenie AI follows a sequential multi-agent architecture:

1. **User Request:** The user submits a natural-language travel request.
2. **Flight Agent:** Retrieves relevant flight information.
3. **Hotel Research Agent:** Searches for accommodation options.
4. **Itinerary Agent:** Generates a practical itinerary using the available research.
5. **Final Response Agent:** Formats the information into a structured travel plan.
6. **State Persistence:** LangGraph checkpoints conversation state in PostgreSQL, allowing conversations to maintain context through thread IDs.

## ☁️ Deployment

TravelGenie AI can be deployed on Render.

The deployment requires:

- A Render Web Service connected to the GitHub repository.
- A PostgreSQL database.
- Required API keys configured as environment variables in the Render dashboard.

Configure the environment variables in Render rather than committing credentials to the repository.

The web service should start using the application's configured Uvicorn startup command and listen on the port provided by the hosting platform.

## ⚠️ Important Disclaimer

TravelGenie AI is an AI-powered travel planning assistant.

- Flight information depends on the data available through AviationStack.
- Hotel suggestions are generated using web research.
- Prices, availability, and travel details may not be live-verified.
- Always verify flight schedules, hotel availability, and prices with the respective providers before booking.

The application provides travel suggestions and planning assistance; it does not make confirmed bookings.

## 🤝 Contributing

Contributions are welcome!

If you'd like to improve the application, add new features, or fix issues:

1. Fork the repository.
2. Create a feature branch.
3. Make your changes.
4. Commit your changes.
5. Open a pull request.

## 🙌 Acknowledgments

Built with modern AI frameworks, LLMs, and travel research APIs.

This project explores the practical application of multi-agent systems, LLM orchestration, API integrations, and persistent conversational state in a real-world travel planning application.

---

**If you find this project useful, consider giving it a ⭐ on GitHub!**