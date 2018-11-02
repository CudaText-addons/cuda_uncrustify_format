import os
import subprocess
import cudatext as app
from . import format_proc

format_proc.INI = 'cuda_uncrustify_format.ini'
format_proc.MSG = '[Uncrustify] '
PROGRAM = 'uncrustify.exe' if os.name=='nt' else 'uncrustify' 


def run_app(text, filename, config):

    command = [PROGRAM, "--assume", os.path.basename(filename), "-c", config]
    print('Running:', ' '.join(command))
    content = text.encode("utf-8")
    
    try:
        if os.name=='nt':
            # to hide the console window brings from command
            si = subprocess.STARTUPINFO()
            si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
            # si.wShowWindow = subprocess.SW_HIDE   # this is default provided

            proc = subprocess.Popen(command, \
                   stdin = subprocess.PIPE, stdout = subprocess.PIPE, stderr = subprocess.PIPE, startupinfo = si)
        else:
            proc = subprocess.Popen(command, \
                   stdin = subprocess.PIPE, stdout = subprocess.PIPE, stderr = subprocess.PIPE)

        outs, errs = proc.communicate(input=content)

        ret_code = proc.poll()
        if ret_code != 0:
            if errs:
                msg = errs.decode("utf-8")
                # slice the last useless part if found (from Uncrustify)
                pos = msg.find("Try running with -h for usage information")
                err = "Uncrustify failed (0x%X)\n\n%s" % (ret_code, msg[:pos])
            else:
                err = "Uncrustify stopped (0x%X)" % ret_code
            
            app.msg_box(err, app.MB_OK+app.MB_ICONWARNING)
            return

    except (OSError, ValueError, subprocess.CalledProcessError, Exception) as e:
    
        err = "Cannot execute '%s':\n\n%s" % (command[0], e)
        app.msg_box(err, app.MB_OK+app.MB_ICONERROR)
        return

    formatted_code=outs.decode("utf-8")
    return formatted_code


def do_format(text):

    filename = app.ed.get_filename()
    config_file = os.path.join(os.path.dirname(filename), 'uncrustify.cfg')
    config_os = os.path.expanduser('~/uncrustify.cfg')

    if os.path.exists(config_file):
        config = config_file
    else:
        config = config_os
    
    return run_app(text, filename, config)


class Command:

    def run(self):
        format_proc.run(do_format)
