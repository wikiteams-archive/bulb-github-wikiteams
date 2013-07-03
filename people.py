'''
Created on 03-07-2013
'''
from bulbs.model import Node, Relationship
from bulbs.property import String, Integer, DateTime
from bulbs.utils import current_datetime

class Person(Node):

    element_type = "person"

    name = String(nullable=False)
    age = Integer()


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
