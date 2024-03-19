import os

os.system("pip install mido")

import mido
import os

# Get tempo (BPM) from user input
bpm = int(input("Enter BPM: "))
total_time = int(input("Enter total time of track (in seconds): "))
tempo = mido.bpm2tempo(bpm)
 
# Define functions for creating tracks
def create_lead_track():
    # Define notes and rhythm for lead melody
    lead_notes = [
        60, 62, 64, 65,
        67, 69, 71, 72,
        72, 71, 69, 67,
        65, 64, 62, 60,
    ]
    # Create lead track
    lead_track = mido.MidiTrack()
    for note in lead_notes:
        lead_track.append(mido.Message('note_on', note=note, velocity=100, time=0))
        lead_track.append(mido.Message('note_off', note=note, velocity=100, time=int(0.25*tempo)))
    return lead_track
 
def create_chords_track():
    # Define chord progressions
    chord_progressions = [
        [60, 63, 67],
        [58, 61, 64],
        [59, 63, 67],
        [57, 61, 65],
    ]
    # Create chords track
    chords_track = mido.MidiTrack()
    for i in range(4):
        chord_progression = chord_progressions[i]
        for note in chord_progression:
            chords_track.append(mido.Message('note_on', note=note, velocity=100, time=0))
        for note in chord_progression:
            chords_track.append(mido.Message('note_off', note=note, velocity=100, time=int(1*tempo/len(chord_progression))))
    return chords_track
 
def create_bass_track():
    # Define notes and rhythm for bassline
    bassline = [
        60, 60, 65, 65,
        67, 67, 65,
        60, 60, 65, 65,
        67, 67, 65,
    ]
    # Create bass track
    bass_track = mido.MidiTrack()
    for note in bassline:
        bass_track.append(mido.Message('note_on', note=note, velocity=100, time=0))
        bass_track.append(mido.Message('note_off', note=note, velocity=100, time=int(0.5*tempo)))
    return bass_track
 
def create_drums_track():
    # Define notes and rhythm for techno drum pattern
    kick = 36
    snare = 40
    hat = 42
    rhythm = [
        [kick, hat],
        [hat],
        [snare],
        [hat],
    ]
    # Create drums track
    drums_track = mido.MidiTrack()
    for i in range(total_time * 2):
        step = i % 4
        for note in rhythm[step]:
            drums_track.append(mido.Message('note_on', note=note, velocity=100, time=0))
            drums_track.append(mido.Message('note_off', note=note, velocity=100, time=int(0.125*tempo)))
    return drums_track
 
# Create MIDI file
mid = mido.MidiFile(type=1)
mid.tracks.append(create_lead_track())
mid.tracks.append(create_chords_track())
mid.tracks.append(create_bass_track())
mid.tracks.append(create_drums_track())
 
# Get directory from user input
directory = input("Enter directory to save MIDI file in (leave blank for current directory): ")
if directory:
    os.makedirs

#softy_plug

