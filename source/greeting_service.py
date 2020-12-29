import re


class GreetingService:
    def say_hello(self, user_name):
        if user_name is None:
            return "Hello Stranger"
        else:
            greetings = re.sub(r'((?<=[a-z])[A-Z]|[A-Z](?=[a-z]))', r' \1', user_name).strip()
            return 'Hello' + ' ' + greetings
