from setuptools import setup

setup_params = dict(
    name='footasks',
    version='1.0',
    description='Example tasks',
    author='Eric Larson',
    author_email='eric@ionrock.org',
    py_modules=['footasks'],
    install_requires=[
        'luigi',
        'arrow',
    ],
    entry_points={
        'deadlines.tasks': [
            'foo = footasks:Foo'
        ],
        'deadlines.targets': [
            'foofile = footasks:FooFile'
        ]
    }
)


if __name__ == '__main__':
    setup(**setup_params)
