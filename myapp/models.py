# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Axes(models.Model):
    name = models.CharField(max_length=191)
    description = models.TextField(blank=True, null=True)
    company_id = models.PositiveIntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'axes'


class CalculModes(models.Model):
    name = models.CharField(max_length=191)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'calcul_modes'


class Companies(models.Model):
    name = models.CharField(max_length=191)
    description = models.TextField(blank=True, null=True)
    token = models.CharField(max_length=191)
    logo = models.CharField(max_length=191, blank=True, null=True)
    active = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'companies'


class CompanyUrls(models.Model):
    company_id = models.PositiveIntegerField()
    url = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'company_urls'


class Domaines(models.Model):
    axe_id = models.PositiveIntegerField()
    name = models.CharField(max_length=191)
    description = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'domaines'


class FichesActions(models.Model):
    company_id = models.PositiveIntegerField()
    axe_id = models.PositiveIntegerField()
    name = models.CharField(max_length=191)
    description = models.TextField(blank=True, null=True)
    note = models.IntegerField()
    benefices = models.TextField()
    impacts = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fiches_actions'


class Migrations(models.Model):
    migration = models.CharField(max_length=191)
    batch = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'migrations'


class PasswordResets(models.Model):
    email = models.CharField(max_length=191)
    token = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'password_resets'


class Profils(models.Model):
    name = models.CharField(max_length=191)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'profils'


class QuestionnaireVersionAxes(models.Model):
    questionnaire_version_id = models.PositiveIntegerField()
    axe_id = models.PositiveIntegerField()
    orderby = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    hide_in_graph = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'questionnaire_version_axes'


class QuestionnaireVersions(models.Model):
    questionnaire_id = models.PositiveIntegerField()
    active = models.IntegerField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'questionnaire_versions'


class Questionnaires(models.Model):
    company_id = models.PositiveIntegerField()
    name = models.CharField(max_length=191)
    description = models.TextField(blank=True, null=True)
    active = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'questionnaires'


class Questions(models.Model):
    name = models.CharField(max_length=191)
    description = models.TextField(blank=True, null=True)
    questionnaire_version_id = models.PositiveIntegerField()
    axe_id = models.PositiveIntegerField()
    domaine_id = models.PositiveIntegerField()
    orderby = models.IntegerField()
    calcul_mode_id = models.PositiveIntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'questions'


class Responses(models.Model):
    question_id = models.PositiveIntegerField()
    name = models.CharField(max_length=191)
    description = models.TextField(blank=True, null=True)
    note = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'responses'


class Temoignages(models.Model):
    company_id = models.PositiveIntegerField()
    name = models.CharField(max_length=191)
    description = models.TextField(blank=True, null=True)
    contexte = models.TextField()
    defi = models.TextField()
    defi_details = models.TextField()
    apports = models.TextField()
    difficultes = models.TextField()
    impacts_metiers = models.TextField()
    impacts_competences = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'temoignages'

    def __str__(self):
    	return str(self.name)


class UserFoResponses(models.Model):
    response_id = models.PositiveIntegerField()
    user_fo_id = models.PositiveIntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_fo_responses'


class UserFoResults(models.Model):
    user_fo_id = models.PositiveIntegerField()
    axe_id = models.PositiveIntegerField()
    note = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
