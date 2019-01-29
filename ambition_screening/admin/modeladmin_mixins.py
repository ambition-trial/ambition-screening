from django_revision.modeladmin_mixin import ModelAdminRevisionMixin
from edc_base.sites import ModelAdminSiteMixin
from edc_model_admin import (
    ModelAdminNextUrlRedirectMixin,
    ModelAdminFormInstructionsMixin,
    ModelAdminFormAutoNumberMixin,
    ModelAdminAuditFieldsMixin,
    ModelAdminReadOnlyMixin,
    ModelAdminInstitutionMixin,
    ModelAdminRedirectOnDeleteMixin,
)
from edc_metadata import NextFormGetter


class ModelAdminMixin(
    ModelAdminNextUrlRedirectMixin,
    ModelAdminFormInstructionsMixin,
    ModelAdminFormAutoNumberMixin,
    ModelAdminRevisionMixin,
    ModelAdminAuditFieldsMixin,
    ModelAdminReadOnlyMixin,
    ModelAdminInstitutionMixin,
    ModelAdminRedirectOnDeleteMixin,
    ModelAdminSiteMixin,
):

    list_per_page = 10
    date_hierarchy = "modified"
    empty_value_display = "-"
    next_form_getter_cls = NextFormGetter
