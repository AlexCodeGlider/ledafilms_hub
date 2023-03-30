from django.db import models

class Contracts(models.Model):
    CONTRACT_TYPE_CHOICES = (
        ('Sales', 'Sales'),
        ('Acquisition', 'Acquisition'),
    )
    
    STATUS_CHOICES = (
        ('Normal', 'Normal'),
        ('Internal', 'Internal'),
        ('Cancelled', 'Cancelled'),
    )
    
    DEAL_STATUS_CHOICES = (
        ('Long Form Executed', 'Long Form Executed'),
        ('In Negotiation', 'In Negotiation'),
        ('Deal Memo Executed', 'Deal Memo Executed'),
        ('Cancelled', 'Cancelled'),
    )
    
    DEAL_TYPE_CHOICES = (
        ('Flat Fee', 'Flat Fee'),
        ('[Royalties/Revenue Share]', '[Royalties/Revenue Share]'),
        ('Minimum Guarantee', 'Minimum Guarantee'),
        ('Straight Distribution', 'Straight Distribution'),
        ('[MG] [++MG]', '[MG] [++MG]'),
        ('Production / License Agrmnt', 'Production / License Agrmnt'),
        ('Volume Deal', 'Volume Deal'),
        ('Co-Production', 'Co-Production'),
        ('Output Agrmnt', 'Output Agrmnt'),
    )
    
    contract_code = models.CharField(max_length=255, blank=True, null=True)
    contract_type = models.CharField(max_length=255, choices=CONTRACT_TYPE_CHOICES)
    licensor = models.CharField(max_length=255)
    distributor = models.CharField(max_length=255)
    status = models.CharField(max_length=255, choices=STATUS_CHOICES)
    deal_status = models.CharField(max_length=255, choices=DEAL_STATUS_CHOICES)
    creation_date = models.DateField(blank=True, null=True)
    deal_type = models.CharField(max_length=255, choices=DEAL_TYPE_CHOICES)
    fully_executed = models.DateField(blank=True, null=True)
    mg = models.FloatField(blank=True, null=True)
    cur = models.CharField(max_length=255, blank=True, null=True)
    additional_terms = models.CharField(max_length=50000, blank=True, null=True)
    contract = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'contracts'


