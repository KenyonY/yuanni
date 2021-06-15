import os
from guang import rm
# from tools import update_requirements


# To keep manimlib latest.
# update_requirements()

rm(['build', 'dist', 'eggs', 'yuanni.egg-info'])

# os.system("yapf -i -r ./manim_express")
os.system('python setup.py sdist bdist_wheel')
os.system('twine upload dist/*')

rm(['build', 'dist', 'eggs', 'yuanni.egg-info'])

