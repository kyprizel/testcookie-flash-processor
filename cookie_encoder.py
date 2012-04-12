def encode_cookie(cookie_value):
    key = 42
    res = ''
    for x in cookie_value:
        res += chr(ord(x) ^ key)
    return res
