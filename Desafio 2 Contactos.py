import json

contactos= {
    "Pedro": {
        "numero": 2617823482,
        "edad":26,
        "correo": "pedroperez@gmail.com", 
        },
    "Juan":{
        "numero": 2618934372,
        "edad":29,
        "correo": "juanlocura@yahoo.com.ar",
    },
    "Marta":{
        "numero":2617891234,
        "edad": 27,
        "correo": "martagimenez@gmail.com"
    }, 
    "Lupe":{
        "numero":2611234567,
        "edad":34,
        "correo":"lupepaz@hotmail.com"
    }
}
with open("contactos.json","r") as archivo: 
    contactos.json= json.load(archivo) 
    print(contactos.json)
    
    print(f"Numero de telefono:{contactos.json["numero"]}")
    print(f"Edades:{contactos.json["edad"]}")
    print(f"Correos:{contactos.json["correo"]}")