
def log(func):

    def wrap(*args, **kwargs):

        logger.info(...)

        res = func(*args, **kwargs)

        return res

    return wrap

