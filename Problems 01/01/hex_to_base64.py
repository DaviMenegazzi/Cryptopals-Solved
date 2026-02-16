"""CONVERTE HEXADECIMAIS EM BASE64"""

string = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
hex_map = {
    "a": 10, "b": 11, "c": 12,
    "d": 13, "e": 14, "f": 15,
    "g": 16, "h": 17, "i": 18
}

def hex_em_bits(n):
    try:
        if int(n): # é número
            return "{0:04b}".format(int(n))
    except ValueError: # é caractere
        lista = []
        def retorna_divisao (numero_atual, n):
            if (n != 0):
                resto = numero_atual % n
                quociente = numero_atual // n
                lista.append(resto)
                if quociente != 0:
                    retorna_divisao(quociente, n)
        retorna_divisao(hex_map[n], 2)
        return "".join([str(i) for i in lista[::-1]]) 

bits = []
for caractere in string:
    em_bits = hex_em_bits(caractere)
    if em_bits == None: # NOTE: por algum motivo, quando o número no hex é "0" ele retorna None e dá problema no resto do código inteiro
        em_bits = "0000"
    if (em_bits != None):
        bits.append(em_bits)

# separa em chunks de 6 bits para a conversão em base64

bits = "".join([str(bit) for bit in bits])

bloco = None
caracteres_base64 = []
for i in range(0, len(bits), 6):
    bloco = bits[i:i+6]

    # Se o bloco for menor que 6, preencher com '0' à direita
    if len(bloco) < 6:
        bloco = bloco.ljust(6, '0')

    caracteres_base64.append(alfabeto[int(bloco, 2)])

print("".join(c for c in caracteres_base64))

