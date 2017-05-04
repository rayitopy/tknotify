# tknotify
tkinter notification similar to notifysend (linux)


# tknotify #

TkNotify its a library (Windows and Linux) to show a popup message in your system.

To run it you must have python and tck/tk configured.

To use like library you can make this:

```python
import tknotify
import time
notification = tknotify.Notify(title="My notification")
notification.show()
time.sleep(5)
notification = tknotify.Notify(title="My notification", msg="My notification message", expire_time=0)
notification.show()
time.sleep(5)
notification.hide()
time.sleep(5)
notification.show()
time.sleep(5)
notification.destroy()
```
