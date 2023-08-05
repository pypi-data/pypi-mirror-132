================
Usage
================

This module support input cipher password in terminal,Only support Python 3.  

Default prompt char is `*`，you can replace the prompt as you love,such as ★.  

::

    import terminal_password as password
    a = password.get_password()
    b = password.get_password(u'\u2605')

