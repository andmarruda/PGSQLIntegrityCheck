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
errors = cr.searchNotMatchRows()
print(f'Missing rows in table or materialized view at right database: {errors}')
