# Mag database

This is an app I wrote as a way of learning to use Eagle, a front-end client program that works with the Emerald Bay database engine.

The files are (I think):

- User-created files:
  - `MAG.BAT` - a simple batch file that just runs the command: `eb eagle mag`.
  - `MAG.PGM` - the main Eagle program for the application. This includes/calls:
    - `AVACOL.PGM` - a small program to set screen colours.
    - `MAG.LIB` - a library of functions for this application.
  - `MAG.EBR` - not sure about this. It looks like it might be a config file for Eagle.
  - `AVALANCH.LIB` - a library of useful functions (my company at the time was called Avalanche, so I probably intended this to be a library to be used across a number of applications).
  - `REFERENC.EBD` - the binary database file.
  - `REFERENC.EBX` - the binary index file.
- System files:
  - `EB.EXE` - the executable for the database engine (server) that lives in the upper part of memory.
  - `EAGLE.EXE` - the executable for the Eagle front-end.
  - `EAGLE.PGM` - I think this is an Eagle program that is used to configure the system.
