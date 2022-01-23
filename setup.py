from setuptools import setup
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()
setup(
    name="pytender",
    packages=["pytender"],
    package_data={"": ["PyTender-format.docx", "gui.pyw", "classes.py"]},
    # include_package_data=True,
    version="1.5.2.1",  # Start with a small number and increase it with every change you make
    license="MIT License",
    description="Prepare bid documents",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Pragyan Shrestha",
    author_email="pragyanOne@gmail.com",
    url="https://github.com/pragyanone/tender",
    download_url="https://github.com/pragyanone/pytender/archive/refs/tags/1.5.2.1.tar.gz",
    keywords=[
        "ppmo",
        "bid",
        "tender",
    ],  # Keywords that define your package best
    install_requires=["python-docx==0.8.11", "num2words==0.5.10"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",  # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        "Intended Audience :: End Users/Desktop",  # Define that your audience are developers
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",  # Again, pick a license
        "Programming Language :: Python :: 3",  # Specify which pyhton versions that you want to support
    ],
)
