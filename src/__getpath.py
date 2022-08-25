
# gives absolute path
# level 1 is current directory, "src"
# level 2 is root directory
# made bacause using `..` for path is dependant on where u run the file from
# e.g. running from `src` will find `tiles` but running from root, it will error
def getPath(level):
    return "/".join(__file__.split("/")[:-level]) + "/"