from collections import Counter

def contar_caracteres(letra):
    """Função que conta os caracteres de uma string
    Ex:
    >>> contar_caracteres('Araujo')
    {'a': 2, 'r': 1, 'u': 1, 'j': 1, 'o': 1}
    >>> contar_caracteres('banana')
    {'a',: 3, 'b',: 1, 'n',: 2,}
        :param letra: string a ser contada
    """

    # Transforma todas as letras em minúsculas
    letra = letra.lower()
    collection = Counter(letra)
    # Uso do método format dentro do print
    print('Quantidade de letras em {}: {}'.format(letra, collection))
    return collection

if __name__ == '__main__':
        letra = 'Araujo'
        collection = contar_caracteres(letra)
        print('A quantidade de letras "a" é igual à: {}'.format(collection['a']))
        contar_caracteres('banana')