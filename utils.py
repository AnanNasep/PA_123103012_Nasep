def log_to_file(message, filename="log.txt"):
    with open(filename, "a") as f:
        f.write(message + "\n")
