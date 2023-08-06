import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    # 包信息
    name="wudaoAI",
    version="1.0.5",
    author="yufeng",
    author_email="zhuyufeng@wudaoai.com",
    license='MIT',
    description="超大中文预训练模型",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/wjx2zuoshi/wudaoAI",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'requests',
    ],
    # 包搜集

)