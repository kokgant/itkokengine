# -*- coding: utf-8 -*-
from django.utils.log import DEFAULT_LOGGING
from .local_settings import PROJECT_PATH

log_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        # 'django.server': DEFAULT_LOGGING['formatters']['django.server'],
        "simple": {
            "format": "%(levelname)s - %(asctime)s - %(name)s - %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
        "file": {"format": "%(asctime)s %(name)-12s %(levelname)-8s %(message)s"},
    },
    "handlers": {
        # 'django.server': DEFAULT_LOGGING['handlers']['django.server'],
        "console": {
            "class": "logging.StreamHandler",
            "level": "INFO",
            "formatter": "simple",
            "stream": "ext://sys.stdout",
        },
        "itkokengine": {
            "class": "logging.handlers.RotatingFileHandler",
            "level": "INFO",
            "formatter": "simple",
            "filename": f"{PROJECT_PATH}/logs/itkokengine.log",
            "maxBytes": 5242880,
            "backupCount": 2,
            "encoding": "utf8",
        },

        "core": {
            "class": "logging.handlers.RotatingFileHandler",
            "level": "INFO",
            "formatter": "simple",
            "filename": f"{PROJECT_PATH}/logs/core.log",
            "maxBytes": 5242880,
            "backupCount": 2,
            "encoding": "utf8",
        },
        
        "file": {
            "level": "INFO",
            "class": "logging.FileHandler",
            "formatter": "file",
            "filename": f"{PROJECT_PATH}/logs/file.log",
        },
    },
    "loggers": {
        # 'django.server': DEFAULT_LOGGING['loggers']['django.server'],
        "": {"level": "INFO", "handlers": ["console",],},
        "itkokengine": {"level": "INFO","handlers": ["itkokengine"],"propagate": False,},
        "core": {"level": "INFO","handlers": ["core"],"propagate": False,},
        "consola": {"level": "DEBUG", "handlers": ["console"], "propagate": False,},
    },
}
