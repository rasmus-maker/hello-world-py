def greet(name: str, shout: bool = False) -> str:
    """Return a friendly greeting for the given name."""
    if not name:
        raise ValueError("name must not be empty")
    message = f"Hello, {name}!"
    return message.upper() if shout else message


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Print a friendly greeting.")
    parser.add_argument("name", nargs="?", default="world", help="Who to greet")
    parser.add_argument("--shout", action="store_true", help="SHOUT the greeting")
    args = parser.parse_args()

    print(greet(args.name, shout=args.shout))
