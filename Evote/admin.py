from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import (
    Candidate,
    ListInfo,
    Parameter,
    Period,
    VoteInfo,
    VoteStudent
)


@admin.register(Candidate)
class CandidateAdmin(ImportExportModelAdmin):
    list_display = (
        'student',
        'position',
        'listInfo',
    )
    list_filter = [
        "listInfo",
    ]


@admin.register(ListInfo)
class ListInfoAdmin(ImportExportModelAdmin):
    list_display = (
        'name',
        'number',
        'slogan',
        'votes'
    )
    list_filter = [
        "period",
    ]


@admin.register(Parameter)
class ParameterAdmin(ImportExportModelAdmin):
    list_display = (
        'code',
        'value',
        'description',
    )


@admin.register(Period)
class PeriodAdmin(ImportExportModelAdmin):
    list_display = ("startYear", "endYear", "periodPresent")
    search_fields = (
        "startYear",
        "endYear"
    )


@admin.register(VoteInfo)
class VoteInfoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('period', 'whiteVotes', 'nullVotes')
    list_filter = [
        "period",
    ]


@admin.register(VoteStudent)
class VoteStudentAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'student', 'period', 'created')
    list_filter = [
        "period",
    ]
    search_fields = (
        'id',
        "student__identificacion",
    )
