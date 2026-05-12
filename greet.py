def greet(name: str) -> str:
    """Return a friendly greeting for the given name."""
    if not name:
        raise ValueError("name must not be empty")
    return f"Hello, {name}!"


if __name__ == "__main__":
    import sys
    who = sys.argv[1] if len(sys.argv) > 1 else "world"
    print(greet(who))
