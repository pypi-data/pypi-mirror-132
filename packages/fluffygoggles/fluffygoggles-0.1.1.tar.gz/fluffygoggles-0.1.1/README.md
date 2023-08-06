FluffyGoggles
======

A Python app for taking a screenshot, reading the text with OCR, and copying the text to the clipboard. And it's free.

The name was randomly generated.

Installation
------------

To install with pip, run:

    pip install fluffygoggles

Quickstart Guide
----------------

Run this program with:

    python -m fluffygoggles

This will take a screenshot, run OCR on it (with pytesseract), and copy the recognized text to the clipboard. It will also open up a "result text" window that looks like Notepad.

You can also run:

    python -m fluffygoggles someimage.png

...to run the program on an image file instead of a screenshot.

You can add the `-q` or `--quiet` argument to suppress the output and result text window.

Contribute
----------

If you'd like to contribute to FluffyGoggles, check out https://github.com/asweigart/fluffygoggles
