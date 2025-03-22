from flask import Flask, render_template, request

app = Flask(__name__)

def decimal_para_binario(decimal):
    if decimal == 0:
        return "0", [], []
    
    binario = ""
    numero = decimal
    passos = []  # Lista para armazenar os passos da conversão
    
    while numero > 0:
        resto = numero % 2
        passos.append((numero, resto))  # Armazena o número atual e o resto
        binario = str(resto) + binario
        numero = numero // 2
        
    # Calcula as posições das potências de 2 e seus valores
    posicoes_potencia = [(i, 2 ** i, binario[::-1][i] if i < len(binario) else "0") for i in range(len(binario))]
    return binario, passos, posicoes_potencia

def binario_para_decimal(binario):
    try:
        decimal = int(binario, 2)
        passos = []
        soma_horizontal = ""  # Para mostrar a soma horizontal
        posicoes_potencia = []
        
        # Calcula os passos e as posições das potências de 2
        for i, bit in enumerate(reversed(binario)):
            valor = int(bit) * (2 ** i)
            passos.append((bit, i, 2 ** i, valor))
            posicoes_potencia.append((i, 2 ** i, bit))
            
            # Constrói a soma horizontal, incluindo todos os bits
            if soma_horizontal:
                soma_horizontal += f" + {bit} × 2{get_sobrescrito(i)}"
            else:
                soma_horizontal += f"{bit} × 2{get_sobrescrito(i)}"
        
        if soma_horizontal:
            soma_horizontal += f" = {decimal}"
        
        return decimal, passos, posicoes_potencia, soma_horizontal
    except ValueError:
        return None, [], [], ""

# Função auxiliar para gerar potências sobrescritas
def get_sobrescrito(numero):
    sobrescrito_map = {
        "0": "⁰", "1": "¹", "2": "²", "3": "³", "4": "⁴",
        "5": "⁵", "6": "⁶", "7": "⁷", "8": "⁸", "9": "⁹"
    }
    return "".join(sobrescrito_map[digito] for digito in str(numero))

@app.route("/", methods=["GET", "POST"])
def index():
    resultado_manual = ""
    resultado_builtin = ""
    erro = ""
    passos_calculo = []  # Para armazenar os passos da conversão
    posicoes_potencia = []  # Para armazenar as posições das potências de 2
    soma_horizontal = ""  # Para mostrar a soma horizontal na conversão binário -> decimal
    aba_ativa = "decimal_para_binario"  # Aba ativa por padrão
    easter_egg = False  # Para controlar o Easter Egg

    if request.method == "POST":
        aba_ativa = request.form.get("aba_ativa")

        if aba_ativa == "decimal_para_binario":
            try:
                decimal = int(request.form.get("decimal"))
                if decimal == 13:  # Easter Egg
                    easter_egg = True
                if decimal < 0:
                    erro = "Por favor, digite um número positivo."
                else:
                    # Converte usando nossa função
                    resultado_manual, passos_calculo, posicoes_potencia = decimal_para_binario(decimal)
                    
                    # Compara com o método built-in do Python
                    resultado_builtin = bin(decimal)[2:]  # Remove o prefixo "0b"
            except ValueError:
                erro = "Por favor, digite um número válido."

        elif aba_ativa == "binario_para_decimal":
            try:
                binario = request.form.get("binario")
                if binario == "1101":  # Easter Egg
                    easter_egg = True
                decimal, passos_calculo, posicoes_potencia, soma_horizontal = binario_para_decimal(binario)
                if decimal is None:
                    erro = "Por favor, digite um número binário válido."
                else:
                    resultado_manual = decimal
                    resultado_builtin = int(binario, 2)
            except ValueError:
                erro = "Por favor, digite um número binário válido."

    return render_template("index.html", 
                           resultado_manual=resultado_manual, 
                           resultado_builtin=resultado_builtin, 
                           erro=erro, 
                           passos_calculo=passos_calculo,
                           posicoes_potencia=posicoes_potencia,
                           soma_horizontal=soma_horizontal,
                           aba_ativa=aba_ativa,
                           easter_egg=easter_egg)

if __name__ == "__main__":
    app.run(debug=True)