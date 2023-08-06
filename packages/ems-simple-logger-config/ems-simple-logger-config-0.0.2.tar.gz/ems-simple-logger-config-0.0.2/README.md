# ems-simple-logger-config

This is a simple (file) logger configuration for Python.

Installation:
```
pip install ems-simple-logger-config
```

On app level: Initialize logger with default values to get a common console output:
```
import logger

log = logger.setup_logger()
log.info('Some text')
```

On app level: Alternatively initialize logger with some configuration. If file_name is added a log file will be created.
```
import logger

log = logger.setup_logger(logger_name = 'SomeLoggerName', log_level = logging.DEBUG, file_name = 'log.txt')
log.info('Some text')
```

On module level get the logger by
```
log = logger.get_logger(__name__)
log.info('Some text')
```