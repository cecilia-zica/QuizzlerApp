import requests

parameters = {
    "amount": 10, # É como selecionar "Mostrar 10 itens por página"
    "type": "boolean"  # É como marcar a caixinha "Apenas do tipo Verdadeiro/Falso"
}
response = requests.get(
                        "https://opentdb.com/api.php",
                        params = parameters
                        )
response.raise_for_status()
data = response.json()
question_data = (data["results"])
