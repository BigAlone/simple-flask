def get_database_url(dbinfo):
    user = dbinfo.get("USER") or "root"
    password = dbinfo.get("PASSWORD") or "zuber"
    host = dbinfo.get("HOST") or "localhost"
    port = dbinfo.get("PORT") or "3306"
    name = dbinfo.get("NAME") or "zuber_log"
    db = dbinfo.get("DB") or "mysql"
    driver = dbinfo.get("DRIVER") or "pymysql"
    return "{}+{}://{}:{}@{}:{}/{}".format(db, driver, user, password, host, port, name)


# 全局环境配置
class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = "iamholly"
    SESSION_TYPE = "filesystem"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


# 开发环境配置N
class DevelopConfig(Config):
    DEBUG = True

    DATABASE = {
        "USER": "root",
        "PASSWORD": "zuber",
        "HOST": "localhost",
        "PORT": "3306",
        "NAME": "zuber_log",
        "DB": "mysql",
        "DRIVER": "pymysql"
    }
    SQLALCHEMY_DATABASE_URI = get_database_url(DATABASE)


# 测试环境配置
class TestingConfig(Config):
    TESTING = True

    DATABASE = {
        "USER": "root",
        "PASSWORD": "zuber",
        "HOST": "localhost",
        "PORT": "3306",
        "NAME": "zuber_test",
        "DB": "mysql",
        "DRIVER": "pymysql"
    }
    SQLALCHEMY_DATABASE_URI = get_database_url(DATABASE)


# 演示环境配置
class DemoConfig(Config):
    DEBUG = True

    DATABASE = {
        "USER": "root",
        "PASSWORD": "zuber",
        "HOST": "localhost",
        "PORT": "3306",
        "NAME": "zuber_log",
        "DB": "mysql",
        "DRIVER": "pymysql"
    }
    SQLALCHEMY_DATABASE_URI = get_database_url(DATABASE)


# 线上环境-生产环境配置
class ProductConfig(Config):
    DATABASE = {
        "USER": "root",
        "PASSWORD": "zuber",
        "HOST": "localhost",
        "PORT": "3306",
        "NAME": "zuber_log",
        "DB": "mysql",
        "DRIVER": "pymysql"
    }
    SQLALCHEMY_DATABASE_URI = get_database_url(DATABASE)


config = {
    "develop": DevelopConfig,
    "testing": TestingConfig,
    "demo": DemoConfig,
    "product": ProductConfig,
    "default": DevelopConfig
}
