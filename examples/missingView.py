from integrityCheck import integrityCheck
db_left = {
    'host': '',
    'port': 5432,
    'user': '',
    'passw': '',
    'dbname': ''
}

db_right = {
    'host': '',
    'port': 5432,
    'user': '',
    'passw': '',
    'dbname': ''
}

cr = integrityCheck(db_left, db_right)
for mv in cr.missingView('right'): #if want to check at the left replace word right to left
    print(f'Missing view at right database: {mv}')
