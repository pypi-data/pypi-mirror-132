import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ControlManual",
    version="0.0.3.6",
    author="ZeroIntensity",
    author_email="admin@controlmanual.xyz",
    description="A universal console-like interface",
    long_description=long_description,
    long_description_content_type="text/markdown",
    entry_points={
        "console_scripts": ["ControlManual=ControlManual.main:main_wrap"]
    },
    url="https://github.com/ZeroIntensity/ControlManual",
    project_urls={
        "Bug Tracker": "https://github.com/ZeroIntensity/ControlManual/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    install_requires=[
        "colorama",
        "aiohttp",
        "click",
        "rethread",
        "psutil",
        "rich",
        "distro",
        "aiofiles",
        "getch",
        "watchdog",
    ],
    python_requires=">=3.8",
)
