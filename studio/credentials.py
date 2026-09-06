"""Windows current-user DPAPI. Never fall back to plaintext persistence."""
import base64
import ctypes
import os
from ctypes import wintypes


class Blob(ctypes.Structure):
    _fields_ = [('size', wintypes.DWORD), ('data', ctypes.POINTER(ctypes.c_char))]


def transform(value, decrypt=False):
    if os.name != 'nt':
        raise ValueError('Armazenamento protegido requer Windows. Use variáveis de ambiente.')
    buffer = ctypes.create_string_buffer(value)
    source = Blob(len(value), ctypes.cast(buffer, ctypes.POINTER(ctypes.c_char)))
    output = Blob()
    crypt = ctypes.WinDLL('crypt32', use_last_error=True)
    kernel = ctypes.WinDLL('kernel32', use_last_error=True)
    function = crypt.CryptUnprotectData if decrypt else crypt.CryptProtectData
    function.restype = wintypes.BOOL
    if not function(ctypes.byref(source), None, None, None, None, 1, ctypes.byref(output)):
        raise ValueError('Não foi possível acessar as credenciais protegidas deste usuário Windows.')
    try:
        return ctypes.string_at(output.data, output.size)
    finally:
        kernel.LocalFree.argtypes = [ctypes.c_void_p]
        kernel.LocalFree(output.data)


def protect(text):
    return base64.b64encode(transform(text.encode('utf-8'))).decode('ascii')


def unprotect(text):
    return transform(base64.b64decode(text), decrypt=True).decode('utf-8')
