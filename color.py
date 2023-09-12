import colorama

# Some ANSI escape sequneces for colours and effects
BLACK = '\u001b[30m'
RED = '\u001b[31m'
GREEN = '\u001b[32m'
YELLOW = '\u001b[33m'
BLUE = '\u001b[34m'
MAGENTA = '\u001b[35m'
CYAN = '\u001b[36m'
WHITE = '\u001b[37m'
RESET = '\u001b[0m'

BOLD = '\u001b[1m'
UNDERLINE = '\u001b[4m'
REVERSE = '\u001b[7m'

# print(RED, "hello")


def colour_print(text: str, *effect: str) -> None:
    """
    Print `text` using the ANSI sequence to change colour, etc

    :param text: The text to print
    :param effect:The effect we want. One of the constant
            defined at the start of this module.
    """

    effect_string= "".join(effect)
    out_string = "{} {}, {}".format(effect_string, text, RESET)
    return out_string


colorama.init()


if __name__ == "__main_in__":
    print(colour_print("Hello World", RED))
    print("This should be in the default terminal color")
    colour_print("Hello World Blue", BLUE)
    colour_print("Hello World in bold bule", BLUE, BOLD)
    colour_print("Hello World YELLOW", YELLOW)
    colour_print("Hello World", UNDERLINE)
    colour_print("Hello World UNDERLINE", REVERSE)
    colour_print("Hello World BLACK", BLACK)
    colour_print("Hello World UNDERLINE BLUE BOLD reverse",BLUE, BOLD, REVERSE, UNDERLINE)
    colour_print("Hello World GREEN", GREEN)
    colour_print("Hello World", RED)
    colorama.deinit()