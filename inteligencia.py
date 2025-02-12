import google.generativeai as genai

def detectar_ingredientes(chave, imagem):
    genai.configure(api_key=chave)
    modelo = genai.GenerativeModel('gemini-1.5-flash')

    prompt = '''Liste quais são os ingredientes dessa imagem.
    Os ingredientes devem ser apresentados em uma lista separada por virgula, como no exemplo a seguir.
    Nenhum texto adicional deve ser gerado como resposta além dos próprios ingredientes.
    # Exemplo de saída:
    arroz, feijão, frango
    '''

    resposta = modelo.generate_content([prompt, imagem])
    ingredientes = resposta.text.split(",")
    
    return ingredientes

def possiveis_receitas(chave, ingredientes):
    genai.configure(api_key=chave)
    modelo = genai.GenerativeModel('gemini-1.5-flash')

    prompt = f'''Considerando a seguinte lista de ingredientes, gere uma lista de receitas culinárias que os utilizem.
    As receitas devem tentar incluir a maior parte dos ingredientes.
    Gere apenas uma lista com os nomes das receitas, separados por vírgula.

    # Lista de ingredientes
    {ingredientes}

    # Exemplo de saída
    Receita 1, Receita 2, Receita 3
    '''

    resposta = modelo.generate_content(prompt)
    receitas = resposta.text.split(",")
    
    return receitas

def receita_completa(chave, ingredientes, receita):
    genai.configure(api_key=chave)
    modelo = genai.GenerativeModel('gemini-1.5-flash')

    prompt = f'''Crie a receita para o prato: "{receita}".
    Inclua a maior quantidade possível dos ingredites da lista de ingredientes.

    " Lista de ingredientes
    {ingredientes}
    '''

    resposta = modelo.generate_content(prompt)
    
    
    return resposta.text