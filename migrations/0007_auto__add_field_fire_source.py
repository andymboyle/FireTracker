# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Fire.source'
        db.add_column('fires_fire', 'source', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['fires.Person'], null=True, blank=True), keep_default=False)

        # Removing M2M table for field source on 'Fire'
        db.delete_table('fires_fire_source')


    def backwards(self, orm):
        
        # Deleting field 'Fire.source'
        db.delete_column('fires_fire', 'source_id')

        # Adding M2M table for field source on 'Fire'
        db.create_table('fires_fire_source', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('fire', models.ForeignKey(orm['fires.fire'], null=False)),
            ('person', models.ForeignKey(orm['fires.person'], null=False))
        ))
        db.create_unique('fires_fire_source', ['fire_id', 'person_id'])


    models = {
        'fires.address': {
            'Meta': {'object_name': 'Address'},
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['fires.City']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['fires.Person']", 'null': 'True', 'blank': 'True'}),
            'property_value': ('django.db.models.fields.IntegerField', [], {'max_length': '12', 'null': 'True', 'blank': 'True'}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'street_slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'})
        },
        'fires.cause': {
            'Meta': {'object_name': 'Cause'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'type_slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'})
        },
        'fires.city': {
            'Meta': {'object_name': 'City'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'name_slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
            'state': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['fires.State']"})
        },
        'fires.department': {
            'Meta': {'object_name': 'Department'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'name_slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
            'short_name': ('django.db.models.fields.CharField', [], {'max_length': '15'})
        },
        'fires.fire': {
            'Meta': {'object_name': 'Fire'},
            'cause': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['fires.Cause']", 'null': 'True', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'extinguish_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['fires.Address']"}),
            'monetary_damage': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'responding': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['fires.Station']", 'null': 'True', 'blank': 'True'}),
            'response_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'source': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['fires.Person']", 'null': 'True', 'blank': 'True'}),
            'story_link': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['fires.StoryLink']", 'null': 'True', 'blank': 'True'}),
            'victim': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['fires.Victim']", 'null': 'True', 'blank': 'True'})
        },
        'fires.injury': {
            'Meta': {'object_name': 'Injury'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'injury': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'injury_slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'})
        },
        'fires.person': {
            'Meta': {'object_name': 'Person'},
            'dob': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'experience': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'name_slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
            'title': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['fires.Title']", 'null': 'True', 'blank': 'True'})
        },
        'fires.source': {
            'Meta': {'object_name': 'Source'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'source': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['fires.Person']"})
        },
        'fires.state': {
            'Meta': {'object_name': 'State'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'name_slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
            'short_name': ('django.db.models.fields.CharField', [], {'max_length': '8'})
        },
        'fires.station': {
            'Meta': {'object_name': 'Station'},
            'address': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['fires.Address']"}),
            'department': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['fires.Department']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'name_slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'})
        },
        'fires.storylink': {
            'Meta': {'object_name': 'StoryLink'},
            'date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'headline': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        'fires.title': {
            'Meta': {'object_name': 'Title'},
            'employer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['fires.Department']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'title_slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'})
        },
        'fires.victim': {
            'Meta': {'object_name': 'Victim'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'injury': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['fires.Injury']"}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['fires.Person']"})
        }
    }

    complete_apps = ['fires']
