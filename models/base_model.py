#!/usr/bin/python3
#Defining the Base model class

import uuid
import datetime


class BaseModel:
    def __init__(self, *args, **kwargs):
        """ Defines common attributes:
            id: string - UUID assigned at instance creation.
            created_at: datetime - set to current datetime at instance creation.
            updated_at: datetime - set to current datetime at instance creation, updated on object change. """

        if kwargs:
            for key,value in kwargs.items():
                if key != "__class__":
                    if key=="created_at" or key=="updated_at":
                        setattr(self,key,datetime.datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                    else: 
                        setattr(self,key,value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()


    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
    

    def save(self):
        self.updated_at = datetime.datetime.now()

    
    def to_dict(self):
        """ Return a dictionary representing the class instance. """

        my_dict = self.__dict__.copy()
        my_dict["__class__"] = self.__class__.__name__
        my_dict["created_at"] = datetime.datetime.isoformat(my_dict["created_at"])
        my_dict["updated_at"] = datetime.datetime.isoformat(my_dict["updated_at"])
        return my_dict






