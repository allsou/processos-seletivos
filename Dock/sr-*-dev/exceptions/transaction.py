class InvalidDateParamsException(Exception):
    message = ('Query params must be begin_date',
               ' and end_date in dd/mm/aaaa format')


class TransactionNotAllowedException(Exception):
    message = 'Account not allowed to transact'


class NotBalanceEnoughException(Exception):
    message = 'Not balance enough'


class DailyLimitException(Exception):
    message = 'Daily limit reached!'
