# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Question'
        db.create_table(u'searchdata_question', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('dns_name', self.gf('django.db.models.fields.CharField')(max_length=200, unique=True, null=True, blank=True)),
            ('ran_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('assimilate_status', self.gf('django.db.models.fields.CharField')(max_length=45)),
            ('assimilate_error', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('remeditor_status', self.gf('django.db.models.fields.CharField')(max_length=45)),
            ('remeditor_error', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('report_status', self.gf('django.db.models.fields.CharField')(max_length=45)),
            ('report_error', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal(u'searchdata', ['Question'])


    def backwards(self, orm):
        # Deleting model 'Question'
        db.delete_table(u'searchdata_question')


    models = {
        u'searchdata.question': {
            'Meta': {'object_name': 'Question'},
            'assimilate_error': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'assimilate_status': ('django.db.models.fields.CharField', [], {'max_length': '45'}),
            'dns_name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ran_date': ('django.db.models.fields.DateTimeField', [], {}),
            'remeditor_error': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'remeditor_status': ('django.db.models.fields.CharField', [], {'max_length': '45'}),
            'report_error': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'report_status': ('django.db.models.fields.CharField', [], {'max_length': '45'})
        }
    }

    complete_apps = ['searchdata']