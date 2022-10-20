import psycopg2

class sqls:
    __filterNameSpace = "NOT pn.nspname IN('pg_catalog', 'information_schema', 'pg_toast')"
    __filterClass = "relpersistence='p'"
    __pgClass = """
        SELECT 
            pn.nspname || '.' || pc.relname as obj 
        FROM 
            pg_class pc 
            JOIN pg_namespace pn ON pn.oid=pc.relnamespace 
        WHERE pc.relkind IN ({}) AND {} AND {}
    """
    __pgAttribute = """
        SELECT
            pn.nspname, pc.relname, pa.attname, pa.attlen, pa.attnum, 
            pa.attndims, pa.attcacheoff, pa.atttypmod, pa.attstorage, pa.attcompression,
            pa.attnotnull, pa.atthasdef, pa.atthasmissing, pa.attidentity, pa.attgenerated,
            
            pt.typname, pt.typlen, pt.typbyval, pt.typtype, pt.typcategory 
        FROM
            pg_attribute pa
            JOIN pg_class pc ON pc.oid=pa.attrelid
            JOIN pg_namespace pn ON pn.oid=pc.relnamespace
            JOIN pg_type pt ON pt.oid=pa.atttypid
        WHERE
            pa.attnum > 0 AND NOT attisdropped AND pn.nspname || '.' || pc.relname = %s
    """

    def __init__(self, host, port, user, passw, dbname):
        self.__conn = psycopg2.connect(host=host, database=dbname, port=port, user=user,
                                       password=passw)
    def getAllPGClass(self, relkind):
        cur = self.__conn.cursor()
        cls = type(self)
        cur.execute(cls.__pgClass.format(('%s, ' * len(relkind)).rstrip(', '), cls.__filterNameSpace, cls.__filterClass), relkind)
        return list(map(lambda pgcls: pgcls[0], cur.fetchall()))

    def getAllAttribute(self, relname):
        cur = self.__conn.cursor()
        cls = type(self)
        cur.execute(cls.__pgAttribute, [relname])
        return cur.fetchall()

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
