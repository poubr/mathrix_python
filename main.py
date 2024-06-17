from input_handler import get_user_input


def main():
    """Main function for running the code."""
    user_configuration = get_user_input()
    if not user_configuration:
        return
    print(user_configuration)


if __name__ == '__main__':
    main()

