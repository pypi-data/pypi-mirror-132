import os
import sys

from setuptools import find_packages
from setuptools import setup

version = "1.0.1"

install_requires = [
    "setuptools>=39.0.1",
]

if not os.environ.get("SNAP_BUILD"):
    install_requires.extend(
        [
            # We specify the minimum acme and certbot version as the current plugin
            # version for simplicity. See
            # https://github.com/certbot/certbot/issues/8761 for more info.
            f"acme>={version}",
            f"certbot>={version}",
        ]
    )
elif "bdist_wheel" in sys.argv[1:]:
    raise RuntimeError(
        "Unset SNAP_BUILD when building wheels " "to include certbot dependencies."
    )
if os.environ.get("SNAP_BUILD"):
    install_requires.append("packaging")

with open("README.md") as readme:
    long_description = readme.read()


setup(
    name="certbot-dns-innovativity",
    version=version,
    description="Innovativity DNS Manager Authenticator plugin for Certbot",
    url="https://github.com/innovativity/",
    author="Innovativity S.r.l.",
    author_email="support@innovativity.it",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT License",
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Plugins",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Security",
        "Topic :: System :: Installation/Setup",
        "Topic :: System :: Networking",
        "Topic :: System :: Systems Administration",
        "Topic :: Utilities",
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=install_requires,
    entry_points={
        "certbot.plugins": [
            "dns-innovativity = certbot_dns_innovativity.dns_innovativity:Authenticator",
        ],
    },
)
