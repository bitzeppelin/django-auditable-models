from distutils.core import setup

setup(
    name = "django-cached-user",
    version = "1.0",
    author = "Bit Zeppelin",
    author_email = "opensource@bitzeppelin.com",
    description = "Auditable model classes for Django",
    long_description = open("README.md").read(),
    license = "BSD",
    url = "http://github.com/bitzeppelin/django-auditable-models",
    install_requires = [
        "Django",
        "django-cached-user"
    ],
    packages = [
        "auditable_models",
    ],
    classifiers = [
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Framework :: Django",
    ]
)
