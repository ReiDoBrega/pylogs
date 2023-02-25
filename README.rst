pylogs: Custom log levels for Python's logging module.
==============================================================

Installation
------------

.. code-block:: sh

   pip install git+https://github.com/ReiDoBrega/pylogs.git


Usage:

.. code-block:: python
   
    from pylogs import Logger, logging

    log_format = "{asctime} - {levelname} - {name} - {lineno} : {message}"
    log_date_format = '%Y-%m-%d %I:%M:%S %p'
    log_style = "{"
    logging.basicConfig(
        level=logging.INFO,
        format=log_format,
        datefmt=log_date_format,
        handlers=[logging.StreamHandler()],
        style=log_style,
    )
    log = Logger('MyClassName')

    log.success("Are you Working? Yuup")
    
here another example, but with coloredlogs:

.. code-block:: python
   
    import coloredlogs
    from pylogs import Logger, logging

    log_format = "{asctime} - {levelname} - {name} - {lineno} : {message}"
    log_date_format = '%Y-%m-%d %I:%M:%S %p'
    log_style = "{"
    logging.basicConfig(
        level=logging.INFO,
        format=log_format,
        datefmt=log_date_format,
        handlers=[logging.StreamHandler()],
        style=log_style,
    )
    coloredlogs.install(
        level=logging.INFO,
        fmt=log_format,
        datefmt=log_date_format,
        handlers=[logging.StreamHandler()],
        style=log_style
    )

    log = Logger('MyClassName')

    log.logkey("Hey, do you remember that, old NFTool user?")
    log.logkey("b770d5b4bb6b594daf985845aae9aa5f:b0cb46d2d31cf044bc73db71e9865f6f")

output with coloredlogs:

.. image:: https://github.com/ReiDoBrega/pylogs/raw/master/examples/screenshots/1.png
