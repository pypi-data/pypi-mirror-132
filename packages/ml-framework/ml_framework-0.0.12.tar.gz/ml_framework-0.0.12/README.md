# AILib


## Commit hooks
https://medium.com/@pratu16x7/using-pre-commit-to-manage-git-hooks-532e055e4771


## Packaging
https://towardsdatascience.com/how-to-convert-your-python-project-into-a-package-installable-through-pip-a2b36e8ace10


python3 -m build
python3 -m pip install --user --upgrade twine
python3 -m twine upload --repository testpypi dist/*
python3 -m twine upload dist/*