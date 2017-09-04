from RLE import encode,decode

def test_encode():
    assert encode('kkkkkbbbb') == '5k4b'

def test_encode_empty():
    assert encode('') == ''

def test_encode_emoji():
    assert encode('😇') == '1😇'
    assert encode('😇😇😇😇😇') == '5😇'

def test_decode():
    assert decode('4k') == 'kkkk'
