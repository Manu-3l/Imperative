#My_Project CUD -> Generar, Actualizar, eliminar, buscar

clients = 'Manuel Rosero'

def create_client(client_name):
    global clients
    if client_name not in clients:
        add_comma()
        clients += client_name
    else:
        print("Client name already exists {}".format(client_name))

def add_comma():
    global clients
    clients += ", "


def update_client(client_name, new_client_name):
    global clients
    if client_name in clients:
        clients =  clients.replace(client_name+ ",", new_client_name+ ",")
    else:
        print("Client name doesn't exists")

def delete_client(cl_nn):
    global clients
    if cl_nn in clients:
        clients = clients.replace(cl_nn+ ",","")
    else:
        print("Client name doesn't exists")


def _Print_welcome():
    print ("WELCOME UNIVERSIDAD DEL VALLE - TULUA")
    print ('*' * 100)
    print ("What would you like to do today")
    print ("[C]reate Client or user")
    print ("[R]ead Client or user")
    print ("[U]pdate Client or user")
    print ("[D]elete Client or user")

def get_client():
    return input("Type your name desired: ")

def _get_lists_clients_names():
    global clients
    print(clients)
    

if __name__ == '__main__':
    _Print_welcome()
    option = input("Type your option desired: ").upper()

    if option == 'C':
        client_name = get_client()
        create_client(client_name)
        _get_lists_clients_names()
        
    elif option == 'R':
        _get_lists_clients_names()
    elif option == 'U':
        client_name = get_client()
        client_name_update = input("Enter a client name that you want to change: ")
        update_client(client_name,client_name_update)
        _get_lists_clients_names()
    elif option == 'D':
        client_name = get_client()
    else:
        print("command invalid")