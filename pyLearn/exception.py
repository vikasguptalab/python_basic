#!/usr/bin/python
import logging

try:
    numerator = 10
    denominator = 0

    result = numerator/denominator
    print(result)
except SyntaxError:
    print("Syntax Error: Denominator cannot be 0.")
except ValueError:
    print("Value Error: Denominator cannot be 0.")
except AttributeError:
    print("Attribute Error: Denominator cannot be 0.")
except:
    logging.exception("Exception occurred")
    print("Error: Denominator cannot be 0.")


