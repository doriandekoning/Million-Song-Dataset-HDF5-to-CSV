"""
Alexis Greenstreet (October 4, 2015) University of Wisconsin-Madison

This code is designed to convert the HDF5 files of the Million Song Dataset
to a CSV by extracting various song properties.

The script writes to a "SongCSV.csv" in the directory containing this script.

Please note that in the current form, this code only extracts the following
information from the HDF5 files:
AlbumID, AlbumName, ArtistID, ArtistLatitude, ArtistLocation,
ArtistLongitude, ArtistName, Danceability, Duration, KeySignature,
KeySignatureConfidence, SongID, Tempo, TimeSignature,
TimeSignatureConfidence, Title, and Year.

This file also requires the use of "hdf5_getters.py", written by
Thierry Bertin-Mahieux (2010) at Columbia University

Credit:
This HDF5 to CSV code makes use of the following example code provided
at the Million Song Dataset website 
(Home>Tutorial/Iterate Over All Songs, 
http://labrosa.ee.columbia.edu/millionsong/pages/iterate-over-all-songs),
Which gives users the following code to get all song titles:

import os
import glob
import hdf5_getters
def get_all_titles(basedir,ext='.h5') :
    titles = []
    for root, dirs, files in os.walk(basedir):
        files = glob.glob(os.path.join(root,'*'+ext))
        for f in files:
            h5 = hdf5_getters.open_h5_file_read(f)
            titles.append( hdf5_getters.get_title(h5) )
            h5.close()
    return titles
"""

import sys
import os
import glob
import hdf5_getters
import re

class Song:
    songCount = 0
    # songDictionary = {}

    def __init__(self, songID):
        self.id = songID
        Song.songCount += 1
        # Song.songDictionary[songID] = self

        self.albumName = None
        self.albumID = None
        self.artistID = None
        self.artistLatitude = None
        self.artistLocation = None
        self.artistLongitude = None
        self.artistFamiliarity = None
        self.artistHotttnesss = None
        self.artistmbid = None
        self.artistPlaymeid = None
        self.artist7digitalid = None
        self.artistTerms = None
        self.artistTermsFreq = None
        self.artistTermsWeight = None
        self.artistMBTags = None
        self.artistMBTagsCount = None
        self.analysisSampleRate = None
        self.audioMD5 = None
        self.endOfFadeIn = None
        self.startOfFadeOut = None
        self.energy = None
        self.release = None
        self.release7digitalid = None
        self.songHotness = None
        self.track7digitalid = None
        self.similarartists = None
        self.loudness = None
        self.mode = None
        self.modeConfidence = None
        self.artistName = None
        self.danceability = None
        self.duration = None
        self.keySignature = None
        self.keySignatureConfidence = None
        self.tempo = None
        self.timeSignature = None
        self.timeSignatureConfidence = None
        self.title = None
        self.year = None
        self.trackID = None
        self.segmentsStart = None
        self.segmentsConfidence = None
        self.segmentsPitches = None
        self.segmentsTimbre = None
        self.segmentsLoudnessMax = None
        self.segmentsLoudnessMaxTime = None
        self.segmentsLoudnessStart = None
        self.sectionStarts = None
        self.sectionsConfidence = None
        self.beatsStart = None
        self.beatsConfidence = None
        self.barsStart = None
        self.barsConfidence = None
        self.tatumsStart = None
        self.tatumsConfidence = None

    def displaySongCount(self):
        print "Total Song Count %i" % Song.songCount

    def displaySong(self):
        print "ID: %s" % self.id  
	
def writeheader(file, csvRowString):
	
	file.write("SongNumber,");
	file.write(csvRowString + "\n");
	csvRowString = ""  

