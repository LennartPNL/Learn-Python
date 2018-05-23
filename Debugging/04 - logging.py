# Logging stuff

import logging

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start of program')

def factorial(n):
    logging.debug('Start of factorial(%s)' % (n))
    total = 1
    for i in range(n + 1): # This will be logged! should be "for i in range(1, n + 1):" of course
        total *= i
        logging.debug('i is ' + str(i) + ' total is ' + str(total))
    logging.debug('factorial(%s)' % (n) + ' has ended')
    return total

factorial(7)


# Logging can be categorized in levels:
# You can change the priority of certain log messages

logging.debug('This is the deepest level of logging')
logging.info('General info: check if your program is working like it should')
logging.warning('Indicating potential problems')
logging.error('Show program breakers')
logging.critical('indicate fatal errors')

# Logging disabled

logging.disable(logging.DEBUG)

logging.debug('This message will now be disabled')
logging.info('this message is not affected')
logging.warning('this message is not affected')
logging.error('this message is not affected')
logging.critical('this message is not affected')

# Logging to a file (run this code separately from the code above)
logging.basicConfig(filename='loggingModule.txt', level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.debug('Writing to this file...')

logging.debug('This is the deepest level of logging')
logging.info('General info: check if your program is working like it should')
logging.warning('Indicating potential problems')
logging.error('Show program breakers')
logging.critical('indicate fatal errors')

