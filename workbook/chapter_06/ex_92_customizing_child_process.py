import os
import subprocess

# .run is high-level to call API, .Popen is low-level to call API
# access to process env vars via os.environ
result = subprocess.run(["env"], capture_output=True, text=True,
                        env={**os.environ, "SERVER": "OTHER_SERVER"})
# print all vars in stdout
print(result.stdout)
# use a diff set of envs vars
result_other = subprocess.run(["env"], capture_output=True, text=True, env={"SERVER": "OTHER_SERVER"})
print(result_other.stdout)