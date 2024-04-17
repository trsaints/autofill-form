def parse_commands(file_path):
    with open(file_path, 'r') as file:
        return [line.strip().split(',') for line in file.readlines() if line.strip()]