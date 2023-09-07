from flask import Flask, render_template, request

app = Flask(__name__)

def calcular_anos_meses_dias(dias):
    # Um ano médio tem 365,25 dias
    anos = int(dias / 365.25)
    # O restante de dias após calcular os anos
    dias_restantes = dias % 365.25

    # Um mês médio tem cerca de 30,44 dias
    meses = int(dias_restantes / 30.44)
    # O restante de dias após calcular os meses
    dias_finais = int(dias_restantes % 30.44)

    return anos, meses, dias_finais


@app.route('/', methods=['GET', 'POST'])
def index():
    resultado = None
    if request.method == 'POST':
        try:
            dias = int(request.form['dias'])
            anos, meses, dias_finais = calcular_anos_meses_dias(dias)
            resultado = f"{dias} dias correspondem a {anos} anos, {meses} meses e {dias_finais} dias."
        except ValueError:
            resultado = "Por favor, insira um número válido de dias."
    
    return render_template('index.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=False)
