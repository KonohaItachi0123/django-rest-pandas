from setuptools import setup

LONG_DESCRIPTION = (
    "Serves up pandas dataframes via the Django REST Framework for client-side"
    "(i.e. d3.js) visualizations"
)


def readme():
    try:
        readme = open("README.md")
    except IOError:
        return LONG_DESCRIPTION
    else:
        return readme.read()


setup(
    name="rest-pandas",
    use_scm_version=True,
    author="S. Andrew Sheppard",
    author_email="andrew@wq.io",
    url="https://github.com/wq/django-rest-pandas",
    license="MIT",
    packages=["rest_pandas"],
    package_data={
        "rest_pandas": [
            "templates/rest_pandas/*.html",
            "static/rest_pandas/js/*.*",
            "static/app/js/*.*",
        ]
    },
    description=LONG_DESCRIPTION.strip(),
    long_description=readme(),
    long_description_content_type="text/markdown",
    install_requires=[
        "djangorestframework>=3.3.1",
        "pandas>=0.19.0",
    ],
    classifiers=[
        "Framework :: Django",
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Framework :: Django",
        "Framework :: Django :: 3.2",
        "Framework :: Django :: 4.0",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Scientific/Engineering :: Visualization",
    ],
    test_suite="tests",
    tests_require=[
        "itertable",
        "xlwt",
        "openpyxl",
        "django",
        "django-mustache",
    ],
    setup_requires=[
        "setuptools_scm",
    ],
)
