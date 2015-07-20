#!/usr/bin/env python

import driller.config as config
import os
import sys

def check_exec(d, p):
    path = os.path.join(d, p)
    return not os.path.isdir(path) and os.access(path, os.X_OK)

def main(argv):

    if len(argv) < 2:
        print "%s <n-workers>" % argv[0]
        return 1

    n = argv[1]

    # verify that config.QEMU_DIR is sane
    if not os.path.isdir(config.QEMU_DIR):
        print "the qemu directory specified in the config is not a directory"
        return 1

    if "driller-qemu-cgc" not in os.listdir(config.QEMU_DIR):
        print "the qemu directory does not contain any file by the name of 'driller-qemu-cgc'"
        return 1

    # verify that config.BINARY_DIR contains some binaries
    if not os.path.isdir(config.BINARY_DIR):
        print "the binary directory specified in the config is not a directory"
        return 1

    if not any(filter(lambda x: check_exec(config.BINARY_DIR, x), os.listdir(config.BINARY_DIR))):
        print "no binary files detected in binary directory specified, failing fast"
        return 1

    args = ["celery", "-A", "driller.tasks", "worker", "-c", n, "--loglevel=info"]

    os.execvp(args[0], args)

if __name__ == "__main__":
    sys.exit(main(sys.argv))