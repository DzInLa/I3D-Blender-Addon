if "bpy" in locals():
    import importlib
    reloadable_modules = [
        'addon_preferences',
        'exporter',
        'object',
        'mesh',
        'light',
        'shader_picker',
        'user_attributes',
        'udim_picker'
    ]

    for module_name in reloadable_modules:
        if module_name in locals():
            importlib.reload(locals()[module_name])

from . import (addon_preferences, exporter, object, user_attributes, mesh, light, shader_picker, udim_picker)
