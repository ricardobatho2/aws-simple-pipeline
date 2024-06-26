import os


configs = {
    "URL": "https://randomuser.me/api/?results=5",
    "bucket":{
        "raw": "s3://de04-demo/cadastro/raw/",
        "work": "s3://de04-demo/cadastro/work/",
        "logs": "s3://de04-demo/cadastro/logs/"    
    } ,
    "metadados":{
        "nome_original": [
            "gender",
            "name.title",
            "name.first",
            "name.last",
            "location.city",
            "location.state",
            "location.country",
            "email",
            "dob.date"
            ],
         "nome": [
            "sexo",
            "titulo",
            "nome",
            "sobrenome",
            "cidade",
            "estado",
            "pais",
            "email",
            "data_nascimento"
         ],
         "tipos":{
             "sexo": "string",
             "titulo": "string",
             "nome": "string",
             "sobrenome": "string",
             "cidade": "string",
             "estado": "string",
             "pais": "string",
             "email": "string",
             "data_nascimento": "date"
         }
    }
}