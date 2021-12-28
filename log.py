# main.py
import logging
import somelib

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s: %(name)s: %(levelname)s: %(message)s")
logger = logging.getLogger("main123")


def main():
    logger.info("py01")
    somelib.do_something()


if __name__ == '__main__':
    main()


