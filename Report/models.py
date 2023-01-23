
from django.contrib.gis.db import models


class MetroStation(models.Model):
    gid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=254, blank=True, null=True)
    descriptio = models.CharField(max_length=254, blank=True, null=True)
    timestamp = models.CharField(max_length=24, blank=True, null=True)
    begin = models.CharField(max_length=24, blank=True, null=True)
    end = models.CharField(max_length=24, blank=True, null=True)
    altitudemo = models.CharField(max_length=254, blank=True, null=True)
    tessellate = models.FloatField(blank=True, null=True)
    extrude = models.FloatField(blank=True, null=True)
    visibility = models.FloatField(blank=True, null=True)
    draworder = models.FloatField(blank=True, null=True)
    icon = models.CharField(max_length=254, blank=True, null=True)
    layer = models.CharField(max_length=254, blank=True, null=True)
    path = models.CharField(max_length=254, blank=True, null=True)
    geom = models.MultiLineStringField(srid=0, dim=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'metro station'
        app_label = 'Training.apps.TrainingConfig' 


class Package08Alignment(models.Model):
    gid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=254, blank=True, null=True)
    descriptio = models.CharField(max_length=254, blank=True, null=True)
    timestamp = models.CharField(max_length=24, blank=True, null=True)
    begin = models.CharField(max_length=24, blank=True, null=True)
    end = models.CharField(max_length=24, blank=True, null=True)
    altitudemo = models.CharField(max_length=254, blank=True, null=True)
    tessellate = models.FloatField(blank=True, null=True)
    extrude = models.FloatField(blank=True, null=True)
    visibility = models.FloatField(blank=True, null=True)
    draworder = models.FloatField(blank=True, null=True)
    icon = models.CharField(max_length=254, blank=True, null=True)
    geom = models.MultiLineStringField(dim=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'package 08 alignment'
        


class Package09Alignment(models.Model):
    gid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=254, blank=True, null=True)
    descriptio = models.CharField(max_length=254, blank=True, null=True)
    timestamp = models.CharField(max_length=24, blank=True, null=True)
    begin = models.CharField(max_length=24, blank=True, null=True)
    end = models.CharField(max_length=24, blank=True, null=True)
    altitudemo = models.CharField(max_length=254, blank=True, null=True)
    tessellate = models.FloatField(blank=True, null=True)
    extrude = models.FloatField(blank=True, null=True)
    visibility = models.FloatField(blank=True, null=True)
    draworder = models.FloatField(blank=True, null=True)
    icon = models.CharField(max_length=254, blank=True, null=True)
    geom = models.MultiLineStringField(dim=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'package 09 alignment'


class Package10Alignment(models.Model):
    gid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=254, blank=True, null=True)
    descriptio = models.CharField(max_length=254, blank=True, null=True)
    timestamp = models.CharField(max_length=24, blank=True, null=True)
    begin = models.CharField(max_length=24, blank=True, null=True)
    end = models.CharField(max_length=24, blank=True, null=True)
    altitudemo = models.CharField(max_length=254, blank=True, null=True)
    tessellate = models.FloatField(blank=True, null=True)
    extrude = models.FloatField(blank=True, null=True)
    visibility = models.FloatField(blank=True, null=True)
    draworder = models.FloatField(blank=True, null=True)
    icon = models.CharField(max_length=254, blank=True, null=True)
    geom = models.MultiLineStringField(dim=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'package 10 alignment'


class Package11Alignment(models.Model):
    gid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=254, blank=True, null=True)
    descriptio = models.CharField(max_length=254, blank=True, null=True)
    timestamp = models.CharField(max_length=24, blank=True, null=True)
    begin = models.CharField(max_length=24, blank=True, null=True)
    end = models.CharField(max_length=24, blank=True, null=True)
    altitudemo = models.CharField(max_length=254, blank=True, null=True)
    tessellate = models.FloatField(blank=True, null=True)
    extrude = models.FloatField(blank=True, null=True)
    visibility = models.FloatField(blank=True, null=True)
    draworder = models.FloatField(blank=True, null=True)
    icon = models.CharField(max_length=254, blank=True, null=True)
    geom = models.MultiLineStringField(dim=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'package 11 alignment'


class Package12Alignment(models.Model):
    gid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=254, blank=True, null=True)
    descriptio = models.CharField(max_length=254, blank=True, null=True)
    timestamp = models.CharField(max_length=24, blank=True, null=True)
    begin = models.CharField(max_length=24, blank=True, null=True)
    end = models.CharField(max_length=24, blank=True, null=True)
    altitudemo = models.CharField(max_length=254, blank=True, null=True)
    tessellate = models.FloatField(blank=True, null=True)
    extrude = models.FloatField(blank=True, null=True)
    visibility = models.FloatField(blank=True, null=True)
    draworder = models.FloatField(blank=True, null=True)
    icon = models.CharField(max_length=254, blank=True, null=True)
    geom = models.MultiLineStringField(dim=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'package 12 alignment'


class Package54Alignment(models.Model):
    gid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=254, blank=True, null=True)
    descriptio = models.CharField(max_length=254, blank=True, null=True)
    timestamp = models.CharField(max_length=24, blank=True, null=True)
    begin = models.CharField(max_length=24, blank=True, null=True)
    end = models.CharField(max_length=24, blank=True, null=True)
    altitudemo = models.CharField(max_length=254, blank=True, null=True)
    tessellate = models.FloatField(blank=True, null=True)
    extrude = models.FloatField(blank=True, null=True)
    visibility = models.FloatField(blank=True, null=True)
    draworder = models.FloatField(blank=True, null=True)
    icon = models.CharField(max_length=254, blank=True, null=True)
    geom = models.MultiLineStringField(dim=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'package 54 alignment'


class ProjectAffectedTrees(models.Model):
    gid = models.AutoField(primary_key=True)
    tree_no_field = models.CharField(db_column='tree no.', max_length=254, blank=True, null=True) 
    common_nam = models.CharField(db_column='common nam', max_length=254, blank=True, null=True) 
    botanical = models.CharField(max_length=254, blank=True, null=True)
    approx_gi = models.CharField(db_column='approx. gi', max_length=254, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    approx_he = models.CharField(db_column='approx. he', max_length=254, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    approx_ag = models.CharField(db_column='approx. ag', max_length=254, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    proposed_a = models.CharField(db_column='proposed a', max_length=254, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    condition = models.CharField(max_length=254, blank=True, null=True)
    survey_dat = models.DateField(db_column='survey dat', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    survey_tim = models.CharField(db_column='survey tim', max_length=254, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    tree_no = models.CharField(db_column='tree no', max_length=254, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    tree_name = models.CharField(db_column='tree name', max_length=254, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    girth_m_field = models.DecimalField(db_column='girth (m)', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    approx_1 = models.DecimalField(db_column='approx. _1', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    canopy_dia = models.DecimalField(db_column='canopy dia', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    conditio_1 = models.CharField(max_length=254, blank=True, null=True)
    comments = models.CharField(max_length=254, blank=True, null=True)
    address = models.CharField(max_length=254, blank=True, null=True)
    proposed_1 = models.CharField(max_length=254, blank=True, null=True)
    approx_gir = models.CharField(db_column='approx gir', max_length=254, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    approx_hei = models.CharField(db_column='approx hei', max_length=254, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    approx_age = models.CharField(db_column='approx age', max_length=254, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    field11 = models.CharField(max_length=254, blank=True, null=True)
    layer = models.CharField(max_length=254, blank=True, null=True)
    path = models.CharField(max_length=254, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'project affected trees'
