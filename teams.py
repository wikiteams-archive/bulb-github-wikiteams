'''
Created on 03-07-2013
'''
from bulbs.model import Node, Relationship
from bulbs.property import String, Integer, DateTime, None
from bulbs.utils import current_datetime

class Repository(Node):

    element_type = "team"

    
    repository_url = String(nullable=False)
    repository_has_downloads = None(nullable=False)
    repository_created_at = String(nullable=False)
    repository_has_issues = None(nullable=False)
    repository_description = String(nullable=False)
    repository_forks = Integer(nullable=False)
    repository_fork  = String(nullable=False)
    repository_has_wiki  = None(nullable=False)
    repository_homepage = String(nullable=False)
    repository_size = Integer(nullable=False)
    repository_private = String(nullable=False)
    repository_name  = String(nullable=False)
    repository_owner = String(nullable=False)
    repository_open_issues = Integer(nullable=False)
    repository_watchers = Integer(nullable=False)
    repository_pushed_at = String(nullable=False)
    repository_language = String(nullable=False)
    repository_organization = String(nullable=False)
    repository_integrate_branch = String(nullable=False)
    repository_master_branch = String(nullable=False)
'''
@author: s4268
'''
