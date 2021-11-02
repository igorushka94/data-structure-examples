d = {x: x for x in range(1, 20)}

# Преобразовать в существующем словаре и перевести все ключи в нижний регистр
r1 = {'IOS': '15.4',
      'IP': '10.255.0.1',
      'hostname': 'london_r1',
      'location': '21 New Globe Walk',
      'model': '4451',
      'vendor': 'Cisco'
      }

lower_r1 = {key.lower(): value for key, value in r1.items()}

# dict comprehensions по вложенным словарям
london_co = {
    'r1': {
        'hostname': 'london_r1',
        'location': '21 New Globe Walk',
        'vendor': 'Cisco',
        'model': '4451',
        'IOS': '15.4',
        'IP': '10.255.0.1'
    },
    'r2': {
        'hostname': 'london_r2',
        'location': '21 New Globe Walk',
        'vendor': 'Cisco',
        'model': '4451',
        'IOS': '15.4',
        'IP': '10.255.0.2'
    },
    'sw1': {
        'hostname': 'london_sw1',
        'location': '21 New Globe Walk',
        'vendor': 'Cisco',
        'model': '3850',
        'IOS': '3.6.XE',
        'IP': '10.255.0.101'
    }
}
result = {device: {key.lower(): value for key, value in params.items()} for device, params in london_co.items()}
print(result)
