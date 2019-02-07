#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import grrit.api

def test_gerrit_change():
    rev = grrit.api.Revision(
        project='sshecret',
        branch='master',
        change='Icc41124d9f608c04ada4552c42620f76b436a1bb',
        revision=1
    )
    assert(
        rev.get_change() ==
        'sshecret~master~Icc41124d9f608c04ada4552c42620f76b436a1bb'
    )

def test_gerrit_url():
    auth = grrit.api.Auth(
        url='http://gerrit.tylercipriani.com:8080',
        user='thcipriani',
        token='notmyrealpw'
    )
    rev = grrit.api.Revision(
        project='sshecret',
        branch='master',
        change='Icc41124d9f608c04ada4552c42620f76b436a1bb',
        revision=1
    )

    comment = grrit.api.Review(auth, rev)
    assert(
        comment.get_url() ==
        'http://gerrit.tylercipriani.com:8080/a/changes/sshecret~master~Icc411'
        '24d9f608c04ada4552c42620f76b436a1bb/revisions/1/review'
    )
