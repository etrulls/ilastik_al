from lazyflow.graph import Graph, OperatorWrapper

from ilastik.workflow import Workflow

from ilastik.applets.dataSelection import DataSelectionApplet
from ilastik.applets.objectExtraction import ObjectExtractionApplet
from lazyflow.operators.obsolete.valueProviders import OpAttributeSelector
from ilastik.applets.tracking.chaingraph.chaingraphTrackingApplet import ChaingraphTrackingApplet


class ChaingraphTrackingWorkflow( Workflow ):
    def __init__( self ):
        # Create a graph to be shared by all operators
        graph = Graph()
        
        super(ChaingraphTrackingWorkflow, self).__init__(graph=graph)
        
        self._applets = []
        self._imageNameListSlot = None

        ######################
        # Interactive workflow
        ######################
        
        ## Create applets 
        self.dataSelectionApplet = DataSelectionApplet(self, "Input Segmentation", "Input Segmentation", batchDataGui=False)

        self.objectExtractionApplet = ObjectExtractionApplet( self )
        self.trackingApplet = ChaingraphTrackingApplet( self )

        ## Access applet operators
        opData = self.dataSelectionApplet.topLevelOperator
        opObjExtraction = self.objectExtractionApplet.topLevelOperator
        opTracking = self.trackingApplet.topLevelOperator
        
        ## Connect operators ##
        opObjExtraction.BinaryImage.connect( opData.Image )                
        
        opTracking.LabelImage.connect( opObjExtraction.LabelImage )
        opTracking.ObjectFeatures.connect( opObjExtraction.RegionFeatures )

        self._applets.append(self.dataSelectionApplet)
        self._applets.append(self.objectExtractionApplet)
        self._applets.append(self.trackingApplet)

        # The shell needs a slot from which he can read the list of image names to switch between.
        # Use an OpAttributeSelector to create a slot containing just the filename from the OpDataSelection's DatasetInfo slot.
        opSelectFilename = OperatorWrapper( OpAttributeSelector, parent=self )
        opSelectFilename.InputObject.connect( opData.Dataset )
        opSelectFilename.AttributeName.setValue( 'filePath' )

        self._imageNameListSlot = opSelectFilename.Result

    @property
    def applets(self):
        return self._applets

    @property
    def imageNameListSlot(self):
        return self._imageNameListSlot
    