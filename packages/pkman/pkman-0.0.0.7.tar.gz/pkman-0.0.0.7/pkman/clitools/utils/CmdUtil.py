import subprocess
def run_command(args):
    return subprocess.check_call(" ".join(args), shell=True)

def gen_fire_argv(*args, **kwargs):
    argv = []
    for arg in args:
        argv.append(str(arg))
    for k, v in kwargs.items():
        argv.append('--%s=%s' % (k, v))
    return argv