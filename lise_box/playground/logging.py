import logging
log = logging.getLogger(__name__)


if __name__ == '__main__':
    import logging
    logging.basicConfig(
        filename  = 'app.log',      # Log output file
        level     = logging.INFO,   # Output level
    )

# def parse(f,types=None,names=None,delimiter=None):
#     ...
#     try:
#         records.append(split(line,types,names,delimiter))
#     except ValueError as e:
#         log.warning("Couldn't parse : %s", line)
#         log.debug("Reason : %s", e)

# Create a logger object.

# log = logging.getLogger(name)   # name is a string
# Issuing log messages.
#
# log.critical(message [, args])
# log.error(message [, args])
# log.warning(message [, args])
# log.info(message [, args])
# log.debug(message [, args])

# logmsg = message % args