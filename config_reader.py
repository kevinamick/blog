import configparser
import os

Config = configparser.ConfigParser()
Config.read(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'config.ini'))


def config_reader(section):
    dict1 = {}
    options = Config.options(section)
    for option in options:
        try:
            dict1[option] = Config.get(section, option)
            if dict1[option] == -1:
                print("skip: %s" % option)
        except:
            print("exception on %s!" % option)
            dict1[option] = None
    return dict1
