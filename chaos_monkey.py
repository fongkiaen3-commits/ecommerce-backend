import subprocess
import time

print("Chaos Monkey starting...")
time.sleep(3)

subprocess.run(["docker", "stop", "indestructible-db"])

