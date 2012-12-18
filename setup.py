from setuptools import setup
from ilastik import __version__

packages=['ilastik',
          'ilastik.applets',
          'ilastik.applets.base',
          'ilastik.applets.batchIo',
          'ilastik.applets.carving',
          'ilastik.applets.dataSelection',          
          'ilastik.applets.featureSelection',
          'ilastik.applets.labeling',          
          'ilastik.applets.layerViewer',
          'ilastik.applets.objectExtraction',
          'ilastik.applets.objectExtractionMultiClass',
          'ilastik.applets.pixelClassification',
          'ilastik.applets.projectMetadata',
          'ilastik.applets.thresholdMasking',
          'ilastik.applets.tracking',
          'ilastik.applets.tracking.base',
          'ilastik.applets.tracking.chaingraph',
          'ilastik.applets.tracking.conservation',
          'ilastik.applets.tracking.fastApproximate',
          'ilastik.applets.vigraWatershedViewer',
          'ilastik.shell',
          'ilastik.shell.gui',
          'ilastik.shell.headless',
          'ilastik.ilastik_logging',
          'ilastik.utility',
          'ilastik.utility.gui',
          'ilastik.widgets']

package_data={'ilastik': ['ilastik-splash.png',
                          'ilastik-splash.xcf'],
          'ilastik.applets.batchIo': ['*.ui'],
          'ilastik.applets.carving': ['*.ui'],
          'ilastik.applets.dataSelection': ['*.ui'],          
          'ilastik.applets.featureSelection': ['*.ui'],
          'ilastik.applets.labeling': ['*.ui', 'icons/*.png', 'icons/*.jpg'],
          'ilastik.applets.layerViewer': ['*.ui'],
          'ilastik.applets.objectExtraction': ['*.ui'],
          'ilastik.applets.objectExtractionMultiClass': ['*.ui'],
          'ilastik.applets.pixelClassification': ['*.ui'],
          'ilastik.applets.projectMetadata': ['*.ui'],
          'ilastik.applets.thresholdMasking': ['*.ui'],
          'ilastik.applets.tracking': ['*.ui'],          
          'ilastik.applets.tracking.base': ['*.ui'],
          'ilastik.applets.tracking.chaingraph': ['*.ui'],
          'ilastik.applets.tracking.conservation': ['*.ui'],
          'ilastik.applets.tracking.fastApproximate': ['*.ui'],
          'ilastik.applets.vigraWatershedViewer': ['*.ui'],
          'ilastik.shell.gui': ['ui/*.ui', '*.qss'],
          'ilastik.ilastik_logging': ['logging_config.json']
              }

setup(name='ilastik',
      version=__version__,
      description='Interactive Image Analysis',
      url='https://github.com/Ilastik',
      packages=packages,
      package_data=package_data
     )
