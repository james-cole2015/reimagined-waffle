FROM python:3.8-alpine

COPY monkeys_bot/12MonkeysBot.py /monkeys_bot/

COPY monkeys_bot/monkeys_creds.py /monkeys_bot/

COPY monkeys_bot/monkeys_episodes.py /monkeys_bot/

COPY requirements.txt /tmp

RUN pip3 install -r /tmp/requirements.txt

WORKDIR /monkeys_bot

CMD ["python3", "12MonkeysBot.py"]
