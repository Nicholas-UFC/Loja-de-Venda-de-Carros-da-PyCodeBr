import google.generativeai as genai


def get_car_ai_bio(model, brand, year):
    api_key = "SUA API KEY"
    genai.configure(api_key=api_key)

    prompt_template = """
    Você é um assistente de vendas de carros.
    Crie uma descrição de venda atraente para o carro {brand} {model} {year} em até 250 caracteres.
    Seja específico sobre as qualidades e características conhecidas deste modelo.
    """
    prompt = prompt_template.format(brand=brand, model=model, year=year)

    model_gemini = genai.GenerativeModel("gemini-1.5-pro-latest")
    response = model_gemini.generate_content(prompt)
    return response.text
