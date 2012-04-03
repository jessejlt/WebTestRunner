import logging

default_formatter = logging.Formatter('%(asctime)s - %(module)s::%(funcName)s - %(levelname)s - %(message)s', '%m-%d %H:%M')

console_handler = logging.StreamHandler()
console_handler.setFormatter(default_formatter)

root = logging.getLogger()
root.addHandler(console_handler)
root.setLevel(logging.DEBUG)
