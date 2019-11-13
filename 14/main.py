#from save_user_info import Database
from save_user_info import AddressFile


def execute():
    file = AddressFile('address.txt')
#     file.database.set('Yuki', 'hyuki@example.com')
#     file.database.set('Tomura', 'tomura@example.com')
#     file.database.set('Hanako', 'hanako@example.com')
#     file.database.update()
    file.set('Yuki', 'hyuki@example.com')
    file.set('Tomura', 'tomura@example.com')
    file.set('Hanako', 'hanako@example.com')
    file.update()

    for name, email in file.names():
        print('name={}, email={}'.format(name, email))


if __name__ == "__main__":
    execute()
