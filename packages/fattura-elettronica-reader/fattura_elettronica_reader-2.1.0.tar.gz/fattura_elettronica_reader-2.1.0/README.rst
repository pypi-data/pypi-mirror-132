fattura-elettronica-reader
==========================

|pypiver|    |license|    |pyver|    |downloads|    |dependentrepos|    |buymeacoffee|

.. |pypiver| image:: https://img.shields.io/pypi/v/fattura-elettronica-reader.svg
               :alt: PyPI md-toc version

.. |license| image:: https://img.shields.io/pypi/l/fattura-elettronica-reader.svg?color=blue
               :alt: PyPI - License
               :target: https://raw.githubusercontent.com/frnmst/fattura-elettronica-reader/master/LICENSE.txt

.. |pyver| image:: https://img.shields.io/pypi/pyversions/fattura-elettronica-reader.svg
             :alt: PyPI - Python Version

.. |downloads| image:: https://pepy.tech/badge/fattura-elettronica-reader
                 :alt: Downloads
                 :target: https://pepy.tech/project/fattura-elettronica-reader

.. |dependentrepos| image:: https://img.shields.io/librariesio/dependent-repos/pypi/fattura-elettronica-reader.svg
                      :alt: Dependent repos (via libraries.io)
                      :target: https://libraries.io/pypi/fattura-elettronica-reader/dependents

.. |buymeacoffee| image:: assets/buy_me_a_coffee.svg
                   :alt: Buy me a coffee
                   :target: https://buymeacoff.ee/frnmst


Validate, extract, and generate printables of electronic invoice files received
from the "Sistema di Interscambio".

Documentation
-------------

https://docs.franco.net.eu.org/fattura-elettronica-reader

API examples
------------

fattura-elettronica-reader has a `public API`_.
This means for example that you can you easily read invoice files within another
Python program:


::

    >>> import fattura_elettronica_reader
    >>> data = {
            'patched': True,
            'configuration file': str(),
            'write default configuration file': False,
            'extract attachments': True,
            'metadata file': 'myfile.xml',
            'invoice xslt type': 'ordinaria',
            'no invoice xml validation': False,
            'force invoice schema file download': False,
            'generate html output': True,
            'invoice filename': str(),
            'no checksum check': False,
            'force invoice xml stylesheet file download': False,
            'ignore attachment extension whitelist': False,
            'ignore attachment filetype whitelist': False,
            'ignore signature check': False,
            'ignore signers certificate check': False,
            'force trusted list file download': False,
            'keep original file': True,
            'ignore assets checksum': False,
            'destination directory': '/dev/shm',
    }
    >>> fattura_elettronica_reader.assert_data_structure(source='invoice', file_type='p7m', data=data)
    >>> fattura_elettronica_reader.pipeline(
            source='invoice',
            file_type='p7m',
            data=data,
        )


Have a look at the `archive_invoice_files <https://software.franco.net.eu.org/frnmst/automated-tasks/raw/branch/master/automated_tasks/archiving/archive_invoice_files.py>`_
script in the `automated tasks <https://software.franco.net.eu.org/frnmst/automated-tasks>`_ repository.

.. _public API: https://docs.franco.net.eu.org/fattura-elettronica-reader/api.html

CLI helps
---------


::


    $ fattura_elettronica_reader --help


License
-------

Copyright (c) 2018 Enio Carboni - Italy

Copyright (C) 2019-2021 Franco Masotti (franco \D\o\T masotti {-A-T-} tutanota \D\o\T com)

fattura-elettronica-reader is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

fattura-elettronica-reader is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with fattura-elettronica-reader.  If not, see <http://www.gnu.org/licenses/>.

Changelog and trusted source
----------------------------

You can check the authenticity of new releases using my public key.

Changelogs, instructions, sources and keys can be found at `blog.franco.net.eu.org/software <https://blog.franco.net.eu.org/software/>`_.

Crypto donations
----------------

- Bitcoin: bc1qnkflazapw3hjupawj0lm39dh9xt88s7zal5mwu
- Monero: 84KHWDTd9hbPyGwikk33Qp5GW7o7zRwPb8kJ6u93zs4sNMpDSnM5ZTWVnUp2cudRYNT6rNqctnMQ9NbUewbj7MzCBUcrQEY
- Dogecoin: DMB5h2GhHiTNW7EcmDnqkYpKs6Da2wK3zP
- Vertcoin: vtc1qd8n3jvkd2vwrr6cpejkd9wavp4ld6xfu9hkhh0
