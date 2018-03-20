from ambition_rando.tests import AmbitionTestCaseMixin
from django.test import TestCase, tag
from django.test.utils import override_settings
from edc_sync.tests import SyncTestHelper
from model_mommy import mommy
from edc_sync.models import OutgoingTransaction


@tag('sync')
@override_settings(SITE_ID='10')
class TestNaturalKey(AmbitionTestCaseMixin, TestCase):

    sync_test_helper = SyncTestHelper()

    def test_natural_key_attrs(self):
        self.sync_test_helper.sync_test_natural_key_attr('ambition_screening')

    def test_get_by_natural_key_attr(self):
        self.sync_test_helper.sync_test_get_by_natural_key_attr(
            'ambition_screening')

    def test_deserialize_subject_screening(self):
        ambition_screening = mommy.make_recipe(
            'ambition_screening.subjectscreening')
        outgoing_transaction = OutgoingTransaction.objects.get(
            tx_name=ambition_screening._meta.label_lower)
        self.sync_test_helper.sync_test_deserialize(
            ambition_screening, outgoing_transaction)
