#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import os
import requests

class GerritAuth(object):
    def __init__(self, url, user, token):
        self.url = url
        self.user = user
        self.token = token

class GerritReview(object):
    def __init__(self, project, branch, change, revision):
        self.project = project
        self.branch = branch
        self.change = change
        if isinstance(revision, int):
            revision = str(revision)
        self.revision = revision

    def get_change(self):
        return '{}~{}~{}'.format(self.project, self.branch, self.change)

class GerritComment(object):
    def __init__(self, gerrit_auth, gerrit_review):
        self.gerrit = gerrit_auth
        self.review = gerrit_review

    def get_url(self):
        """
        Gerrit review url
        """
        return os.path.join(
            self.gerrit.url,
            'a',  # "a" is important -> authenticated
            'changes',
            self.review.get_change(),
            'revisions',
            self.review.revision,
            'review'
        )

    def post(self, review_input):
        """
        Take a ReviewInput object and post to gerrit review api
        """
        session = requests.Session()
        auth = requests.auth.HTTPBasicAuth(self.gerrit.user, self.gerrit.token)
        r = session.post(
            self.get_url(),
            auth=auth,
            json=review_input.json(),
            headers={'Content-Type': 'application/json;charset=UTF-8'}
        )
        return r
