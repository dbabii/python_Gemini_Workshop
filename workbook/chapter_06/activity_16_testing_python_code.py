import subprocess
import sys

code = compile("1" + "+1" * 10 ** 6, "string", "exec")

r = subprocess.run([sys.executable, "-c", code],
                   capture_output=True)
# got recurrsion error
print(r.returncode)