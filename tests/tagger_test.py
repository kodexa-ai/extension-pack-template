import os

from kodexa import Pipeline, Document
from demo_extension import TestTagger


def get_test_directory():
    return os.path.dirname(os.path.abspath(__file__)) + "/../test_documents/"


def test_test_tagger():
    filename = 'test_document.kdxa'

    pipeline = Pipeline(Document.from_kdxa(get_test_directory() + filename))
    pipeline.add_step(TestTagger("RED_TAG"))
    document = pipeline.run().output_document

    tagged_nodes = document.select('//*[hasTag("RED_TAG")]')
    assert len(tagged_nodes) == 1


