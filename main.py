import configparser

cfg = configparser.ConfigParser()
cfg.read('config.ini')
print(cfg['GOOGLE SHEETS API']['client_id'])