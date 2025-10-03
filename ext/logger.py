import logging
import functools
import disnake
import time
from pathlib import Path


def setup_logger(name: str, level=logging.INFO):
    logger = logging.getLogger(name)
    logger.setLevel(level)

    formatter = logging.Formatter(
        "%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    file_handler = logging.FileHandler(Path('logs', name + '.log'), encoding="utf-8")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger

main_logger = setup_logger("main")

def command_logger():
    def decorator(func):
        logger = setup_logger(func.__module__)
        @functools.wraps(func)
        async def wrapper(self, inter: disnake.ApplicationCommandInteraction, *args, **kwargs):
            start = time.perf_counter()
            try:
                result = await func(self, inter, *args, **kwargs)

                duration = (time.perf_counter() - start) * 1000
                logger.info(
                    f"[SUCCESS] /{func.__name__} by {inter.author} "
                    f"in {inter.guild.name if inter.guild else 'DM'} "
                    f"Duration: {duration:.2f} ms"
                )
                return result

            except Exception as e:
                duration = (time.perf_counter() - start) * 1000
                logger.error(
                    f"[FAILED] /{func.__name__} by {inter.author} "
                    f"in {inter.guild.name if inter.guild else 'DM'} "
                    f"Error: {e} "
                    f"Duration: {duration:.2f} ms"
                )
                raise
        return wrapper
    return decorator           