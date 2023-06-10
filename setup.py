import setuptools
with open('README.md','r',encoding='utf-8') as f:
    long_description = f.read()

__version__ = "0.0.0"
REPO_NAME = "Text_Summarizer"
AUTHOR_USER_NAME = "anishantony8"
SRC_REPO = "text_summaraizer"
AUTHOR_EMAIL = 'anishantony8@gmail.com'
setuptools.setup(
    name=REPO_NAME,
    version=__version__,
    author_email=AUTHOR_EMAIL,
    author=AUTHOR_USER_NAME,
    long_description="An app for text summarization",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls = {
        "Bug_Tracker" : f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")

)