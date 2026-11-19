#!/bin/bash
set -e
T=/home/felipe-lopez/titanium/.hephaestus/storyboards/is-this-all-on-runware/making-of/takes
D=/home/felipe-lopez/titanium/.hephaestus/storyboards/is-this-all-on-runware/making-of/titles
I=/tmp/cleancut2/int
O="/home/felipe-lopez/Desktop/Runware Test/Creative Task Runware/Final Passes/pieces"
p() { python3 /tmp/cleancut2/scripts/piece.py "$1"; }
# name vsrc va vb asrc aa ab [norm]
r() { p "{\"out\":\"$O/$1.mp4\",\"vsrc\":\"$2\",\"va\":$3,\"vb\":$4,\"asrc\":\"$5\",\"aa\":$6,\"ab\":$7${8:+,\"norm\":$8}}"; }
r 00-title-card        $D/title-card-with-silence.mp4 0 48 $D/title-card-with-silence.mp4 0 48 false
r 01-1B-pick           $T/1B-pick.mp4 0 96 $T/1B-pick.mp4 0 96
r 02-1C-1-pick         $T/1C-1-pick.mp4 0 60 $T/1C-1-pick.mp4 0 60
r 03-1C-2-v3           $T/1C-2-v3.mp4 0 84 $T/1C-2-v3.mp4 0 84
r 04-bridge-1-2-v1     $I/bridge-1-2-v1.tail.nut 0 121 $T/bridge-1-2-v1.mp4 0 121
r 05-2A-1-v2-graded    $I/2A-1.g3.nut 0 36 $T/2A-1-v2.mp4 12 48
r 06-2A-2-v3-graded    $I/2A-2.g1.nut 0 72 $T/2A-2-v3.mp4 0 72
r 07-2B-v2             $T/2B-v2.mp4 0 96 $T/2B-v2.mp4 0 96
r 08-2C-v3             $T/2C-v3.mp4 72 144 $T/2C-v3.mp4 72 144
r 09-bridge-2-3        $T/bridge-2-3.mp4 0 97 $T/bridge-2-3.mp4 0 97
r 10-3A-v2             $T/3A-v2.mp4 12 120 $T/3A-v2.mp4 12 120
r 11-3B-pick           $T/3B-pick.mp4 0 120 $T/3B-pick.mp4 0 120
r 12-3C-1-pick         $T/3C-1-pick.mp4 0 48 $T/3C-1-pick.mp4 0 48
r 13-3C-2-pick         $T/3C-2-pick.mp4 0 72 $T/3C-2-pick.mp4 0 72
r 14-3D-1-v2           $T/3D-1-v2.mp4 0 72 $T/3D-1-v2.mp4 0 72
r 15-3D-2-pick         $T/3D-2-pick.mp4 0 72 $T/3D-2-pick.mp4 0 72
r 16-3E-pick           $T/3E-pick.mp4 0 81 $T/3E-pick.mp4 0 81
r 17-3F-pick           $T/3F-pick.mp4 0 144 $T/3F-pick.mp4 0 144
r 18-black-end         $D/black-1.5s.mp4 0 36 $D/black-1.5s.mp4 0 36 false
