# TayTules

No documentation yet :/

python3 -m pip install --upgrade twine

python3 -m pip install --upgrade build

python3 -m build

python3 -m twine upload --repository testpypi dist/VERSION/*

pip install -i https://test.pypi.org/simple/     TayTules-pkg-taytek==VERSION

pip install TayTules-pkg-taytek==0.0.6