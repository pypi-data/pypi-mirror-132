Changelog for MMLlib
====================

1.4
---

- Bump major version to enable semantic versioning
- Add octave tracking feature.
- Add basic support for MicroPython/ESP PWM
- The “mmllint” command can now output “normalised” MML,
  that is, MML which will play on GW-BASIC without the
  extensions (such as octave tracking or permitting omission
  of the default argument values) present
- “N” without number is now correctly parsed (as rest)
- Update documentation wrt performance expectations, fine detail
- ./run.py (in-tree) defaults to python3 as interpreter now
- “O” without number now sets the default octave (extension),
  which was already implied in both documentation and consistency

0.3
---

-  Enable Python 3 compatibility.
-  Add new mmllint script.
-  Include example MML songs.
-  Add first parts of test suite.
-  Some bugfixes.

0.2
---

-  Add mml2musicxml script.

0.1
---

-  Separate from Floppi-Music.
