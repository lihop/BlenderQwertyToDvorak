# BlenderQwertyToDvorak
To generate for keymaps for new versions of Blender:
1. Export the default Blender keymap to `templates/KeyconfigData_${version}.py`. Make sure to select 'All Keymaps' in the export options.
2. Create the new keymap using:
```
cat templates/KeyconfigData_${version}.py templates/QwertyToDvorak.py templates/Main.py > QwertyToDvorak_${version}.py
```
You can replace `templates/QwertyToDvorak.py` with `templates/QwertyToProgrammerDvorak.py` to make a keymap for Programmer Dvorak.

As an example, the QwertyToDvorak_2.8.py file was generated using:
```
cat templates/KeyconfigData_2.8.py templates/QwertyToDvorak.py templates/Main.py > QwertyToDvorak_2.8.py
```

**Note about Programmer Dvorak**:
Blender does not recognise the '!', '#', and '@' keys. Trying to set them results in an 'Unsupported key: Unknown' error. Therefore, they have been left as default. The `templates/QwertyToProgrammerDvorak.py` file can be edited to set them to something else.
