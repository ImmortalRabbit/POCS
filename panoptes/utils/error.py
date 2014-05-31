import sys

import panoptes.utils.logger as logger


@logger.has_logger
class Error(Exception):

    """ Base class for Panoptes errors """
    def __init__(self, msg=None):
        if msg:
            self.logger.error('{}: {}'.format(self.__class__.__name__,msg))
            self.msg = msg

    def exit_program(self, msg='No reason specified'):
        """ Kills running program """
        self.logger.error("TERMINATING: {}".format(msg))
        sys.exit()


class NotFound(Error):
    """ Generic not found class """
    def __init__(self, msg):
        # pass
        self.msg = msg
        self.exit_program(msg='Cannot find {}'.format(self.msg))

class InvalidConfig(Error):
    """ Error raised if config file is invalid """
    pass

class InvalidMountCommand(Error):
    """ Error raised if attempting to send command that doesn't exist """
    pass

class BadSerialConnection(Error):
    """ Error raised when serial command is bad """
    pass

class MountNotFound(NotFound):
    """ Mount cannot be import """
    pass
 
class CameraNotFound(NotFound):
    """ Camera cannot be import """
    pass