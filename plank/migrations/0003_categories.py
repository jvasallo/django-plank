# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Adding model 'Category'
        db.create_table('plank_category', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50, db_index=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('plank', ['Category'])

        # Adding field 'Service.category'
        db.add_column('plank_service',
                      'category',
                      self.gf('django.db.models.fields.related.ForeignKey')(related_name='services', null=True,
                                                                            to=orm['plank.Category']),
                      keep_default=False)

    def backwards(self, orm):

        # Deleting model 'Category'
        db.delete_table('plank_category')

        # Deleting field 'Service.category'
        db.delete_column('plank_service', 'category_id')

    models = {
        'plank.category': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Category'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'})
        },
        'plank.event': {
            'Meta': {'ordering': "('-start',)", 'object_name': 'Event'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'informational': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'message': ('django.db.models.fields.TextField', [], {}),
            'service': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'events'", 'to': "orm['plank.Service']"}),
            'start': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'status': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'events'", 'to': "orm['plank.Status']"})
        },
        'plank.service': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Service'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'services'", 'null': 'True', 'to': "orm['plank.Category']"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'})
        },
        'plank.status': {
            'Meta': {'ordering': "('severity',)", 'object_name': 'Status'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'severity': ('django.db.models.fields.IntegerField', [], {}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'})
        }
    }

    complete_apps = ['plank']
