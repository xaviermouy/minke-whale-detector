"""
This code updates the audio file path in the detection files in case audio files have been moved since the detector was run.

"""
from ecosound.core.tools import list_files
from ecosound.core.annotation import Annotation
import os

detec_dir =r'\\nefscdata\PassiveAcoustics\DETECTOR_OUTPUT\PYTHON_MINKE\KETOS_v0.2\Raw\NEFSC_GOM\NEFSC_GOM_202102_MDR_NOTCOMPLETE'
new_audio_dir = r'/mnt/PassiveAcoustics_Soundfiles/PassiveAcoustics_Soundfiles/BOTTOM_MOUNTED/NEFSC_GOM/NEFSC_GOM_202102_MDR/5443_48kHz_UTC'

print('Starting to update audio files paths.')
nc_files = list_files(detec_dir,suffix='.nc')
for nc_file in nc_files:
    annot=Annotation()
    annot.from_netcdf(nc_file)
    annot.insert_values(audio_file_dir=new_audio_dir)
    annot.to_netcdf(nc_file)
    print('stop')
print('Process complete.')