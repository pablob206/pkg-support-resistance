<div align="center">

## TECHNICAL DOCS
![Github Actions](https://github.com/pdm-project/pdm/workflows/Tests/badge.svg)
[![pdm-managed](https://img.shields.io/badge/pdm-managed-blueviolet)](https://pdm.fming.dev)
</div>


## Developer Command utilities
```bash
# example: initialize project
cd my-pdm-project
pip install pdm[all]
pdm install
source .venv/bin/activate

# black
pdm run black .
# flake8
pdm run flake8
pdm run flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
pdm run flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
# pre-commit
pdm run pre-commit run --all-files
# pylint
pdm run pylint --recursive=y .

# pytest
pdm run pytest

# example: pdm add, update and remove dependencies
pdm add scipy
pdm add -dG dev mplfinance # add into dev
pdm update scipy
pdm remove scipy

# Update pdm version
pdm self update

# Cython
cythonize --inplace vanilla_algo.py
python setup.py build_ext --inplace

```

### Tag push
```bash
git tag 0.1.2
git push --tags
```
