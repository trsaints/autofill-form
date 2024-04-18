import argparse


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--pid', required=True, type=str)

    args = parser.parse_args()
    pid = args.pid

    return [pid]