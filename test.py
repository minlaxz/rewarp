import time
import sys

for i in range(18, 0, -1):
    print(f"\r{i}", end=" ")
    sys.stdout.flush()
    time.sleep(1)
