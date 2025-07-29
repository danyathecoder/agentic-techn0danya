import os
import logging
from agentic_techn0danya.logger import setup_logging
from agentic_techn0danya.bot import setup_bot

def main() -> None:
    """
    Entry point for the application.
    """
    # Get log level from environment variable, default to "INFO" if not set
    log_level = os.getenv("LOG_LEVEL", "INFO")

    # Configure logging with the specified level
    setup_logging(log_level=log_level)

    try:
        application = setup_bot()
        logging.info("Bot is starting up...")
        application.run_polling()
    except Exception as e:
        logging.critical("Application failed to start or crashed.", exc_info=True)
    finally:
        logging.info("Bot has been shut down.")

if __name__ == '__main__':
    main()