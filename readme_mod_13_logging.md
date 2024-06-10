# Setting Up Logging with Loggly

## Introduction

This guide will walk you through the steps to set up logging in your Python application using Loggly, a cloud-based logging service.

## Prerequisites

Before you begin, make sure you have the following:

- Python installed on your system
- Pip package manager
- An active Loggly account
- Loggly token (API Key)

## Step 1: Install Required Packages

First, install the necessary Python package for integrating with Loggly. Open your terminal or command prompt and run:

```bash
poetry add loggly-python-handler
```

## Step 2: Add Loggly Handler in Your Application

In your Python application, import the Loggly HTTPSHandler and Formatter:

```bash
import os
from loggly.handlers import HTTPSHandler
from logging import Formatter
```

Next, configure the Loggly handler with your Loggly token:

```bash
loggly_token = os.getenv('LOGGLY_TOKEN')
loggly_url = f'https://logs-01.loggly.com/inputs/{loggly_token}/tag/python' if loggly_token else ''

args = (loggly_url, 'POST')
```

## Step 3: Set Up Logging Configuration

You can set up logging configuration using a configuration file. Here's an example configuration file (logging.conf):

```bash
[handlers]
keys=HTTPSHandler

[handler_HTTPSHandler]
class=loggly.handlers.HTTPSHandler
formatter=jsonFormat
args=('https://logs-01.loggly.com/inputs/${LOGGLY_TOKEN}/tag/python','POST')

[formatters]
keys=jsonFormat

[loggers]
keys=root

[logger_root]
handlers=HTTPSHandler
level=INFO

[formatter_jsonFormat]
format={ "loggerName":"%(name)s", "timestamp":"%(asctime)s", "fileName":"%(filename)s", "logRecordCreationTime":"%(created)f", "functionName":"%(funcName)s", "levelNo":"%(levelno)s", "lineNo":"%(lineno)d", "time":"%(msecs)d", "levelName":"%(levelname)s", "message":"%(message)s"}
```

Ensure that you replace ${LOGGLY_TOKEN} with your actual Loggly token.

## Step 4: Use Logging in Your Application
Finally, use the configured logger in your application code:

```bash
import logging
from logging.config import fileConfig

fileConfig('logging.conf')

logger = logging.getLogger(__name__)

logger.info('Logging configured successfully')
```

## Conclusion
You have now successfully set up logging in your Python application using Loggly. Your application will now send logs to your Loggly account for centralized logging and monitoring.