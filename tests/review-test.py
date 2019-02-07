#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import grrit.review

import json

def test_revew_input_json():
    ri = grrit.review.Comment().say('hi')
    assert('{"message": "hi"}' == json.dumps(ri.json()))

def test_revew_input_with_file_comment_json():
    ri = grrit.review.Comment('hi')
    fc = grrit.review.FileComment('/srv/foo').say('bar')
    ri.add(fc)
    expect = ('{"message": "hi", "comments": '
              '{"/srv/foo": [{"message": "bar"}]}}')
    assert(expect == json.dumps(ri.json()))

def test_revew_input_with_file_comment_and_line_json():
    ri = grrit.review.Comment('hi')
    fc = grrit.review.FileComment('/srv/foo').line(29).say('bar')
    ri.add(fc)
    expect = ('{"message": "hi", "comments": '
              '{"/srv/foo": [{"line": 29, "message": "bar"}]}}')
    assert(expect == json.dumps(ri.json()))

def test_revew_input_with_file_comment_and_range_json():
    ri = grrit.review.Comment()
    fc = grrit.review.FileComment('/srv/foo').start(29).end(32).say('bar')
    ri.add(fc)
    expect = ('{"comments": '
              '{"/srv/foo": [{"range": {"start_line": 29, "end_line": 32}, '
              '"message": "bar"}]}}')
    assert(expect == json.dumps(ri.json()))

def test_non_fancy_syntax():
    ri = grrit.review.Comment('test')
    comments = [
        grrit.review.FileComment('/srv/bar', 'baz', 10, 29),
        grrit.review.FileComment('/srv/foo', 'hello world', 29),
        grrit.review.FileComment('/srv/bar', 'bar', 1),
    ]
    ri.add(comments)
    expect = ('{'
            '"message": "test", '
            '"comments": {'
                '"/srv/bar": ['
                    '{"range": {"start_line": 10, "end_line": 29}, '
                    '"message": "baz"}, '
                    '{"line": 1, "message": "bar"}'
                '], '
                '"/srv/foo": ['
                    '{"line": 29, "message": "hello world"}'
                ']}}')
    assert(expect == json.dumps(ri.json()))
