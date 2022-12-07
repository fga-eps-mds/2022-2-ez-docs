# mkdocs

### What's up everyone!

mkdocs is a MVP (minimum viable product) that were build for an SDM (Software Development Methods) class, with the aim of learn the goals of different approaches for creating software through agile practices.

So, we contribute to the Open Source community with mkdocs, which helps users to issue a wide range of certificates, declarations, resumes, receipts, slips, or whatever else the imagination allows through a database and a template in markdown format.

## Prerequisites

Before starting, make sure you've met the following requirements:
* You have installed the latest version of `<Python>`.
* You have a `<Windows / Linux / Mac>` machine.
* You read the [project GitPage](https://fga-eps-mds.github.io/2022-2-Squad07/index.html).


## Installation

To install *mkdocs*, open an interactive shell and run:
```bash
$ python<version> -m pip install mkdocs-s7
```

## Using mkdocs

To start using *mkdocs*, you'll need a markdown template, a database (.csv, .txt, xls) and a pattern of keys.

* directory_template: str - template folder .md
* key_name_file: str - parameter concerning the denominator key of the document name, which must follow the format {key_name}.
For example, for a template that has the keys "name" and "registration", the output could be "name_registration", generating the following results:
    - Aaron_3141592653.pdf
    - Barnardo_2718281828.pdf
    - Caliban_4815162342.pdf

    Valid separators: registration_name, registration-name, registration:name, registration name.
* key_value: dict - dictionary with all the keys and their respective values, already extracted from the module that handled
	the data.
    - Structure:
    ```python
    {
        "NAME": "Diomedes",
        "CLASS": "Databases",
        "DATE": "23 November 2022",
        "TIN": "161.803.398-87",
        "REGISTRATION": "1123581321"
    }
    ```
    Keys are arbitrary in nature, which means that their names, quantities, and repetitions are uncertain. All will be searched within the template: those found will be replaced by the corresponding value, and those that are not will be indicated in the terminal via warning.
* flag: int - optional parameter that defines the final output format.
    - 1 (def.) - The doc will be converted to .pdf
    - 2 - The doc will remain in .md

With that, you may open an interactive shell and run:
```bash
$ mkdocs-s7 <~/template.md> <~/database> <~/pattern_keys> --flag = 1 or 2
```


## Getting involved
1. Read the [CONTRIBUTING.md](docs/CONTRIBUTING.md) guide.
2. Fork this repository.
3. Create a branch on your local machine: `git checkout -b <branch_name>`.
4. Make your changes and confirm them following the [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/): `git commit -m "commit_message"`
5. Send to origin branch: `git push origin <branch_name> / <local>`
6. Create pull request through Github.


## Open source licensing info

This project is under license. See the [LICENSE](LICENSE) file for details.

---
**2022-2-Squad7**  

#### Special thanks to:
Dr. [Carla Rocha Aguiar](https://github.com/RochaCarla), our professor at the University of Brasília.


*Created by [Bruno Ribeiro](https://github.com/BrunoRiibeiro), [Bruno Martins](https://github.com/gitbmvb), [Diógenes Dantas](https://github.com/diogjunior100), [Igor Penha](https://github.com/igorpenhaa), [Lucas Bergholz](https://github.com/LucasBergholz) and [Rafael Nobre](https://github.com/RafaelN0bre) in 2022*
