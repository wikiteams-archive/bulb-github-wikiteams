'''
Created on 04-07-2013
'''
from bulbs.model import Node, Relationship
from bulbs.property import String, Integer, DateTime, None, List
from bulbs.utils import current_datetime
class Gist(Node):

    element_type = "gist"

    user = String(nullable=False)
    url = String(nullable=True)
    id = String(nullable=True)
    description = String(nullable=True)
    public = String(nullable=True)
    user = List(nullable=True)
    files = List(nullable=True)
    
    comments = String(nullable=True)
    comments_url = String(nullable=True)
    html_url = String(nullable=True)
    git_pull_url = String(nullable=True)
    git_push_url = String(nullable=True)
    created_at = String(nullable=True)
  
'''
@author: s4268
'''
