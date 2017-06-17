__author__ = "Shlomy Balulu"

"""
Configuration file contains calculator linux command patterns
"""

COMMANDS = {
    'bc': 'echo "%d + %d" | bc',
    'prime': 'openssl prime -generate -bits %d -hex'
}