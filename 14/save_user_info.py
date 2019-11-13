from configparser import ConfigParser


class Database:

    def __init__(self, filename):
        self._filename = filename
        config_parser = ConfigParser()
        config_parser.read(filename, 'UTF-8')
        if not config_parser.has_section('SECTION'):
            config_parser.add_section('SECTION')
        self._properties = config_parser

    def set(self, key, value):
        self._properties.set('SECTION', key, value)

    def get(self, key):
        self._properties.get('SECTION', key)

    def update(self):
        with open(self._filename, 'w') as file:
            self._properties.write(file)

    @property
    def properties(self):
        return self._properties


class AddressFile:

    def __init__(self, filename):
        self._database = Database(filename)

    # @property
    # def database(self):
    #     return self._database

    def set(self, key, value):
      self._database.set(key, value)
    
    def update(self):
      self._database.update()


    def names(self):
        return self._database.properties.items('SECTION')
