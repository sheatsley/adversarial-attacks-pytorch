import setuptools  # Easily download, build, install, upgrade, and uninstall Python packages

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    author="Hoki Kim",
    author_email="24K.Harry@gmail.com",
    description="A PyTorch-based adversarial machine learning library",
    install_requires=["torch"],
    license="MIT",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords="deep-learning pytorch adversarial-attacks",
    name="torchattacks",
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
    url="https://github.com/sheatsley/adversarial_machine_learning",
)
