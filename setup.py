"""
Setup for building HDeepRM package.
"""

import os.path as path
import setuptools
import hdeeprm.__meta__ as meta

def main() -> None:
    """
Entry point for the setup.

Args:
    None.

Returns:
    None.
    """

    readme = open(path.join(path.dirname(__file__), 'README.rst')).read()
    setuptools.setup(
        name=meta.NAME,
        version=meta.VERSION,
        author=meta.AUTHOR,
        author_email=meta.AUTHOR_EMAIL,
        description=meta.DESCRIPTION,
        long_description=readme,
        url=meta.URL,
        license='MIT',
        packages=[meta.NAME],
        classifiers=[
            'Development Status :: 4 - Beta',
            'Intended Audience :: Science/Research',
            'License :: OSI Approved :: MIT License',
            'Natural Language :: English',
            'Programming Language :: Python :: 3.6',
            'Topic :: Scientific/Engineering :: Artificial Intelligence'
        ],
        keywords=meta.KEYWORDS,
        install_requires=[
            'defusedxml',
            'gym',
            'lxml',
            'numpy',
            'procset',
            'pybatsim',
            'torch'
        ],
        entry_points={
            'console_scripts': [
                'hdeeprm-launch = hdeeprm.cmd:launch'
            ]
        },
        include_package_data=True)

if __name__ == '__main__':
    main()
