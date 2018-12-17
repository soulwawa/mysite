import traceback
import sys

try:
    do_something()
except Exception:
    print(traceback.format_exc())
    traceback.print_exc()
    # traceback.print_stack()
