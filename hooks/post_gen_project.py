import random
import os
import shutil


DIGITS = "".join([chr(number) for number in range(48, 58)])
UPPER_LETTERS = "".join([chr(number) for number in range(65, 91)])
LOWER_LETTERS = UPPER_LETTERS.lower()


def generate_value(
    length: int = 48,
    alphabet: str = DIGITS + UPPER_LETTERS + LOWER_LETTERS,
) -> str:
    return "".join([random.choice(alphabet) for _ in range(length)])


def set_variable(value, place, path):
    with open(path, mode="r+", encoding='utf-8') as file:
        info = file.read()
        index = info.index(place)
        info = list(info)
        info[index:index + len(place) + 1] = list(value)
        info = "".join(info)
        file.seek(0)
        file.write(info)


def main():
    if "{{cookiecutter.websockets}}" == "n":
        os.remove("./server/config/routing.py")
        shutil.rmtree("./server/apps/chat")
        shutil.rmtree("./server/apps/core/consumer")
        shutil.rmtree("./server/apps/core/middleware")
        shutil.rmtree("./server/apps/core/mixins")
        os.remove("./docs/ws.yml")

    if "{{cookiecutter.celery}}" == "n":
        os.remove("./server/config/celery.py")
        os.remove("./server/config/settings/celery.py")

    if "{{cookiecutter.autodeploy}}" == "n":
        os.remove("./.github/workflows/deploy.yml")

    set_variable(
        f"{generate_value()}/\n",
        "SET_DJANGO_ADMIN_URL",
        path="./.env",
    )
    set_variable(
        f"{generate_value()}\n",
        "SET_DJANGO_SECRET_KEY",
        path="./.env",
    )


if __name__ == "__main__":
    main()
