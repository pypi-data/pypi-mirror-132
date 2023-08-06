import inspect
import logging
import traceback

import logs.client_log_config

from socket import socket

LOGGER = logging.getLogger('client')


class Log:
    """
    Класс-декоратор, выполняющий логирование вызовов функций.
    Сохраняет событие типа 'info', содержащее:
    Имя вызываемой функции, параметры, с которыми она вызывается,
    функция из которой она вызывается, и модуль, вызывающий функцию.
    """

    def __call__(self, func):
        def decorated(*args, **kwargs):
            splitter = '\\'
            res = func(*args, **kwargs)
            LOGGER.info(f'Произошел вызов функции {func.__name__} со следующими параметрами - {args}, {kwargs}. '
                        f'Вызов произошел из функции {traceback.format_stack()[0].split()[-1]} '
                        f'модуля {inspect.stack()[0][1].split(splitter)[-1]}')
            return res

        return decorated


def login_required(func):
    """
    Функция-декоратор, проверяющая, что клиент авторизован на сервере.
    Проверяет, что передаваемый объект сокета находится в
    списке авторизованных клиентов.
    За исключением передачи словаря-запроса на авторизацию.
    Если клиент не авторизован, генерирует исключение TypeError
    """

    def checker(*args, **kwargs):
        from common.variables import ACTION, PRESENCE
        from server.server.core import MessageProcessor
        if isinstance(args[0], MessageProcessor):
            found = False
            for arg in args:
                if isinstance(arg, socket):
                    for client in args[0].names:
                        if args[0].names[client] == arg:
                            found = True
            for arg in args:
                if isinstance(arg, dict):
                    if ACTION in arg and arg[ACTION] == PRESENCE:
                        found = True
            if not found:
                raise TypeError
        return func(*args, **kwargs)

    return checker
