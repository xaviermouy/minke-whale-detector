"""
This code updates the audio file path in the detection files in case audio files have been moved since the detector was run.

"""
from ecosound.core.tools import list_files, filename_to_datetime
from ecosound.core.annotation import Annotation
import os
import pandas as pd

detec_dir =r'\\nefscdata\PassiveAcoustics\DETECTOR_OUTPUT\PYTHON_MINKE\KETOS_v0.2\Raw\NEFSC_GOM\NEFSC_GOM_202102_MDR'
new_audio_dir = r'/mnt/PassiveAcoustics_Soundfiles/PassiveAcoustics_Soundfiles/BOTTOM_MOUNTED/NEFSC_GOM/NEFSC_GOM_202102_MDR/5443_48kHz_UTC'

print('Starting to update audio files paths.')
nc_files = list_files(detec_dir,suffix='.nc')
for nc_file in nc_files:
    annot=Annotation()
    annot.from_netcdf(nc_file)
    # update audio dir
    annot.insert_values(audio_file_dir=new_audio_dir)
    # update datetime values
    full_paths = annot.data.audio_file_dir + os.sep + annot.data.audio_file_name + annot.data.audio_file_extension
    annot.data.audio_file_start_date = filename_to_datetime(full_paths.to_list())
    if len(annot)>0:
        annot.data["time_min_date"] = pd.to_datetime(annot.data["audio_file_start_date"] + pd.to_timedelta(annot.data["time_min_offset"], unit="s"))
        annot.data["time_max_date"] = pd.to_datetime(annot.data["audio_file_start_date"] + pd.to_timedelta(annot.data["time_max_offset"], unit="s"))
    # save update data
    annot.to_netcdf(nc_file)
    print('stop')
print('Process complete.')