def main():
    if not os.path.exists("out"):
    	os.makedirs("out")
    outputFile1 = open('out/SongCSV0.csv', 'w')

    csvRowString = ("SongID,albumName,albumID,artistID,artistLatitude,artistLocation,artistLongitude,artistFamiliarity,artistHotttnesss,artistmbid,artistPlaymeid,artist7digitalid,artistTerms,artistTermsFreq,artistTermsWeight,artistMBTags,artistMBTagsCount,analysisSampleRate,audioMD5,endOfFadeIn,startOfFadeOut,energy,release,release7digitalid,songHotness,track7digitalid,similarartists,loudness,mode,modeConfidence,artistName,danceability,duration,keySignature,keySignatureConfidence,tempo,timeSignature,timeSignatureConfidence,title,year,trackID,segmentsStart,segmentsConfidence,segmentsPitches,segmentsTimbre,segmentsLoudnessMax,segmentsLoudnessMaxTime,segmentsLoudnessStart,sectionStarts,sectionsConfidence,beatsStart,beatsConfidence,barsStart,barsConfidence,tatumsStart,tatumsConfidence")

    csvAttributeList = re.split('\W+', csvRowString)
    for i, v in enumerate(csvAttributeList):
        csvAttributeList[i] = csvAttributeList[i].lower()
    writeheader(outputFile1, csvRowString)
    print("started converting")



    #Set the basedir here, the root directory from which the search
    #for files stored in a (hierarchical data structure) will originate
    basedir = "." # "." As the default means the current directory
    ext = ".h5" #Set the extension here. H5 is the extension for HDF5 files.
    #################################################
  
    #FOR LOOP
    counter = 0
    filecounter = 0
    for root, dirs, files in os.walk(basedir):        
        files = glob.glob(os.path.join(root,'*'+ext))
        for f in files:
	    counter+=1
        if (counter % 1000) == 0 :
	    	print "Progress: {0}".format(counter)
        if (counter % 10000) == 0 :
    		outputFile1.close()
    	    filecounter+=1
		outputFile1 = open('out/SongCSV{0}.csv'.format(filecounter), 'w')
		writeheader(outputFile1, csvRowString)
		
            songH5File = hdf5_getters.open_h5_file_read(f)
            song = Song(str(hdf5_getters.get_song_id(songH5File)))

            testDanceability = hdf5_getters.get_danceability(songH5File)
            # print type(testDanceability)
            # print ("Here is the danceability: ") + str(testDanceability)

            song.artistName = str(hdf5_getters.get_artist_name(songH5File))
            song.artistID = str(hdf5_getters.get_artist_id(songH5File))
            song.albumID = str(hdf5_getters.get_release_7digitalid(songH5File))
            song.artistLatitude = str(hdf5_getters.get_artist_latitude(songH5File))
            song.artistLocation = str(hdf5_getters.get_artist_location(songH5File))
            song.artistLongitude = str(hdf5_getters.get_artist_longitude(songH5File))
            song.artistFamiliarity = str(hdf5_getters.get_artist_familiarity(songH5File))
            song.artistHotttnesss = str(hdf5_getters.get_artist_hotttnesss(songH5File))
            song.artistmbid = str(hdf5_getters.get_artist_mbid(songH5File))
            song.artistPlaymeid = str(hdf5_getters.get_artist_playmeid(songH5File))
            song.artist7digitalid = str(hdf5_getters.get_artist_7digitalid(songH5File))
            song.artistTerms = str(hdf5_getters.get_artist_terms(songH5File))
            song.artistTermsFreq = str(hdf5_getters.get_artist_terms_freq(songH5File))
            song.artistTermsWeight = str(hdf5_getters.get_artist_terms_weight(songH5File))
            song.artistMBTags = str(hdf5_getters.get_artist_mbtags(songH5File))
            song.artistMBTagsCount = str(hdf5_getters.get_artist_mbtags_count(songH5File))
            song.analysisSampleRate = str(hdf5_getters.get_analysis_sample_rate(songH5File))
            song.audioMD5 = str(hdf5_getters.get_audio_md5(songH5File))
            song.endOfFadeIn = str(hdf5_getters.get_end_of_fade_in(songH5File))
            song.startOfFadeOut = str(hdf5_getters.get_start_of_fade_out(songH5File))
            song.energy = str(hdf5_getters.get_energy(songH5File))
            song.release = str(hdf5_getters.get_release(songH5File))
            song.release7digitalid = str(hdf5_getters.get_release_7digitalid(songH5File))
            song.songHotness = str(hdf5_getters.get_song_hotttnesss(songH5File))
            song.track7digitalid = str(hdf5_getters.get_track_7digitalid(songH5File))
            song.similarartists = str(hdf5_getters.get_similar_artists(songH5File))
            song.loudness = str(hdf5_getters.get_loudness(songH5File))
            song.mode = str(hdf5_getters.get_mode(songH5File))
            song.modeConfidence = str(hdf5_getters.get_mode_confidence(songH5File))
            song.artistName = str(hdf5_getters.get_artist_name(songH5File))
            song.danceability = str(hdf5_getters.get_danceability(songH5File))
            song.duration = str(hdf5_getters.get_duration(songH5File))
            song.keySignature = str(hdf5_getters.get_key(songH5File))
            song.keySignatureConfidence = str(hdf5_getters.get_key_confidence(songH5File))
            song.tempo = str(hdf5_getters.get_tempo(songH5File))
            song.timeSignature = str(hdf5_getters.get_time_signature(songH5File))
            song.timeSignatureConfidence = str(hdf5_getters.get_time_signature_confidence(songH5File))
            song.title = str(hdf5_getters.get_title(songH5File))
            song.year = str(hdf5_getters.get_year(songH5File))
            song.trackID = str(hdf5_getters.get_track_id(songH5File))
            song.segmentsStart = str(hdf5_getters.get_segments_start(songH5File))
            song.segmentsConfidence = str(hdf5_getters.get_segments_confidence(songH5File))
            song.segmentsPitches = str(hdf5_getters.get_segments_pitches(songH5File))
            song.segmentsTimbre = str(hdf5_getters.get_segments_timbre(songH5File))
            song.segmentsLoudnessMax = str(hdf5_getters.get_segments_loudness_max(songH5File))
            song.segmentsLoudnessMaxTime = str(hdf5_getters.get_segments_loudness_max_time(songH5File))
            song.segmentsLoudnessStart = str(hdf5_getters.get_segments_loudness_start(songH5File))
            song.sectionStarts = str(hdf5_getters.get_sections_start(songH5File))
            song.sectionsConfidence = str(hdf5_getters.get_sections_confidence(songH5File))
            song.beatsStart = str(hdf5_getters.get_beats_start(songH5File))
            song.beatsConfidence = str(hdf5_getters.get_beats_confidence(songH5File))
            song.barsStart = str(hdf5_getters.get_bars_start(songH5File))
            song.barsConfidence = str(hdf5_getters.get_bars_confidence(songH5File))
            song.tatumsStart = str(hdf5_getters.get_tatums_start(songH5File))
            song.tatumsConfidence = str(hdf5_getters.get_tatums_confidence(songH5File))
          

            #print song count
            csvRowString += str(song.songCount) + ","

            for attribute in csvAttributeList:
                # print "Here is the attribute: " + attribute + " \n"
                if hasattr(song, attribute) :
                    csvRowString += getattr(song, attribute)
                else :
                    print "Attibute {0} not found".format(attribute)

                csvRowString += ","

            #Remove the final comma from each row in the csv
            lastIndex = len(csvRowString)
            csvRowString = csvRowString[0:lastIndex-1]
            csvRowString += "\n"
            outputFile1.write(csvRowString)
            csvRowString = ""

            songH5File.close()

    outputFile1.close()
	
main()
