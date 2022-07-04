class AccountActiveException(Exception):
    message = 'Account active, disable before delete holder'


class AccountHasBalanceException(Exception):
    message = 'Account has balance, withdraw before delete holder'
