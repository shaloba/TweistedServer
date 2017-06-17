__author__ = "Shlomy Balulu"

from argparse import ArgumentParser
import sys

class ArgsParser():

    def __init__(self):
        self.__args = self.parse()

    def parse(self):
        """
        extracting user input using python argparse lib
        :return: args object (ArgumentParser instance)
        """
        try:
            parser = ArgumentParser()
            parser.add_argument('--add', nargs=2)
            parser.add_argument('--prime', nargs=1)
            args = parser.parse_args()
        except Exception as err:
            print err
            return None

        return self.analyze_args(args)

    def analyze_args(self, args):
        """
        convert ArgumentParser to dictionary in order to analyzed by the server.
        :param args:argparse object containing the user input
        :return: dictionary with action and parameters
        """
        args_obj = args.__dict__
        if args_obj.get('add'):
            action = 'bc'
            params = args_obj['add']

        elif args_obj.get('prime'):
            action = 'prime'
            params = args_obj['prime']
        else:
            print "Invalid Arguments..."
            sys.exit(0)

        params_check = self.validate_params(params)
        if params_check is True:
            parsed_args = dict(action=action,
                               params=map(int, params))
            return parsed_args

    def validate_params(self, params):
        try:
            map(int, params)
            return True
        except ValueError as err:
            print "Invalid Arguments, Error: " + str(err)
            return False


    def get_args(self):
        return self.__args
