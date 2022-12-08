from setuptools import setup, find_packages
  
with open('requirements.txt') as f:
    requirements = f.readlines()
  
long_description = 'Um pacote pip do projeto de Métodos de Desenvolvimento de Software - Squad7'
  
setup(
        name ='mkdocs_s7',
        version ='1.3.0',
        author ='Bruno Ribeiro, Bruno Martins, Diógenes Dantas, Igor Penha, Lucas Gobbi e Rafael Nobre',
        author_email ='rafaelmedeirosnobre2001@gmail.com',
        description ='Um pacote python de geração de documentos automáticos',
        long_description = long_description,
        long_description_content_type ="text/markdown",
        license ='MIT',
        packages = find_packages(),
        entry_points ={
            'console_scripts': [
                'mkdocs_s7 = mkdocs_s7.main:main'
            ]
        },
        classifiers =(
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
        ),
        keywords ='mkdocs_s7',
        install_requires = requirements,
        zip_safe = False
)