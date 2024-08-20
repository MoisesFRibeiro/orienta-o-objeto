def dividir(a, b):
    """metodo para dividir dois numeros
    args:
        a (any): dividendo
        b (any): divisor
    returns:
        str: mensagem de erro ou 'ok!' se a divisão for bem-sucedida
        any: quociente ou none em caso de erro   
    """

    if b == 0:
        return None, 'erro de divisão'
    else:
        divisao = a / b
        return divisao, 'ok!'