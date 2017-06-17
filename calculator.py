__author__ = "Shlomy Balulu"

import os
import config
import json

class Calculator():

    def calculate(self, data):
        """
        calculate client requests
        :param data: dictionary contains action and parameters
        :return: os command execution result
        """

        data = json.loads(data)
        action = data['action']
        params = data['params']
        return self.execute_command(action, params)

    def execute_command(self, action, params):
        """
        bind action and params to the OS command and execute it
        :param action: type of calculation
        :param params: command parameters
        :return: os command execution result
        """
        command = config.COMMANDS[action] % tuple(params)
        return os.popen(command).read().strip()