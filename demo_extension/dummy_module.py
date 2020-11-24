from kodexa import Document, PipelineContext, TableDataStore
import logging

logger = logging.getLogger('demo_extension')

class TestTagger:
        
    def __init__(self, tag_to_apply:str):
        self.tag_to_apply = tag_to_apply
    
    def get_name(self):
        return "DemoAction"
    
    def process(self, document, context):
        
        logger.info('TestTagger process method...')
        logger.info(f'The tag_to_apply value is: {self.tag_to_apply}')

        # this selector applies the regex .*apple.* to the content of each node
        apple_nodes = document.select('//*[contentRegex(".*apple.*")]')

        # we will tag each node selected by our selector with the value provided on tag_to_apply
        for n in apple_nodes:
            n.tag(self.tag_to_apply)

        # actions must always return a document
        return document