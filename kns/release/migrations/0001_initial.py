# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Release'
        db.create_table('release_release', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50, db_index=True)),
            ('appid', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('version', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=255)),
            ('released_time', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('changelog', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('release', ['Release'])


    def backwards(self, orm):
        
        # Deleting model 'Release'
        db.delete_table('release_release')


    models = {
        'release.release': {
            'Meta': {'object_name': 'Release'},
            'appid': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'changelog': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'released_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '255'}),
            'version': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['release']
