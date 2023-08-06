"""
1. Move the source code to the src/ folder.
2. Run from the directory where `pyproject.toml` is located:
    py -m build
3. Upload to PyPI:
    py -m twine upload --repository testpypi dist/* (testing site)
    py -m twine upload dist/*

"""
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyev3",
    version="0.0.5",
    author="Eduardo Nigro",
    author_email="eduardo.b.nigro@gmail.com",
    description="Direct Commands for LEGO EV3",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/EduardoNigro/pyev3",
    project_urls={
        "Bug Tracker": "https://github.com/EduardoNigro/pyev3/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows :: Windows 10",
    ],
    install_requires=[
        "hidapi",
        "numpy",
        "plotly"
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
