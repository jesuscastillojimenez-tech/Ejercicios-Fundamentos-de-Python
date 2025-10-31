# analizador.py

OPERADORES = set('+-*/^')


def interpretar_expresion(entrada):
    """
    Analiza expresiones con 3 números y 2 operadores (a op b op c)
    sin usar librerías. Devuelve (n1, n2, n3, op1, op2) o None.
    """
    if not entrada:
        return None

    s = entrada.replace(" ", "")
    if s == "":
        return None

    tokens = []
    i = 0
    n = len(s)

    while i < n:
        ch = s[i]

        # Si es operador y no es signo de número
        if ch in OPERADORES:
            if ch in '+-' and (i == 0 or s[i-1] in OPERADORES):
                # signo unido al número
                j = i + 1
                while j < n and (s[j].isdigit() or s[j] == '.'):
                    j += 1
                if j == i + 1:
                    return None
                tokens.append(s[i:j])
                i = j
                continue
            else:
                tokens.append(ch)
                i += 1
                continue

        # Si es número o punto
        if ch.isdigit() or ch == '.':
            j = i
            puntos = 0
            while j < n and (s[j].isdigit() or s[j] == '.'):
                if s[j] == '.':
                    puntos += 1
                    if puntos > 1:
                        return None
                j += 1
            tokens.append(s[i:j])
            i = j
            continue

        # Carácter inválido
        return None

    # Deben ser exactamente 5 tokens: num op num op num
    if len(tokens) != 5:
        return None

    try:
        n1 = float(tokens[0])
        op1 = tokens[1]
        n2 = float(tokens[2])
        op2 = tokens[3]
        n3 = float(tokens[4])
    except:
        return None

    if op1 not in OPERADORES or op2 not in OPERADORES:
        return None

    return n1, n2, n3, op1, op2


def aplicar_operador(a, b, op):
    """
    Aplica un operador simple entre dos números.
    """
    if op == '+':
        return a + b
    if op == '-':
        return a - b
    if op == '*':
        return a * b
    if op == '/':
        try:
            return a / b
        except ZeroDivisionError:
            return "Error: División por cero."
    if op == '^':
        try:
            return a ** b
        except Exception as e:
            return f"Error potencia: {e}"
    return None
