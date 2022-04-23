
import camera
import platform

operating_system_name = platform.system()

if operating_system_name == "Windows":
    camera.start_windows_gesture_library()

elif operating_system_name == "Linux":
    pass
elif operating_system_name == "Darwin":     #Library returns Darwin when you use Mac
    print("Your system is unsupported")


