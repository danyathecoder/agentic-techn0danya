import logging
import sys
from pathlib import Path

def setup_logging(log_level: str = "INFO", log_file: Path = Path("app.log")):
    """
    Configures logging for the application with specified level and file.

    Args:
        log_level (str): The minimum logging level to capture (e.g., "DEBUG", "INFO", "WARNING").
        log_file (Path): The path to the log file.
    """
    # Get the numeric value for the string log level
    numeric_level = getattr(logging, log_level.upper(), None)
    if not isinstance(numeric_level, int):
        raise ValueError(f"Invalid log level: {log_level}")

    # Define the format for log messages
    log_format = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

    # Get the root logger
    logger = logging.getLogger()
    logger.setLevel(numeric_level)

    # Clear any existing handlers to prevent duplicate logs if this function is called again
    if logger.hasHandlers():
        logger.handlers.clear()

    # Create and configure console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(log_format)

    # Create and configure file handler
    try:
        file_handler = logging.FileHandler(log_file, mode='a', encoding='utf-8')
        file_handler.setFormatter(log_format)
    except (IOError, OSError) as e:
        logging.error(f"Failed to create log file at {log_file}: {e}", exc_info=True)
        # Continue with console logging even if file logging fails
        file_handler = None

    # Add handlers to the root logger
    logger.addHandler(console_handler)
    if file_handler:
        logger.addHandler(file_handler)

    logging.info("Logging configured successfully to level %s.", log_level.upper())