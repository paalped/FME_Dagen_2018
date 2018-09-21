import fmeobjects
import os

logger = fmeobjects.FMELogFile()
CURRENT_PATH = FME_MacroValues['FME_MF_DIR_DOS']

some_deleted = False
deleted_files = []
for _file in os.listdir(CURRENT_PATH):
    if '_pytmp_' in _file:
        os.remove(_file)
        deleted_files.append(_file)
        some_deleted = True
deleted_files = '\n'.join(deleted_files)
if some_deleted:
    logger.logMessageString(f'Following files has been cleaned: {deleted_files}', 0)