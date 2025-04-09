def convert(s: str, numRows: int) -> str:
    # Se só tem 1 linha ou a string é menor que o número de linhas,
    # não é necessário converter para zigzag
    if numRows == 1 or numRows >= len(s):
        return s

    # Criamos uma lista de strings, uma para cada linha do zigzag
    rows = [''] * numRows  # Ex: ['','',''] para 3 linhas

    # Pergunta: O que essa lista 'rows' armazena?
    # → Ela guarda os caracteres de cada linha do padrão zigzag

    # Começamos na linha 0
    curr_row = 0

    # Direção inicial: "subindo" ou "descendo" (começamos subindo, mas isso muda)
    going_down = False

    # Pergunta: Para que serve 'going_down'?
    # → Ele controla a direção atual do zigzag (descendo ou subindo)

    # Para cada caractere na string de entrada
    for char in s:
        # Adiciona o caractere na linha atual
        rows[curr_row] += char

        # Se estamos no topo (linha 0) ou fundo (última linha), mudamos de direção
        if curr_row == 0 or curr_row == numRows - 1:
            going_down = not going_down

        # Dependendo da direção, vamos para a próxima linha ou subimos uma
        curr_row += 1 if going_down else -1

        # Pergunta: O que essa linha faz? curr_row += 1 if going_down else -1
        # → Se estamos descendo, vai para a próxima linha. Se subindo, volta uma linha.

    # Junta todas as linhas em uma string só
    return ''.join(rows)

    # Pergunta: Por que usamos ''.join(rows)?
    # → Para juntar todas as linhas do zigzag em uma única string de resultado

entrada1 = "PAYPALISHIRING"
linhas1 = 3
print("Entrada:", entrada1)
print("numRows =", linhas1)
print("Saída esperada: PAHNAPLSIIGYIR")
print("Saída real:     ", convert(entrada1, linhas1))
print()


