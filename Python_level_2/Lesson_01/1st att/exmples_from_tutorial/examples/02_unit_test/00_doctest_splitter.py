def split(line, types=None, delimiter=None):
    """ Разбивает текстовую строку и при необходимости
        выполняет преобразование типов.
        Например:
        >>> split('GOOG 100 490.50')
        ['GOOG', '100', '490.50']
        >>> split('GOOG 100 490.50',[str, int, float])
        ['GOOG', 100, 490.5]
        >>>
        По умолчанию разбиение производится по пробельным символам, 
        но имеется возможность указать другой символ-разделитель, в виде именованного аргумента:
    
        >>> split('GOOG,100,490.50',delimiter=',')
        ['GOOG', '100', '490.50']
        >>>
    """
    fields = line.split(delimiter)
    if types:
        fields = [ ty(val) for ty, val in zip(types, fields) ]
    return fields


def third(x):
    """ Возвращает треть от x. Например:

        >>> third(6.9)
        2.3
        >>>
    """
    return x / 3


if __name__ == '__main__':
    import doctest
    doctest.testmod()    
