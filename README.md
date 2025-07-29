# Agentic AI techn0danya

[![Python Version](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code Style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Telegram bot, that was built for Agentic AI demo for H&S skills and would be used to show some basic Agentic AI concepts.

## Table of Contents

- [Core Features](#core-features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Setup and Installation](#setup-and-installation)
- [Configuration](#configuration)
  - [1. Environment Variables](#1-environment-variables)
  - [2. Prompt Configuration](#2-prompt-configuration)
- [Usage](#usage)
- [Logging](#logging)
- [Contributing](#contributing)
- [License](#license)

## Core Features

Trying to automate one chatty guy telegram posting routine.

## Tech Stack

- **Language**: Python 3.9+
- **Package Manager**: [Poetry](https://python-poetry.org/)
- **Telegram Bot Framework**: [`python-telegram-bot`](https://python-telegram-bot.org/)
- **HTTP Requests**: [`httpx`](https://www.python-httpx.org/)
- **LLM Gateway**: [OpenRouter API](https://openrouter.ai/docs)

## Project Structure

The project is organized to separate concerns, making it clean and maintainable.

```
agentic-techn0danya/
├── .gitignore                  # Git ignore file
├── README.md                   # This file
├── agentic-techn0danya/
|   ├── agentic_techn0danya/    # Core bot package
|       ├── init.py             # Makes 'agentic_techn0danya' a Python package
|       ├── bot.py
|       ├── logger.py           # Logging setup and configuration
|   ├── main.py                 # Main entry point to start the application
|   ├── poetry.lock             # Poetry lock file for deterministic installs
|   ├── pyproject.toml          # Poetry project configuration and dependencies
|   ├── .env.example            # Example environment variables file
|   ├── tests/                  # Directory for unit and integration tests
|       └── ...
├── prompts/
    ├── chat_system_prompt.txt  # <-- Used to demostrate full flow of Agentic AI thinking during the lecture
    ├── system_prompt.txt       # Defines the bot's overall role and personality
    ├── user_prompt.txt         # Defines the specific task for the bot
```

## Setup and Installation

Follow these steps to get the bot running locally.

1.  **Clone the Repository**
    ```bash
    git clone https://github.com/your-username/agentic-techn0danya.git
    cd agentic-techn0danya
    ```

2.  **Install Poetry**
    If you don't have Poetry, follow the [official installation instructions](https://python-poetry.org/docs/#installation).

3.  **Install Project Dependencies**
    Poetry will create a virtual environment and install all the necessary packages from `pyproject.toml`.
    ```bash
    poetry install
    ```

## Configuration

Before running the bot, you need to configure your API keys and prompts.

### 1. Environment Variables

1.  Create a `.env` file in the root of the project directory by copying the example file.
    ```bash
    cp .env.example .env
    ```

2.  Open the `.env` file and fill in your credentials:
    ```ini
    # .env

    # Get this from BotFather on Telegram
    TELEGRAM_BOT_TOKEN="YOUR_TELEGRAM_BOT_TOKEN"

    # Get this from your OpenRouter account dashboard
    OPENROUTER_API_KEY="YOUR_OPENROUTER_API_KEY"

    # Set the desired logging level (DEBUG, INFO, WARNING, ERROR)
    LOG_LEVEL="INFO"
    ```

### 2. Prompt Configuration

The bot's behavior is controlled by the files in the `/prompts` directory.
-   **`prompts/chat_system_prompt.txt`**: This file tells the AI *how to behave*. Define its personality, role, and general instructions here to demonstrate how bot communicates as custom chat.
-   **`prompts/system_prompt.txt`**: This file tells the AI *how to behave*. Define its personality, role, and general instructions here for the Telegram bot.
-   **`prompts/user_prompt.txt`**: This file defines the specific task for the AI when the `/generate` command is used. You can use the `{user_input}` placeholder, which will be replaced with any text the user provides after the command.

**Example `user_prompt.txt`:**
```
Generate a concise and engaging Telegram post about the following topic: {user_input}.
Ensure the information is current by using your web search ability.
```

## Usage

1.  **Activate the Virtual Environment**
    ```bash
    poetry shell
    ```

2.  **Run the Bot**
    Execute the main script to start the bot.
    ```bash
    python main.py
    ```    You should see log messages in your console indicating that the bot has started successfully.

3.  **Interact with the Bot on Telegram**
    Open Telegram and find the bot you created with BotFather.
    -   **Simple Generation**: Send the command:
        ```
        /generate
        ```

## Logging

-   All events are logged to the **console** in real-time.
-   A complete log history is saved to **`app.log`** in the project root.
-   The verbosity of the logs can be controlled by setting the `LOG_LEVEL` variable in your `.env` file. Recommended levels:
    -   `INFO`: For normal operation.
    -   `DEBUG`: For detailed troubleshooting.

## Contributing

Contributions are welcome! If you have suggestions for improvements or find a bug, please feel free to open an issue or submit a pull request. Who knows, probably we can make AGI from this.

## License

This project is licensed under the MIT License. See the [LICENSE](https://opensource.org/licenses/MIT) file for details.