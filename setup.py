from setuptools import setup, find_packages

setup(
    name="open-code-bridge",
    version="0.0",
    description="",
    author="",
    author_email="",
    url="https://github.com/KKogaa/open-api-bridge",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
    ],
    entry_points={
        "console_scripts": [
            "ocb=main:main",
        ],
    },
)
