from distutils.core import setup

install_requires = ["requests>=2.25.0", "urllib3>=1.26.0"]

setup(
    name='MlCheap',  # How you named your package folder (MyLib)
    packages=['MlCheap'],  # Chose the same as "name"
    version='0.1.8',  # Start with a small number and increase it with every change you make
    license='MIT',  # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    description='MlCheap help you to easily label your data, train your model and publish it',
    # Give a short description about your library
    author='Arash Safari',  # Type in your name
    author_email='arashsafari86@email.com',  # Type in your E-Mail
    url='https://github.com/mlcheap/api.git',  # Provide either the link to your github or to your website
    download_url='https://github.com/mlcheap/api/archive/refs/heads/main.zip',  # I explain this later on
    keywords=['mlcheap', 'api', 'labeling', 'annotation', 'machine learning', 'deeplearning'],
    # Keywords that define your package best
    install_requires=install_requires,
    classifiers=[
        'Development Status :: 3 - Alpha',
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Intended Audience :: Developers',  # Define that your audience are developers
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',  # Again, pick a license
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
