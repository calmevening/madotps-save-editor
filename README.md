# madotps-save-editor
Save editor for the Madoka Magica TPS games

## The Games
The Madoka Magica TPS games were a series of third person shooters developed from 2011-2013 for Android and iOS. There are three entries and several ports to iOS, and Au Smart Pass, both of which are currently lost media.

It is speculated by the repo maintainer that this file format is also used in the lost game "M.N.I.B.R." ("Manicured Nails in Bloody Red"), a first person shooter created by the same developer of the TPS games.

## Format
All integers are stored as big-endian bytes in a binary file that's been harcoded to be named "save.sav". This file is located in /data/data/ on Android; no information currently on how the iOS port stores the file.

The file can be retrieved by a file explorer or command prompt, but only if your phone is rooted/jailbroken or you're using a rooted Android emulator.

The file is set at a constant size of 512 bytes, but will only ever use and modify 380 bytes.

The file is structured like this:
<pre>
* 0 - the file's magic number is the integer 0; 0x0000
* continueStage
* continueDifficulty (0-3)
* continueScore (the default value is 0)
* continueTime (the default value is 0)
* bestScore[i][j] (the default value is 0)
* bestTime[i][j] (the default value is 20 BF 02 00 or 32)
* bestRank[i][j] (the default value is 3)
** i = level difficulty (0-3)
** j = current level (0-10)
</pre>
