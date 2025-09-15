import os

secret_value = os.getenv(key="MY_SECRET", default="No secret found")
print("Secret value is {0}".format(secret_value))
