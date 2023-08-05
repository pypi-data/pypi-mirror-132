import os
import sys
import traceback

from importlib import import_module
from os.path import abspath


def _add_paths(paths, **special_paths):
    import os
    import sys
    
    os.chdir(os.path.dirname(__file__))

    # add current dir to `sys.path` (this is necessary for embed python)
    sys.path.insert(0, abspath('.'))
    sys.path.insert(1, abspath(special_paths['project_lib']))
    sys.path.extend(map(os.path.abspath, paths))
    
    if special_paths.get('pywin32'):
        # ref: https://stackoverflow.com/questions/58612306/how-to-fix
        #      -importerror-dll-load-failed-while-importing-win32api
        #      (see comment of @ocroquette)
        try:
            import pywin32_system32
        except ImportError:
            print('Adding pywin32 support failed')
            
        _pywin32_dir = pywin32_system32.__path__._path[0]  # noqa
        #   -> ~/lib/site-packages/pywin32_system32
        os.add_dll_directory(_pywin32_dir)
        #   WARNING: this method is available since python 3.8.
        
        _site_packages_dir = os.path.dirname(_pywin32_dir)
        sys.path.extend((
            _site_packages_dir + '/pythonwin',
            _site_packages_dir + '/win32',
            _site_packages_dir + '/win32/lib',
        ))


# ------------------------------------------------------------------------------


def auth_launch():
    pass


def launch(main_func, *args, **kwargs):
    try:
        main_func(*args, **kwargs)
    except Exception:
        _show_error_info(traceback.format_exc())
        input('Press enter to leave...')
    sys.exit()


def _show_error_info(err_msg, title='Runtime Exception', terminal='console'):
    """
    Args:
        err_msg: suggest passing `traceback.format_exc()`.
        title:
        terminal:

    Rerferences:
        https://stackoverflow.com/questions/1278705/when-i-catch-an-exception
            -how-do-i-get-the-type-file-and-line-number
        https://stackoverflow.com/questions/17280637/tkinter-messagebox-without
            -window
        https://www.cnblogs.com/freeweb/p/5048833.html
    """
    if terminal == 'console':
        print(title + ':', err_msg)
    elif terminal == 'tkinter':
        from tkinter import Tk, messagebox
        root = Tk()
        root.withdraw()
        messagebox.showerror(title=title, message=err_msg)
    elif terminal == 'vbsbox':
        return os.popen(
            'echo msgbox "{{msg}}", 64, "{{title}}" > '
            'alert.vbs && start '
            'alert.vbs && ping -n 2 127.1 > '
            'nul && del alert.vbs'.format(title=title, msg=err_msg)
        ).read()


if __name__ == '__main__':
    # try:
    #     from lk_logger import lk
    #     lk.enable_lite_mode()
    # except Exception:
    #     lk = None
    import os

    os.chdir(os.path.dirname(__file__))

    try:
        conf = _parse_target_conf(sys.argv)
        # from lk_logger import lk
        # lk.logp(conf)
        
        # check in target dir to make sure all sequent relative paths
        # references are based on the target dir.
        os.chdir(conf['TARGET_DIR'])
        sys.path.append(abspath('.'))
        
        mod = import_module(conf['TARGET_MOD'], conf['TARGET_PKG'])
        if conf['TARGET_FUNC']:
            main = getattr(mod, conf['TARGET_FUNC'])
            launch(main, *conf['TARGET_ARGS'], **conf['TARGET_KWARGS'])
    
    except Exception:
        _show_error_info(traceback.format_exc())
        input('Press enter to leave...')
    
    # finally:
    #     if lk:
    #         lk.enable()
