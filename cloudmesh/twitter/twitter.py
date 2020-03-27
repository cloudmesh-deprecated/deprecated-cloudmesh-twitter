from cloudmesh.common.util import path_expand
from cloudmesh.common.util import banner

import sys
from cloudmesh.common.console import Console

class Twitter:

    """
    twitter = Twitter()
    twitter.register("twitter.json")
    output = twitter.stream(file="stdout")

    """
    def __init__(self):
        pass

    def register(self, file=None):
        Console.error("Not implemented")
        raise NotImplementedError

    def stream(self,
               file="stdout",
               attributes=None,
               filter=None):
        """
        Stream the twitter data

        :param file: the file
        :param attributes: list of attributes
        :param filter: is a function operating on a tweet dict
        :return:
        """
        banner(f"Streaming: file={file}")
        print (f"    attributes: {attributes}")
        print (f"    file      : {file}")
        print ()
        if file == "stdout":
            output = sys.stdout
        else:
            output = open(path_expand(file), "w")

        with output:
            print("hallo")

        Console.error("Not implemented")
        raise NotImplementedError

