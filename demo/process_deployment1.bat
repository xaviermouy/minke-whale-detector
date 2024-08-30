@echo off 

rem ############################### Data info ############################
set AUDIO_DIR=C:\Users\xavier.mouy\Documents\Projects\2021_Minke_detector\apps\Minke_detector_windows_anaconda\demo\data\deployment1
set FILES_EXT=.wav
set CHANNEL=1
set RECORDING_ID=UK-SAMS-N1-20201102
set OUTPUT_DIR=C:\Users\xavier.mouy\Documents\Projects\2021_Minke_detector\apps\Minke_detector_windows_anaconda\demo\results\deployment1
set SUMMARY_TIME_OFFSET=0 

rem ############################## Detector info #########################
set DETECTOR_DIR=C:\Users\xavie\OneDrive\Desktop\Minke_detector
set MODEL=C:\Users\xavie\OneDrive\Desktop\Minke_detector\models\with_denoising\ketos_model.kt
set MIN_CONFIDENCE=0.9
set BATCH_SIZE=512

rem ######################### No need to edit part below #################
echo "Starting detector"
set TMP_DIR=%DETECTOR_DIR%\tmp
python %DETECTOR_DIR%\scripts\run_ketos_detector.py --audio_folder=%AUDIO_DIR% --extension=%FILES_EXT% --channel=%CHANNEL% --deployment_id=%RECORDING_ID% --output_folder=%OUTPUT_DIR% --model=%MODEL% --tmp_dir=%TMP_DIR% --batch_size=%BATCH_SIZE% --threshold=0.1 --step_sec=1 --smooth_sec=0 --recursive & echo "Extracting detections and daily summary" & python %DETECTOR_DIR%\scripts\create_detection_spectrograms_and_spreadsheet.py --detec_dir=%OUTPUT_DIR% --time_offset=%SUMMARY_TIME_OFFSET% --min_confidence=%MIN_CONFIDENCE%
echo "Processing complete"
pause