class Countries(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    continent = models.CharField(max_length=255, blank=True, null=True)
    region = models.CharField(max_length=255, blank=True, null=True)
    country = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'countries'


class People(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    person = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'people'


class Rights(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    group = models.CharField(max_length=255, blank=True, null=True)
    right = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'rights'


class Roles(models.Model):
    title = models.ForeignKey('Titles', models.DO_NOTHING, db_column='title', blank=True, null=True)
    role = models.CharField(max_length=255, blank=True, null=True)
    person = models.ForeignKey(People, models.DO_NOTHING, db_column='person', blank=True, null=True)
    row = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'roles'


class Titles(models.Model):
    title = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    aka_1 = models.CharField(max_length=255, blank=True, null=True)
    aka_2 = models.CharField(max_length=255, blank=True, null=True)
    adj_running_time = models.CharField(max_length=255, blank=True, null=True)
    copyright_holder = models.CharField(max_length=255, blank=True, null=True)
    copyright_year = models.CharField(max_length=255, blank=True, null=True)
    country_of_origin = models.CharField(max_length=255, blank=True, null=True)
    dialogue_language = models.CharField(max_length=255, blank=True, null=True)
    external_comments = models.CharField(max_length=255, blank=True, null=True)
    genre = models.CharField(max_length=255, blank=True, null=True)
    imdb_code = models.CharField(max_length=255, blank=True, null=True)
    internal_comments = models.CharField(max_length=255, blank=True, null=True)
    logline = models.CharField(max_length=255, blank=True, null=True)
    motion_picture_association_of_america = models.CharField(max_length=255, blank=True, null=True)
    number_of_episodes = models.IntegerField(blank=True, null=True)
    number_of_seasons = models.IntegerField(blank=True, null=True)
    original_format = models.CharField(max_length=255, blank=True, null=True)
    original_language = models.CharField(max_length=255, blank=True, null=True)
    production_company = models.CharField(max_length=255, blank=True, null=True)
    project_code = models.CharField(max_length=255, blank=True, null=True)
    project_group = models.CharField(max_length=255, blank=True, null=True)
    project_type = models.CharField(max_length=255, blank=True, null=True)
    rating = models.CharField(max_length=255, blank=True, null=True)
    running_time = models.CharField(max_length=255, blank=True, null=True)
    sales_agency = models.CharField(max_length=255, blank=True, null=True)
    season = models.FloatField(blank=True, null=True)
    short_synopsis = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    subtitle_language = models.CharField(max_length=255, blank=True, null=True)
    synopsis = models.CharField(max_length=50000, blank=True, null=True)
    title_code = models.CharField(max_length=255, blank=True, null=True)
    website = models.CharField(max_length=255, blank=True, null=True)
    year_completed = models.FloatField(blank=True, null=True)
    web_site = models.CharField(max_length=255, blank=True, null=True)
    link = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    us_box_office = models.CharField(max_length=255, blank=True, null=True)
    latam_box_office = models.CharField(max_length=255, blank=True, null=True)
    imdb_link = models.CharField(max_length=255, blank=True, null=True)
    rating_usa = models.CharField(max_length=255, blank=True, null=True)
    rating_mexico = models.CharField(max_length=255, blank=True, null=True)
    rating_brazil = models.CharField(max_length=255, blank=True, null=True)
    rating_argentina = models.CharField(max_length=255, blank=True, null=True)
    rating_bolivia = models.CharField(max_length=255, blank=True, null=True)
    rating_chile = models.CharField(max_length=255, blank=True, null=True)
    rating_colombia = models.CharField(max_length=255, blank=True, null=True)
    rating_costa_rica = models.CharField(max_length=255, blank=True, null=True)
    rating_ecuador = models.CharField(max_length=255, blank=True, null=True)
    rating_el_salvador = models.CharField(max_length=255, blank=True, null=True)
    rating_guatemala = models.CharField(max_length=255, blank=True, null=True)
    rating_honduras = models.CharField(max_length=255, blank=True, null=True)
    rating_nicaragua = models.CharField(max_length=255, blank=True, null=True)
    rating_panama = models.CharField(max_length=255, blank=True, null=True)
    rating_paraguay = models.CharField(max_length=255, blank=True, null=True)
    rating_peru = models.CharField(max_length=255, blank=True, null=True)
    rating_dominican_republic = models.CharField(max_length=255, blank=True, null=True)
    rating_uruguay = models.CharField(max_length=255, blank=True, null=True)
    rating_venezuela = models.CharField(max_length=255, blank=True, null=True)
    imdb = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'titles'


class Windows(models.Model):
    LICENSE_TYPE_CHOICES = (
        ('License', 'License'),
        ('Non-Exclusive', 'Non-Exclusive'),
        ('Holdback', 'Holdback'),
    )

    start_date = models.DateField()
    end_date = models.DateField()
    license_type = models.CharField(max_length=255, choices=LICENSE_TYPE_CHOICES)
    start_confirmed = models.BooleanField(db_column='Start Confirmed')  # Field renamed to remove unsuitable characters.
    end_confirmed = models.BooleanField(db_column='End Confirmed')  # Field renamed to remove unsuitable characters.
    title = models.ForeignKey(Titles, models.DO_NOTHING, db_column='title')
    window = models.IntegerField(primary_key=True)
    contract = models.ForeignKey(Contracts, models.DO_NOTHING, db_column='contract')
    country = models.ForeignKey(Countries, models.DO_NOTHING, db_column='country')
    right = models.ForeignKey(Rights, models.DO_NOTHING, db_column='right')

    class Meta:
        managed = False
        db_table = 'windows'