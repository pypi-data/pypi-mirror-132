Introduction
============
Remt project is note-taking support tool for reMarkable tablet

    https://remarkable.com/

Features
--------
The features of Remt are

- reMarkable tablet operations

  - list files and directories
  - create directories
  - export a notebook as PDF file using reMarkable tablet renderer or
    Remt project renderer
  - export an annotated PDF document using reMarkable tablet renderer or
    Remt project renderer
  - import a PDF document
  - create index of PDF document annotations
  - interactive selection of files on a tablet using `fzf` command

- cache of reMarkable tablet metadata to speed up tablet operations;
  caching supports multiple devices
- Remt project renderer supports

  - export of large files and usually produces smaller PDF files comparing
    to the reMarkable tablet renderer
  - processing of multi-page notebooks and PDF files
  - most of the drawing tools

- Remt project can be used as a library for UI and other applications

Known Problems
--------------

1. Import of a PDF file requires restart of reMarkable tablet.
2. Remt ver. 0.10.0 removed support for brushes. The brushes were
   implemented using raster images, which does not look well in PDF export.
   The investigation into a vector based brushes can be found in
   `Remt wiki <https://gitlab.com/wrobell/remt/-/wikis/Tool%20Brush%20Pencil>`_.

.. vim: sw=4:et:ai
