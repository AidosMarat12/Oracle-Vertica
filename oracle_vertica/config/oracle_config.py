import oracledb
import vertica_python

ORACLE_CONFIG = {
    'user': 'system',
    'password': 'your_password',
    'dsn': 'localhost:1521/FREEPDB1'
}

def test_oracle_config():
    try:
        connection = oracledb.connect(**ORACLE_CONFIG)
        cursor = connection.cursor()
        cursor.execute("SELECT count(*) FROM AIDOSMARAT.E_COMMERCE_BUSINESS")
        result = cursor.fetchall()
        print("Oracle connection successful", result)
    except Exception as e:
        print("Oracle connection failed", e)
    finally:
        try:
            cursor.close()
            connection.close()
        except:
            pass


VERTICA_CONFIG = {
    'host': 'localhost',
    'port': 5433,
    'user': 'dbadmin',
    'password': 'vertica123',
    'database': 'verticadb'
}


def test_vertica_config():
    print("Testing Vertica...")
    try:
        conn = vertica_python.connect(**VERTICA_CONFIG)
        cursor = conn.cursor()
        cursor.execute("SELECT 'Vertica OK'")
        print("Vertica:", cursor.fetchone())
    except Exception as e:
        print("Vertica failed:", e)
    finally:
        try:
            cursor.close()
            conn.close()
        except:
            pass

if __name__ == "__main__":
    test_oracle_config()
    test_vertica_config()
