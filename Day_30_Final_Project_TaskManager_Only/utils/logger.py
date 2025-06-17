import logging

def setup_logging():
    logging.basicConfig(
        filename="data/task_log.txt",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )
    logging.info("🔧 Task Manager started")
