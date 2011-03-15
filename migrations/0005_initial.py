# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'State'
        db.create_table('fires_state', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('name_slug', self.gf('django.db.models.fields.SlugField')(max_length=50, db_index=True)),
            ('short_name', self.gf('django.db.models.fields.CharField')(max_length=8)),
        ))
        db.send_create_signal('fires', ['State'])

        # Adding model 'City'
        db.create_table('fires_city', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('name_slug', self.gf('django.db.models.fields.SlugField')(max_length=50, db_index=True)),
            ('state', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['fires.State'])),
        ))
        db.send_create_signal('fires', ['City'])

        # Adding model 'Title'
        db.create_table('fires_title', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('title_slug', self.gf('django.db.models.fields.SlugField')(max_length=50, db_index=True)),
        ))
        db.send_create_signal('fires', ['Title'])

        # Adding model 'Person'
        db.create_table('fires_person', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('name_slug', self.gf('django.db.models.fields.SlugField')(max_length=50, db_index=True)),
            ('dob', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('title', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['fires.Title'], null=True, blank=True)),
            ('experience', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('fires', ['Person'])

        # Adding model 'Address'
        db.create_table('fires_address', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('street', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('city', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['fires.City'])),
            ('property_value', self.gf('django.db.models.fields.IntegerField')(max_length=12, null=True, blank=True)),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['fires.Person'], null=True, blank=True)),
        ))
        db.send_create_signal('fires', ['Address'])

        # Adding model 'Department'
        db.create_table('fires_department', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('name_slug', self.gf('django.db.models.fields.SlugField')(max_length=50, db_index=True)),
            ('short_name', self.gf('django.db.models.fields.CharField')(max_length=15)),
        ))
        db.send_create_signal('fires', ['Department'])

        # Adding model 'Station'
        db.create_table('fires_station', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('name_slug', self.gf('django.db.models.fields.SlugField')(max_length=50, db_index=True)),
            ('address', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['fires.Address'])),
        ))
        db.send_create_signal('fires', ['Station'])

        # Adding model 'StoryLink'
        db.create_table('fires_storylink', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('link', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('headline', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
        ))
        db.send_create_signal('fires', ['StoryLink'])

        # Adding model 'Injury'
        db.create_table('fires_injury', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('injury', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('injury_slug', self.gf('django.db.models.fields.SlugField')(max_length=50, db_index=True)),
        ))
        db.send_create_signal('fires', ['Injury'])

        # Adding model 'Victim'
        db.create_table('fires_victim', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('person', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['fires.Person'])),
            ('injury', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['fires.Injury'])),
        ))
        db.send_create_signal('fires', ['Victim'])

        # Adding model 'Cause'
        db.create_table('fires_cause', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('type_slug', self.gf('django.db.models.fields.SlugField')(max_length=50, db_index=True)),
        ))
        db.send_create_signal('fires', ['Cause'])

        # Adding model 'Fire'
        db.create_table('fires_fire', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('location', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['fires.Address'])),
            ('cause', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['fires.Cause'], null=True, blank=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('monetary_damage', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('response_time', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('extinguish_time', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
        ))
        db.send_create_signal('fires', ['Fire'])

        # Adding M2M table for field responding on 'Fire'
        db.create_table('fires_fire_responding', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('fire', models.ForeignKey(orm['fires.fire'], null=False)),
            ('station', models.ForeignKey(orm['fires.station'], null=False))
        ))
        db.create_unique('fires_fire_responding', ['fire_id', 'station_id'])

        # Adding M2M table for field story_link on 'Fire'
        db.create_table('fires_fire_story_link', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('fire', models.ForeignKey(orm['fires.fire'], null=False)),
            ('storylink', models.ForeignKey(orm['fires.storylink'], null=False))
        ))
        db.create_unique('fires_fire_story_link', ['fire_id', 'storylink_id'])

        # Adding M2M table for field victim on 'Fire'
        db.create_table('fires_fire_victim', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('fire', models.ForeignKey(orm['fires.fire'], null=False)),
            ('victim', models.ForeignKey(orm['fires.victim'], null=False))
        ))
        db.create_unique('fires_fire_victim', ['fire_id', 'victim_id'])

        # Adding M2M table for field source on 'Fire'
        db.create_table('fires_fire_source', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('fire', models.ForeignKey(orm['fires.fire'], null=False)),
            ('person', models.ForeignKey(orm['fires.person'], null=False))
        ))
        db.create_unique('fires_fire_source', ['fire_id', 'person_id'])


    def backwards(self, orm):
        
        # Deleting model 'State'
        db.delete_table('fires_state')

        # Deleting model 'City'
        db.delete_table('fires_city')

        # Deleting model 'Title'
        db.delete_table('fires_title')

        # Deleting model 'Person'
        db.delete_table('fires_person')

        # Deleting model 'Address'
        db.delete_table('fires_address')

        # Deleting model 'Department'
        db.delete_table('fires_department')

        # Deleting model 'Station'
        db.delete_table('fires_station')

        # Deleting model 'StoryLink'
        db.delete_table('fires_storylink')

        # Deleting model 'Injury'
        db.delete_table('fires_injury')

        # Deleting model 'Victim'
        db.delete_table('fires_victim')

        # Deleting model 'Cause'
        db.delete_table('fires_cause')

        # Deleting model 'Fire'
        db.delete_table('fires_fire')

        # Removing M2M table for field responding on 'Fire'
        db.delete_table('fires_fire_responding')

        # Removing M2M table for field story_link on 'Fire'
        db.delete_table('fires_fire_story_link')

        # Removing M2M table for field victim on 'Fire'
        db.delete_table('fires_fire_victim')

        # Removing M2M table for field source on 'Fire'
        db.delete_table('fires_fire_source')


    models = {
        'fires.address': {
            'Meta': {'object_name': 'Address'},
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['fires.City']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['fires.Person']", 'null': 'True', 'blank': 'True'}),
            'property_value': ('django.db.models.fields.IntegerField', [], {'max_length': '12', 'null': 'True', 'blank': 'True'}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': '150'})
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
            'source': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['fires.Person']", 'null': 'True', 'blank': 'True'}),
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
