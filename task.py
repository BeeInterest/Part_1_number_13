import secrets
import string
import random

class GeneratePassword:
    def __init__(self,length_password):
        alphabet = string.ascii_letters + string.digits + string.punctuation
        length_password = length_password
