Dependencies
============

Tidy depends on several python packages as described in ``setup.py``.

Besides, it depends on:

- ``tesseract`` for OCR (also you need some language pack for ``tesseract`` installed).
  For Arch, install with

  .. code-block:: bash

     $ sudo pacman -S tesseract tesseract-data-eus

- ``imagemagick`` for image manipulation, such as metadata generation.

  .. code-block:: bash

     $ sudo pacman -S imagemagick

