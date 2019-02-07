#!/usr/bin/env python3
#-*- coding: utf-8 -*-
"""
gerritcommentor.gerrit.api
~~~~~~~~~~~~~~~~~~~

"""

import os
import requests

class Auth(object):
    """
    Simple object to hold auth info
    """
    def __init__(self, url, user, token):
        self.url = url
        self.user = user
        self.token = token

class Revision(object):
    """
    Store info for gerrit revision
    """
    def __init__(self, project, branch, change, revision):
        self.project = project
        self.branch = branch
        self.change = change
        if isinstance(revision, int):
            revision = str(revision)
        self.number = revision

    def get_change(self):
        return '{}~{}~{}'.format(self.project, self.branch, self.change)

class Review(object):
    """
    Actual api for gerrit review
    """
    def __init__(self, gerrit_auth, gerrit_revision):
        self.gerrit = gerrit_auth
        self.revision = gerrit_revision

    def get_url(self):
        """
        Gerrit review url
        """
        return os.path.join(
            self.gerrit.url,
            'a',  # "a" is important -> authenticated
            'changes',
            self.revision.get_change(),
            'revisions',
            self.revision.number,
            'review'
        )

    def post(self, review_input):
        """
        Take a ReviewInput object and post to gerrit review api
        """
        auth = requests.auth.HTTPBasicAuth(self.gerrit.user, self.gerrit.token)
        return requests.post(
            self.get_url(),
            auth=auth,
            json=review_input.json(),
            headers={'Content-Type': 'application/json;charset=UTF-8'}
        )
