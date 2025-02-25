"""Modoboa admin signals."""

import django.dispatch

check_extra_account_form = django.dispatch.Signal() # Provides account, form
extra_account_dashboard_widgets = django.dispatch.Signal() # Provides user, account
extra_account_forms = django.dispatch.Signal() # Provides user, account
extra_admin_content = django.dispatch.Signal() # Provides user, location, currentpage
extra_domain_actions = django.dispatch.Signal() # Provides user, domain
extra_domain_dashboard_widgets = django.dispatch.Signal() # Provides user, domain
extra_domain_filters = django.dispatch.Signal()
extra_domain_forms = django.dispatch.Signal() # Provides user, domain
extra_domain_menu_entries = django.dispatch.Signal() # Provides user
extra_domain_qset_filters = django.dispatch.Signal() # Provides domfilter, extrafilters
# extra_domain_types = django.dispatch.Signal()
extra_domain_wizard_steps = django.dispatch.Signal()
get_account_form_instances = django.dispatch.Signal() # Provides user, account
get_domain_form_instances = django.dispatch.Signal() # Provides user, domain
# get_domain_tags = django.dispatch.Signal(providing_args=["domain"])
import_object = django.dispatch.Signal() # Provides objtype
use_external_recipients = django.dispatch.Signal() # Provides recipients
extra_account_identities_actions = django.dispatch.Signal() # Provides account
