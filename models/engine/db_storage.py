#!/usr/bin/python3
import MySQLdb
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models.base_model import BaseModel, Base
# from models.city import City
# from models.place import Place
# from models.user import User
# from models.amenity import Amenity
# from models.review import Review


class DBStorage:
    """Database storage engine"""
    __engine = None
    __session = None

    def __init__(self):
        """constructor/initializer"""
        HBNB_MYSQL_USER = getenv("HBNB_MYSQL_USER")
        HBNB_MYSQL_PWD = getenv("HBNB_MYSQL_PWD")
        HBNB_MYSQL_HOST = getenv("HBNB_MYSQL_HOST")
        HBNB_MYSQL_DB = getenv("HBNB_MYSQL_DB")
        conn = "mysql+mysqldb://{}:{}@{}/{}".format(HBNB_MYSQL_USER,
                                                    HBNB_MYSQL_PWD,
                                                    HBNB_MYSQL_HOST,
                                                    HBNB_MYSQL_DB)
        self.__engine = create_engine(conn, pool_pre_ping=True)
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)
        # session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        # self.__session = scoped_session(session_factory)

    def all(self, cls=None):
        """Gets all objects, of a class if specified, stored in the database"""
        from models.base_model import BaseModel
        from models.city import City
        from models.state import State
        from models.place import Place
        from models.user import User
        from models.amenity import Amenity
        from models.review import Review
        if cls is None:
            cls_list = [State, City, User, Amenity, Place, Review]
        else:
            cls_list = [cls]
        obj_dict = {}
        for clas in cls_list:
            objects = self.__session.query(clas).all()
            for obj in objects:
                key = "{}.{}".format(clas.__name__, obj.id)
                obj_dict[key] = obj
        return obj_dict

    def new(self, obj):
        """add object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commits all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete obj from the current database session """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """create all tables in the database """
        from models.base_model import BaseModel
        from models.city import City
        from models.state import State
        from models.place import Place
        from models.user import User
        from models.amenity import Amenity
        from models.review import Review
        Base.metadata.create_all(self.__engine)
        session_db = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_db)
        self.__session = Session()
