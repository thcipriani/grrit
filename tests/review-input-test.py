#!/usr/bin/env python3
#-*- coding: utf-8 -*-

from gerritcommentor import review

import json

def test_revew_input_json():
    ri = review.ReviewInput('hi')
    assert('{"message": "hi"}' == json.dumps(ri.json()))

def test_revew_input_with_file_comment_json():
    ri = review.ReviewInput('hi')
    ri.add_comment('/srv/foo', 'bar')
    expect = ('{"message": "hi", "comments": '
              '{"/srv/foo": [{"message": "bar"}]}}')
    assert(expect == json.dumps(ri.json()))

def test_revew_input_with_file_comment_and_line_json():
    ri = review.ReviewInput('hi')
    ri.add_comment('/srv/foo', 'bar', 29)
    expect = ('{"message": "hi", "comments": '
              '{"/srv/foo": [{"line": 29, "message": "bar"}]}}')
    assert(expect == json.dumps(ri.json()))

def test_revew_input_with_file_comment_and_range_json():
    ri = review.ReviewInput('hi')
    ri.add_comment('/srv/foo', 'bar', 29, 32)
    expect = ('{"message": "hi", "comments": '
              '{"/srv/foo": [{"range": {"start_line": 29, "end_line": 32}, '
              '"message": "bar"}]}}')
    assert(expect == json.dumps(ri.json()))
