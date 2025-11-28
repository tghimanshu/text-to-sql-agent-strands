# AWS Agent

AWS Agent is a Python-based project that leverages the `strands` library and Gemini models to create intelligent agents capable of performing various tasks, including natural language processing, math calculations, and database operations.

## Features

- **Intelligent Agent**: Uses Google's Gemini models via `strands` to answer queries.
- **Custom Tools**: Includes a custom `letter_counter` tool to demonstrate tool creation.
- **Database Operations**: Utilities to merge and manage SQLite databases.

## Project Structure

- `agent.py`: Defines the Strands agent, configures the Gemini model, and includes custom tools.
- `database_operations.py`: Contains functions to combine and manage SQLite databases.
- `main.py`: Entry point for the application.
- `__init__.py`: Package initialization file.

## Prerequisites

- Python 3.13 or higher.
- A Google Gemini API Key.

## Setup

1.  **Clone the repository:**
    ```bash
    git clone <repository_url>
    cd aws-agent
    ```

2.  **Install dependencies:**
    This project uses `uv` for dependency management, but can be installed via pip.
    ```bash
    pip install -r pyproject.toml
    # OR if you have a requirements.txt generated
    # pip install -r requirements.txt
    ```

    *Note: The project defines dependencies in `pyproject.toml`.*

    Dependencies include:
    - `boto3`
    - `python-dotenv`
    - `strands-agents[gemini]`

3.  **Environment Configuration:**
    Create a `.env` file in the root directory and add your Gemini API key:
    ```
    GEMINI_API_KEY=your_api_key_here
    ```

## Usage

### Running the Agent

To run the agent and see it answer sample queries:

```bash
python agent.py
```

This will initialize the agent and process the hardcoded message in `agent.py`.

### Database Operations

To use the database combination utility:

```python
from database_operations import combine_sqlite_databases

combine_sqlite_databases("source.db", "target.db")
```

You can also run the script directly if you have `weather_data.sqlite` and `time_series.sqlite` in your directory (for testing purposes):

```bash
python database_operations.py
```

### Main Entry Point

To run the main application entry point:

```bash
python main.py
```
