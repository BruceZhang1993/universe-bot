from setuptools import setup, find_packages
import universe_bot

setup(
    name=universe_bot.__name__,
    version=universe_bot.__version__,
    packages=find_packages(),
    url=universe_bot.__url__,
    license=universe_bot.__license__,
    author=universe_bot.__author__,
    author_email=universe_bot.__email__,
    description=universe_bot.__description__,
    long_description=universe_bot.__long_description__,
    long_description_content_type="text/markdown",
    keywords=universe_bot.__keywords__,
    install_requires=universe_bot.__requirements__,
    extra_requires=universe_bot.__extra_requires__,
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'universe-bot=universe_bot.__main__:main'
        ],
        'universe_bot.backend': [
            'telegram=universe_bot_telegram',
        ]
    }
)
