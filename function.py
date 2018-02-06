from PyQt5.QtWidgets import QApplication

from utils import formatJson


def getClip():
    board = QApplication.clipboard()
    return board.text()


def setClip(data):
    board = QApplication.clipboard()
    board.setText(data)


def JSON(command, success, failed):
    try:
        format = formatJson.formatJSON(getClip())
        setClip(format)
        success(format)
    except Exception as e:
        message = str(type(e)) + '\n' + str(e)
        failed(message)


def 二维码(command, success, failed):
    success('')


def U_L_Case(command, success, failed):
    try:
        c = getClip()
        import re
        p = re.compile('[a-z]')
        if len(p.findall(c)) > 0:
            result = c.upper()
        else:
            result = c.lower()
        setClip(result)
        success(result)
    except Exception as e:
        message = str(type(e)) + '\n' + str(e)
        failed(message)


def Encrypt(command, success, failed):
    import hashlib
    data = getClip().encode('utf-8')
    if len(data) <= 0:
        failed('no content !')
        return
    md5 = hashlib.md5(data)
    sha1 = hashlib.sha1(data)
    sha224 = hashlib.sha224(data)
    sha256 = hashlib.sha256(data)
    sha384 = hashlib.sha384(data)
    message = 'M D 5 : ' + md5.hexdigest() + '\n'
    message = message + 'S H A1: ' + sha1.hexdigest() + '\n'
    message = message + 'SHA224: ' + sha224.hexdigest() + '\n'
    message = message + 'SHA256: ' + sha256.hexdigest() + '\n'
    message = message + 'SHA384: ' + sha384.hexdigest() + '\n'
    message = message + '\n原文:\n-----\n' + data.decode()
    success(message)


def Trans(command, success, failed):
    import utils.translate.main_
    utils.translate.main_.translate(getClip(), success, failed)


def do(command, success, failed):
    funcName = command.replace(' ', '_')
    try:
        func = eval(funcName)
        func(command, success, failed)
    except Exception as e:
        message = str(type(e)) + '\n' + str(e)
        failed(message)
