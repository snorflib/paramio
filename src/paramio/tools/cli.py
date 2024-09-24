import sys


def get_flag_value(flag: str) -> str | None:
    for idx, arg in enumerate(sys.argv):
        if arg.startswith(f"{flag}="):
            return arg.split("=", 1)[1]
        elif arg != flag:
            continue
        elif idx + 1 >= len(sys.argv):
            return None
        return str(sys.argv[idx + 1])
    return None
