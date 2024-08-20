# from flask_appbuilder import ModelView
from fab_addon_audit.views import AuditedModelView
from flask_appbuilder.models.sqla.interface import SQLAInterface
from .models import Contact, ContactGroup


class ContactModelView(AuditedModelView):
    datamodel = SQLAInterface(Contact)

    label_columns = {"contact_group": "Contacts Group"}
    list_columns = ["name", "personal_cellphone", "birthday", "email", "contact_group"]

    show_fieldsets = [
        ("Summary", {"fields": ["name", "address", "contact_group"]}),
        (
            "Personal Info",
            {
                "fields": ["birthday", "email", "personal_phone", "personal_cellphone"],
                "expanded": False,
            },
        ),
    ]


class GroupModelView(AuditedModelView):
    datamodel = SQLAInterface(ContactGroup)
    related_views = [ContactModelView]
