from __future__ import print_function
from cloudmesh.shell.command import command
from cloudmesh.shell.command import PluginCommand
from cloudmesh.twitter.twitter import Twitter
from cloudmesh.common.console import Console
from cloudmesh.common.util import path_expand
from pprint import pprint
from cloudmesh.common.debug import VERBOSE
from fastparquet import ParquetFile
import sys
import json
import tweepy

class StreamListener(tweepy.StreamListener):
    def on_status(self, status):
        print(status.id_str)

        isretweet = False

        if hasattr(status, "retweeted_status"):
            isretweet = True
            
        # changes go here
        # more information with Twitter API access


    def on_error(self, status_code):
        print('Error, exiting')
        sys.exit()

class TwitterCommand(PluginCommand):

    # noinspection PyUnusedLocal
    @command
    def do_twitter(self, args, arguments):
        """
        ::

          Usage:
            cms twitter register [REGISTER]
            cms twitter stream start [--file=FILE]
                                     [--attributes=ATTRIBUTES]
                                     [--filter=FILTER]

          Arguments:
            REGISTER  a file name with the registration information
                      [default: ~/.cloudmesh/twitter.json]
            FILE      The file to which the stream is redirected.
                      By default this is stdout
                      [default: stdout]

          Options:
              -f      specify the file

          Descriptions:

            filter is not really that important, attributes are

            cms twitter register [FILE]

              Registers the twitter API with data stored in the file.
              TODO: find out which data is used and which format it has.
                    Use the format that twitter offers

            cms twitter stream start [--file=FILE]
                                     [--attributes=ATTRIBUTES]
                                     [--filter=FILTER]

              Starts the twitter stream and redirects it to the given file. If
              stdout is specified it just prints it. Twitter returns a number
              of attributes in a tweet. You can specify a comma separated list
              of attributes that are stored instead of all attributes. If you
              do not specify attributes, all attributes will be returned.

              The filter is currently unimportant, but we want to be able to
              identify in future just some tweets that match this pattern.

        """

        VERBOSE(arguments)

        file = arguments["--file"]
        attributes = arguments["attributes"]
        filter = arguments["filter"]
        register = arguments.REGISTER

        with open('~/.cloudmesh/twitter.json') as f:
            data = json.load(f)

        consumer_key = data.consumer_key
        consumer_secret = data.consumer_secret
        access_key = data.access_key
        access_secret = data.access_secret


        if arguments.register:

            twitter = Twitter()
            twitter.register(file=register)
            #Console.error("Not implemented")
            #raise NotImplementedError
            auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
            auth.set_access_token(access_key, access_secret)
            api = tweepy.API(auth)


        elif arguments.stream:

            twitter = Twitter()
            twitter.stream(
                   file=file,
                   attributes=attributes,
                   filter=filter)

            auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
            auth.set_access_token(access_key, access_secret)
            api = tweepy.API(auth)

            streamListener = StreamListener()
            stream = tweepy.Stream(auth = api.auth, listener=streamListener, tweet_mode='extended')

            tags = filter
            stream.filter(track=tags)

        return ""
