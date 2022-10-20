import psycopg2

class sqls:
    def __init__(self, host, port, user, passw, dbname):
        self.__conn = psycopg2.connect(host=host, database=dbname, port=port, user=user,
                                       password=passw)
    def getAllPGClass(self, relkind):
        cur = self.__conn.cursor()
        cur.execute("SELECT pn.nspname || '.' || pc.relname as obj FROM pg_class pc JOIN pg_namespace pn ON pn.oid=pc.relnamespace WHERE pc.relkind IN ("+ ('%s, ' * len(relkind)).rstrip(', ') +") AND NOT pn.nspname IN('pg_catalog', 'information_schema', 'pg_toast') AND relpersistence='p'", relkind)
        return list(map(lambda cls: cls[0], cur.fetchall()))

    def pgClassWithRowCount(self):
        allcls = self.getAllPGClass(['r', 'm'])
        dict = {}
        for cls in allcls:
            try:
                cur = self.__conn.cursor()
                cur.execute('SELECT COUNT(*) FROM ' + cls)
                dict[cls] = cur.fetchall()[0][0]
            except:
                dict[cls] = 0
        return dict

    def __del__(self):
        try:
            self.__conn.close()
        except:
            print('Não conectado!')
