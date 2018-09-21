import fme
import fmeobjects


class FeatureProcessor(object):
    def __init__(self):
        self.unique_attributes = dict()
        self.feature_list = []
        
    def input(self,feature):
        for attribute_name in feature.getAllAttributeNames():
            if attribute_name not in self.unique_attributes.keys():
                # Store unique attribute values in a set
                self.unique_attributes[attribute_name] = set()
                self.unique_attributes[attribute_name].add(feature.getAttribute(attribute_name))
            else:
                self.unique_attributes[attribute_name].add(feature.getAttribute(attribute_name))
        self.feature_list.append(feature)
        
    def close(self):
        
        # Tranform every set into list
        # To preserve index
        for attribute_name, value_set in self.unique_attributes.items():
            self.unique_attributes[attribute_name] = list(value_set)
        
        # Create new attributes with reference to the old attribute name
        # Switch value with index id
        for feature in self.feature_list:
            for attribute_name, value_list in self.unique_attributes.items():
                attribute_value = feature.getAttribute(attribute_name)
                feature.setAttribute(f'ref_{attribute_name}', value_list.index(attribute_value))
            self.pyoutput(feature)
        # Create new features one per unique value
        # Group feature_type per attribute name
        # Set attribute with reference to the index
        for attribute_name, value_list in self.unique_attributes.items():    
            for index, attribute_value in enumerate(value_list):
                newFeature = fmeobjects.FMEFeature()
                newFeature.setAttribute('fme_feature_type', f'{attribute_name}_table')
                newFeature.setAttribute(attribute_name, attribute_value)
                newFeature.setAttribute(f'ref_{attribute_name}', index)
                self.pyoutput(newFeature)
            

import fmeobjects
import os

INFO = fmeobjects.FME_INFORM # 0
WARN = fmeobjects.FME_WARN # 1
ERROR = fmeobjects.FME_ERROR # 2

logger = fmeobjects.FMELogFile()

CURRENT_PATH = FME_MacroValues['FME_MF_DIR_DOS']
FILENAME = FME_MacroValues['FME_MF_NAME']

CONFIGFILE = f'{FILENAME}_config.xml'.replace('.fmw','')

if os.path.isfile(CONFIGFILE):
    logger.logMessageString('Configfile ok', INFO)
    
else:
    logger.logMessageString(f'file don\'t exists: {os.path.join(CURRENT_PATH, CONFIGFILE)}', ERROR)
    raise FileNotFoundError(f'Missing file: {os.path.join(CURRENT_PATH, CONFIGFILE)}')

    