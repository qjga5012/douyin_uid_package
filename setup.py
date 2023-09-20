from setuptools import setup, find_packages

setup(
    name="douyin_uid_package",
    version="0.0.1",
    packages=find_packages(),
    install_requires=[
        # 在这里列出你的库所需的其他Python包
        'requests',
    ],

    author="caohui524",
    author_email="408141249@qq.com",
    description="A library for obtaining tiktok uid",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    license="MIT",
    url="",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)