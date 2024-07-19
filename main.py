from user_configuration import get_user_input
from utils_printer import print_welcome_screen, print_cookie


def main():
    """Main function for running the code."""
    print_welcome_screen()
    user_configuration = get_user_input()
    if not user_configuration:
        return
    print("Now let's practice!")
    print_cookie()


if __name__ == '__main__':
    main()