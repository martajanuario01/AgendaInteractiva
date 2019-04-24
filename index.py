import json

# base de datos
def cargar_contactos():
    with open('./data/contactos.json') as file:
        data = json.load(file)
        file.close()
        return data

def guardar_contactos(contacts):
    with open('./data/contactos.json', 'w') as file:
        json.dump(contacts, file)
        file.close()

# funciones
def ver_contactos():
    contactos = cargar_contactos()
    print("Lista de contactos:")
    for index in range(len(contactos)):
        contact = contactos[index]
        print (str(index + 1) + ".-", contact['nombre'], contact['apellido'], "-->", contact['telefono'])

def anadir_contacto():   
    nombre = input("Nombre: ")
    apellido = input("Apelllido: ")
    telefono = input("Teléfono: ")
    contactos = cargar_contactos()
    contactos.append({
        'nombre': nombre,
        'apellido': apellido,
        'telefono': int(telefono)
    })

    guardar_contactos(contactos)
    print('-- Contacto añadido')

def borrar_contacto():
    contactos = cargar_contactos()
    print("Lista de contactos:")
    for index in range(len(contactos)):
        contact = contactos[index]
        print (str(index + 1) + ".-", contact['nombre'], contact['apellido'], "-->", contact['telefono'])
    index_contacto = int(input("-- Selecciona uno: ")) - 1
    contactos.remove(contactos[index_contacto])

    guardar_contactos(contactos)
    print("Contacto eliminado!")

def editar_contacto():
    contactos = cargar_contactos()
    campos = ["nombre", "apellido", "telefono"]
    print("Lista de contactos:")
    for index in range(len(contactos)):
        contact = contactos[index]
        print (str(index + 1) + ".-", contact['nombre'], contact['apellido'], "-->", contact['telefono'])
    index_contacto = int(input("-- Selecciona uno: ")) - 1
    print("Propiedades:")
    for index in range(len(campos)):
        print(str(index + 1) + ".-", campos[index].capitalize())

    propiedad = int(input("-- Selecciona una: ")) - 1
    valor = input("-- Nuevo valor: ")
    contacto = contactos[index_contacto]
    contacto[campos[propiedad]] = valor

    guardar_contactos(contactos)
    print("Contacto editado!")

operations = {
    '1': ver_contactos,
    '2': anadir_contacto,
    '3': borrar_contacto,
    '4': editar_contacto,
    '5': exit
}

while True:
        print('\nMenú\n-----------------------------')
        print('1.- Ver contactos')
        print('2.- Añadir contacto')
        print('3.- Eliminar contacto')
        print('4.- Editar contacto')
        print('5.- Salir')

        option = input('-- Selecciona una: ')
        function = operations.get(option, lambda: print('Acción no encontrada'))
        print("\n")
        function()
