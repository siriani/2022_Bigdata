import requests
import json
def soma(a,b):
    return a+b

def subtracao(a,b):
    return a-b

a = int(input("Digite o primeiro numero:\n"))
print("Digite o segundo número:")
b = int(input())

soma1 = soma(a,b)

url = "https://data.mongodb-api.com/app/data-cdirn/endpoint/data/beta/action/insertOne"
payload = json.dumps({
    "collection": "testes",
    "database": "alunos",
    "dataSource": "Cluster0",
    "document": {
        "operacao": "a="+str(a)+" b="+str(b),
        "resultado": soma1

    }
})
headers = {
    'Content-Type': 'application/json',
    'Access-Control-Request-Headers': '*',
    'api-key': 'GBicXNTZ9woynIh37zevgkNUo7hvfmL3gUeNBVa7OA7s0MSHpQ4FUG9n7NlpbtA2'
}
response = requests.request("POST", url, headers=headers, data=payload)
print(response.text)

#