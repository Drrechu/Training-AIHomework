from setuptools import setup, find_packages


def get_requirements():
    with open('requirements.txt') as requirements:
        return requirements.read().splitlines()


setup(
    name="ReceiverService",
    version="0.1.0",
    description="Practice service",
    author="Dawid Rech",
    install_requires=get_requirements(),
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'receiver_service = receiver_service.app:run_app',
        ]
    },
    include_packages_data=True
)