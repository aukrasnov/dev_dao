import os
import statistics
import pymysql
import yaml


def exists(fpath: str)->int:
    return 1 if os.path.isfile(fpath) else -1


def median(table, colomn):
    # Connect to the database
    f = open('/Users/aleksandr/PycharmProjects/anchor-etl/.config.yml', 'r')
    config = yaml.load(f)
    f.close()
    connection = pymysql.connect(user=config["mysql"]['sections'][0]["user"],
                                 password=config["mysql"]['sections'][0]["pass"],
                                 host=config["mysql"]['sections'][0]["host"],
                                 db=config["mysql"]['sections'][0]["db"],
                                 charset='cp1251',
                                 cursorclass=pymysql.cursors.DictCursor)
    cur = connection.cursor()
    sql = 'SELECT DISTINCT {} FROM repetitors.{}'.format(colomn, table)
    cur.execute(sql)
    sql_result = cur.fetchall()
    result = [f['{}'.format(colomn)] for f in sql_result]
    return statistics.median(result)






