# Musical-Manipulator #
Project using pyDub to manipulate and edit audio files.

<a href = "https://github.com/MartinHarvey/Musical-Manipulator/blob/master/Changelog.md"> Changelog </a>


To Do:
------
<li>
  Add Compatibility for more file formats
<li>
  Add more manipulation functions
<li>
  Add more GUI Elements

This project uses:
------------------

The excellent <a href = https://github.com/jiaaro/pydub> pyDub </a> by jiaaro forms the core of this program. It handles all of the heavy lifting in a
very easy to use, high-level syntax. It is easy to install and the source code is available on GitHub.

The GUI elements of this project are provided by Tkinter, a set of modules that are available out of the box with Python, and exists as the de-facto
standard for creating interfaces in Python. It allows you to create professional and easy to understand GUIs, which are far better than controlling a
program via the command line.

About:
------
This program was originally designed to help improve my python programming. Although still very elementary, it also helped me with
using Git for version control. An external library, pyDub is used for all sound operations. It is very high level and is similar to
regular Python. It has various functions for reversing, repeating audio, to name a few. I hope to implement more functions in the
future.

The file dialog ability comes from Tkinter, which allows GUI functions to be implemented in Python. It may be replaced by PyQt
as I create a proper GUI, rather than having a CLI. I would prefer to use TKinter, as I believe it could be perfect for such a purpose
(and as it the application uses the TKinter filedialog widget already), however, TKinter has proved difficult to use and the quality of
online tutorials is low.
