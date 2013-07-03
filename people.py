'''
Created on 03-07-2013
'''
from bulbs.model import Node, Relationship
from bulbs.property import String, Integer, DateTime
from bulbs.utils import current_datetime

class Person(Node):

    element_type = "person"

    name = String(nullable=True)

class User(Person):
    
    element_type = "user"
    
    actor_attributes_gravatar_id = String(nullable=True)
    actor_attributes_type = String(nullable=True)
    actor_attributes_login = String(nullable=True)
    actor_attributes_name = String(nullable=True)
    actor_attributes_company = String(nullable=True)
    actor_attributes_location = String(nullable=True)
    actor_attributes_blog = String(nullable=True)
    actor_attributes_email = String(nullable=True)

class Knows(Relationship):

    label = "knows"

    created = DateTime(default=current_datetime, nullable=False)
    
class Follows(Relationship):

    label = "follows"

    created = DateTime(default=current_datetime, nullable=False)
    
class Watches(Relationship):

    label = "watches"

    created = DateTime(default=current_datetime, nullable=False)
'''
@author: s4268
'''
