import requests


def post(url, data, json, **kwargs):
    return requests.post(url, data=data, json=json, **kwargs)


def put(url, data, **kwargs):
    return requests.put(url, data=data, **kwargs)


def get(url, params, **kwargs):
    return requests.get(url, params=params, **kwargs)


def delete(url, **kwargs):
    return requests.delete(url, **kwargs)


def patch(url, data, **kwargs):
    return requests.patch(url, data=data, **kwargs)


def head(url, **kwargs):
    return requests.head(url, **kwargs)
