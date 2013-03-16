# -*- coding: utf-8 -*-

from datetime import datetime
from django.db import models
from django.contrib.gis.db import geomodels
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from cached_user.utils import get_non_anonymous_user


class AuditableModelMixin(object):
    """
    AuditableModel inherits from models.Model and implements the following
    fields for audit purposes:
      * created
      * modified
      * created_by
      * modified_by
    """

    created = models.DateTimeField(
        verbose_name=_('Created'),
        auto_now_add=True,
        editable=False
    )

    modified = models.DateTimeField(
        verbose_name=_('Modified'),
        auto_now=True,
        null=True,
        editable=False
    )

    created_by = models.ForeignKey(User,
        verbose_name=_('Created by'),
        related_name="%(class)s_related",
        editable=False
    )

    modified_by = models.ForeignKey(User,
        verbose_name=_('Modified by'),
        related_name="%(class)s_related_mod",
        null=True,
        editable=False
    )

    def save(self, *args, **kwargs):
        # If the object already existed, it will already have an id
        current_user = get_non_anonymous_user()
        if self.id:
            # This object is being edited, not saved, set last_edited_by
            self.modified_by = current_user
        else:
            # This is a new object, set the owner
            self.created_by = current_user
            # Save first to obtain an ID
            kwargs['force_insert'] = False

        super(AuditableModel, self).save(*args, **kwargs)

    class Meta:
        abstract = True
        

class AuditableManager(models.Manager):
    """
    Replacement for the default manager in AuditableModels so we only query
    for the active objects.
    """
    pass


class AuditableGeoManager(geomodels.GeoManager):
    """
    Replacement for the default manager in AuditableModels so we only query
    for the active objects.
    """
    pass


class AuditableModel(AuditableModelMixin, models.Model):
    pass


class AuditableGeoModel(AuditableModelMixin, geomodels.Model):
    pass
