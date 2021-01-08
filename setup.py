import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="greenmonster-fastapi-braddschick", # Replace with your own username
    version="0.0.1",
    author="Bradd Schick",
    author_email="bradd.schick@gmail.com",
    description="A logging package for FastAPI using loguru",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/braddschick/greenmonster-fastapi",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)