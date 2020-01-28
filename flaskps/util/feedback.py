class PageUnderConstruction(Exception):
    '''The required page is under construction'''


class AppInMaintenanceMode(Exception):
    '''The aplication is in maintenance mode'''


class RestrictedAcess(Exception):
    '''Restricted acess for this page'''


class UserHasNoSession(Exception):
    '''Session not active'''


class ChangeBaseRole(Exception):
    '''Operation rejected'''


class FailEmailSend(Exception):
    '''Unable to send email'''

class UserIsBloqued(Exception):
    '''The user is bloqued'''