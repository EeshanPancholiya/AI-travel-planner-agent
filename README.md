# AgentXplore - AI Travel Planning Agent

An intelligent travel planning agent built with LangGraph and LangChain that provides comprehensive travel plans with real-time weather data, place recommendations, currency conversions, and expense calculations.

## Features

-  AI-Powered Planning**: Uses advanced LLMs (Groq/OpenAI) for intelligent travel recommendations
-  Real-time Weather**: Current weather and forecasts for destinations
-  Smart Location Search**: Google Places API integration for accurate place information
-  Currency Conversion**: Real-time exchange rates for international travel
-  Expense Calculation**: Detailed cost breakdowns and budget planning
-  ReAct Agent Pattern**: Reasoning and Action workflow for comprehensive planning
-  Modern UI**: Clean Streamlit interface for easy interaction

##  Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [API Keys Setup](#api-keys-setup)
- [Running the Application](#running-the-application)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)

## Prerequisites

Before you begin, ensure you have the following installed on your system:

- **Python 3.11+** (recommended)
- **pip** (Python package installer)
- **Git** (for cloning the repository)

##  Installation

### Step 1: Clone the Repository

```bash
git clone <your-repository-url>
cd AgentXplore
```

### Step 2: Create Virtual Environment (Recommended)

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate
```

### Step 3: Install Dependencies

```bash
# Upgrade pip
pip install --upgrade pip

# Install all required packages
pip install -r requirements.txt
```

##  API Keys Setup

To use all features of the travel agent, you'll need to obtain API keys from the following services:

### Required API Keys

1. **Groq API Key** (Recommended - Free tier available)
   - Visit: [https://console.groq.com/](https://console.groq.com/)
   - Sign up and obtain your API key
   - Starts with `gsk_`

2. **OpenWeatherMap API Key** (Free tier available)
   - Visit: [https://openweathermap.org/api](https://openweathermap.org/api)
   - Sign up and get your API key
   - Free tier includes 1000 calls/day

### Optional API Keys (For Enhanced Features)

3. **Google Places API Key**
   - Visit: [Google Cloud Console](https://console.cloud.google.com/)
   - Enable Places API and get your key
   - Provides detailed location information

4. **Exchange Rate API Key** (Free tier available)
   - Visit: [https://exchangerate-api.com/](https://exchangerate-api.com/)
   - Sign up and get your API key
   - Free tier includes 1500 requests/month

5. **Alpha Vantage API Key** (Free tier available)
   - Visit: [https://www.alphavantage.co/](https://www.alphavantage.co/)
   - Sign up and get your API key
   - Used for financial calculations

### Environment Configuration

Create a `.env` file in the project root directory:

```bash
# Create .env file
touch .env
```

Add your API keys to the `.env` file:

```env
# LLM API Keys (you need at least one)
GROQ_API_KEY=your_groq_api_key_here
OPENAI_API_KEY=your_openai_api_key_here

# Weather Information (Required for weather features)
OPENWEATHERMAP_API_KEY=your_openweathermap_api_key_here

# Google Places API (Optional - for enhanced location search)
GPLACES_API_KEY=your_google_places_api_key_here

# Currency Conversion (Optional - for currency features)
EXCHANGE_RATE_API_KEY=your_exchange_rate_api_key_here

# Alpha Vantage (Optional - for financial calculations)
ALPHAVANTAGE_API_KEY=your_alphavantage_api_key_here
```

**⚠️ Important**: Never commit your `.env` file to version control. It's already included in `.gitignore`.

##  Running the Application

The application consists of two components that need to be running simultaneously:

### Terminal 1: Backend (FastAPI Server)

```bash
# Navigate to project directory
cd AgentXplore

# Export environment variables and start backend
export GROQ_API_KEY=your_actual_groq_key && \
export OPENWEATHERMAP_API_KEY=your_actual_weather_key && \
export GPLACES_API_KEY=your_actual_places_key && \
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

You should see:
```
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
INFO:     Started reloader process
INFO:     Started server process
INFO:     Application startup complete.
```

### Terminal 2: Frontend (Streamlit UI)

Open a new terminal window:

```bash
# Navigate to project directory
cd AgentXplore

# Export environment variables and start frontend
export GROQ_API_KEY=your_actual_groq_key && \
export OPENWEATHERMAP_API_KEY=your_actual_weather_key && \
export GPLACES_API_KEY=your_actual_places_key && \
streamlit run streamlit_app.py --server.port 8501
```

You should see:
```
You can now view your Streamlit app in your browser.
Local URL: http://localhost:8501
Network URL: http://192.168.1.x:8501
```

## 🎯 Usage

### Accessing the Application

1. Open your web browser
2. Navigate to: `http://localhost:8501`
3. You'll see the "🌍 Travel Planner Agentic Application" interface

### Example Queries

Try asking the travel agent questions like:

- **"Plan a 3-day trip to Paris"**
- **"I want to visit Tokyo for 5 days with a budget of $2000"**
- **"Plan a romantic weekend in Rome"**
- **"What's the weather like in Bali this week?"**
- **"Plan a budget backpacking trip to Thailand"**
- **"I need a business trip itinerary for New York"**

### What You'll Get

The AI travel agent will provide:

-  Day-by-day itinerary** with specific activities
-  Hotel recommendations** with approximate costs
-  Restaurant suggestions** with price ranges
-  Tourist attractions** and off-beat locations
-  Transportation options** and costs
-  Weather forecast** for your travel dates
-  Detailed expense breakdown** and daily budget
-  Currency conversion** for international trips

##  Project Structure

```
AgentXplore/
├── agent/
│   └── agentic_workflow.py      # Core agent logic (GraphBuilder)
├── config/
│   └── config.yaml              # Model configuration
├── tools/
│   ├── weather_info_tool.py     # Weather intelligence
│   ├── place_search_tool.py     # Location search
│   ├── currency_conversion_tool.py # Currency conversion
│   └── expense_calculator_tool.py  # Budget calculations
├── utils/
│   ├── model_loader.py          # LLM provider management
│   ├── config_loader.py         # Configuration loading
│   ├── weather_info.py          # Weather API service
│   ├── place_info_search.py     # Places API service
│   └── currency_converter.py    # Currency API service
├── prompt_library/
│   └── prompt.py                # System prompts
├── main.py                      # FastAPI backend
├── streamlit_app.py             # Streamlit frontend
├── requirements.txt             # Python dependencies
├── setup.py                     # Package configuration
├── .env                         # Environment variables (create this)
└── README.md                    # This file
```

##  Configuration

### Switching Between LLM Providers

You can switch between Groq and OpenAI by modifying `main.py`:

```python
# For Groq (faster, free tier)
graph = GraphBuilder(model_provider="groq")

# For OpenAI (more capable, paid)
graph = GraphBuilder(model_provider="openai")
```

### Model Configuration

Modify `config/config.yaml` to change model settings:

```yaml
llm:
  groq:
    provider: "groq"
    model_name: "deepseek-r1-distill-llama-70b"
  openai:
    provider: "openai" 
    model_name: "gpt-4o-mini"
```

##  Troubleshooting

### Common Issues

#### 1. **500 Internal Server Error**
- **Cause**: Invalid or missing API keys
- **Solution**: Check your `.env` file and ensure API keys are valid

#### 2. **Module Not Found Error**
- **Cause**: Dependencies not installed
- **Solution**: Run `pip install -r requirements.txt`

#### 3. **Environment Variables Not Loading**
- **Cause**: `.env` file not being read
- **Solution**: Export variables manually or restart servers after creating `.env`

#### 4. **Port Already in Use**
- **Cause**: Previous server instances still running
- **Solution**: 
  ```bash
  # Kill existing processes
  pkill -f uvicorn
  pkill -f streamlit
  
  # Then restart servers
  ```

#### 5. **API Rate Limits**
- **Cause**: Exceeded free tier limits
- **Solution**: Wait for reset or upgrade to paid tier

### Debugging Steps

1. **Check server logs** in terminal for error messages
2. **Verify API keys** are correctly formatted and valid
3. **Test backend** directly:
   ```bash
   curl -X POST "http://localhost:8000/query" \
   -H "Content-Type: application/json" \
   -d '{"question": "test"}'
   ```
4. **Check environment variables**:
   ```bash
   echo $GROQ_API_KEY
   ```

##  Updates and Maintenance

### Updating Dependencies

```bash
pip install --upgrade -r requirements.txt
```

### Adding New Tools

1. Create new tool in `tools/` directory
2. Add corresponding utility in `utils/`
3. Import and add to `agentic_workflow.py`
4. Update requirements if needed

##  License

This project is licensed under the MIT License - see the LICENSE file for details.

##  Author

**Eeshan Pancholiya**
- Email: epancholiya@gmail.com
- Project: AgentXplore - AI Travel Planning Agent

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 🙏 Acknowledgments

- Built with [LangChain](https://langchain.com/) and [LangGraph](https://langchain-ai.github.io/langgraph/)
- Powered by [Groq](https://groq.com/) and [OpenAI](https://openai.com/)
- UI built with [Streamlit](https://streamlit.io/)
- Backend powered by [FastAPI](https://fastapi.tiangolo.com/)

---

**Happy Traveling! ✈️🌍**

For support or questions, please open an issue on the repository.