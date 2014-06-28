from django.contrib import admin
from library_internal.models import *

class LibCbDbAdmin(admin.ModelAdmin):
    list_display = LibCbDb._meta.get_all_field_names()

admin.site.register(LibCbDb, LibCbDbAdmin)

class LibCbDb_DE_FU_BENGAdmin(admin.ModelAdmin):
    list_display = LibCbDb_DE_FU_BENG._meta.get_all_field_names()

admin.site.register(LibCbDb_DE_FU_BENG, LibCbDb_DE_FU_BENGAdmin)

class LibCcdDbAdmin(admin.ModelAdmin):
    list_display = LibCcdDb._meta.get_all_field_names()

admin.site.register(LibCcdDb, LibCcdDbAdmin)

class LibCcdDb1Admin(admin.ModelAdmin):
    list_display = LibCcdDb1._meta.get_all_field_names()

admin.site.register(LibCcdDb1, LibCcdDb1Admin)

class LibCdvdDbAdmin(admin.ModelAdmin):
    list_display = LibCdvdDb._meta.get_all_field_names()

admin.site.register(LibCdvdDb, LibCdvdDbAdmin)

class LibCtDbAdmin(admin.ModelAdmin):
    list_display = LibCtDb._meta.get_all_field_names()

admin.site.register(LibCtDb, LibCtDbAdmin)

class LibCtDb1Admin(admin.ModelAdmin):
    list_display = LibCtDb1._meta.get_all_field_names()

admin.site.register(LibCtDb1, LibCtDb1Admin)

class LibCvDbAdmin(admin.ModelAdmin):
    list_display = LibCvDb._meta.get_all_field_names()

admin.site.register(LibCvDb, LibCvDbAdmin)

class LibCvDb1Admin(admin.ModelAdmin):
    list_display = LibCvDb1._meta.get_all_field_names()

admin.site.register(LibCvDb1, LibCvDb1Admin)

class LibChoirDbAdmin(admin.ModelAdmin):
    list_display = LibChoirDb._meta.get_all_field_names()

admin.site.register(LibChoirDb, LibChoirDbAdmin)

class LibChoirDb1Admin(admin.ModelAdmin):
    list_display = LibChoirDb1._meta.get_all_field_names()

admin.site.register(LibChoirDb1, LibChoirDb1Admin)

class LibClassnumberlookuptableAdmin(admin.ModelAdmin):
    list_display = LibClassnumberlookuptable._meta.get_all_field_names()

admin.site.register(LibClassnumberlookuptable, LibClassnumberlookuptableAdmin)

class LibDummyrecordtableAdmin(admin.ModelAdmin):
    list_display = LibDummyrecordtable._meta.get_all_field_names()

admin.site.register(LibDummyrecordtable, LibDummyrecordtableAdmin)

class LibDummyrecordtable1Admin(admin.ModelAdmin):
    list_display = LibDummyrecordtable1._meta.get_all_field_names()

admin.site.register(LibDummyrecordtable1, LibDummyrecordtable1Admin)

class LibEbDbAdmin(admin.ModelAdmin):
    list_display = LibEbDb._meta.get_all_field_names()

admin.site.register(LibEbDb, LibEbDbAdmin)

class LibEbDb1Admin(admin.ModelAdmin):
    list_display = LibEbDb1._meta.get_all_field_names()

admin.site.register(LibEbDb1, LibEbDb1Admin)

class LibEbDb2Admin(admin.ModelAdmin):
    list_display = LibEbDb2._meta.get_all_field_names()

admin.site.register(LibEbDb2, LibEbDb2Admin)

class LibEcdDbAdmin(admin.ModelAdmin):
    list_display = LibEcdDb._meta.get_all_field_names()

admin.site.register(LibEcdDb, LibEcdDbAdmin)

class LibEcdDb1Admin(admin.ModelAdmin):
    list_display = LibEcdDb1._meta.get_all_field_names()

admin.site.register(LibEcdDb1, LibEcdDb1Admin)

class LibEdvdDbAdmin(admin.ModelAdmin):
    list_display = LibEdvdDb._meta.get_all_field_names()

admin.site.register(LibEdvdDb, LibEdvdDbAdmin)

class LibEtDbAdmin(admin.ModelAdmin):
    list_display = LibEtDb._meta.get_all_field_names()

admin.site.register(LibEtDb, LibEtDbAdmin)

class LibEtDb1Admin(admin.ModelAdmin):
    list_display = LibEtDb1._meta.get_all_field_names()

admin.site.register(LibEtDb1, LibEtDb1Admin)

class LibEvDbAdmin(admin.ModelAdmin):
    list_display = LibEvDb._meta.get_all_field_names()

admin.site.register(LibEvDb, LibEvDbAdmin)

class LibEvDb1Admin(admin.ModelAdmin):
    list_display = LibEvDb1._meta.get_all_field_names()

admin.site.register(LibEvDb1, LibEvDb1Admin)

class LibGeneralPurposeLabelAdmin(admin.ModelAdmin):
    list_display = LibGeneralPurposeLabel._meta.get_all_field_names()

admin.site.register(LibGeneralPurposeLabel, LibGeneralPurposeLabelAdmin)

class LibGeneralPurposeLabel1Admin(admin.ModelAdmin):
    list_display = LibGeneralPurposeLabel1._meta.get_all_field_names()

admin.site.register(LibGeneralPurposeLabel1, LibGeneralPurposeLabel1Admin)

class LibKcbDbAdmin(admin.ModelAdmin):
    list_display = LibKcbDb._meta.get_all_field_names()

admin.site.register(LibKcbDb, LibKcbDbAdmin)

class LibKcbDb1Admin(admin.ModelAdmin):
    list_display = LibKcbDb1._meta.get_all_field_names()

admin.site.register(LibKcbDb1, LibKcbDb1Admin)

class LibKcdvdDbAdmin(admin.ModelAdmin):
    list_display = LibKcdvdDb._meta.get_all_field_names()

admin.site.register(LibKcdvdDb, LibKcdvdDbAdmin)

class LibKctDbAdmin(admin.ModelAdmin):
    list_display = LibKctDb._meta.get_all_field_names()

admin.site.register(LibKctDb, LibKctDbAdmin)

class LibKctDb1Admin(admin.ModelAdmin):
    list_display = LibKctDb1._meta.get_all_field_names()

admin.site.register(LibKctDb1, LibKctDb1Admin)

class LibKcvDbAdmin(admin.ModelAdmin):
    list_display = LibKcvDb._meta.get_all_field_names()

admin.site.register(LibKcvDb, LibKcvDbAdmin)

class LibKcvDb1Admin(admin.ModelAdmin):
    list_display = LibKcvDb1._meta.get_all_field_names()

admin.site.register(LibKcvDb1, LibKcvDb1Admin)

class LibKebDbAdmin(admin.ModelAdmin):
    list_display = LibKebDb._meta.get_all_field_names()

admin.site.register(LibKebDb, LibKebDbAdmin)

class LibKebDb1Admin(admin.ModelAdmin):
    list_display = LibKebDb1._meta.get_all_field_names()

admin.site.register(LibKebDb1, LibKebDb1Admin)

class LibKecdDbAdmin(admin.ModelAdmin):
    list_display = LibKecdDb._meta.get_all_field_names()

admin.site.register(LibKecdDb, LibKecdDbAdmin)

class LibKecdDb1Admin(admin.ModelAdmin):
    list_display = LibKecdDb1._meta.get_all_field_names()

admin.site.register(LibKecdDb1, LibKecdDb1Admin)

class LibKedvdDbAdmin(admin.ModelAdmin):
    list_display = LibKedvdDb._meta.get_all_field_names()

admin.site.register(LibKedvdDb, LibKedvdDbAdmin)

class LibKevDbAdmin(admin.ModelAdmin):
    list_display = LibKevDb._meta.get_all_field_names()

admin.site.register(LibKevDb, LibKevDbAdmin)

class LibKevDb1Admin(admin.ModelAdmin):
    list_display = LibKevDb1._meta.get_all_field_names()

admin.site.register(LibKevDb1, LibKevDb1Admin)

class LibKeeperindextableAdmin(admin.ModelAdmin):
    list_display = LibKeeperindextable._meta.get_all_field_names()

admin.site.register(LibKeeperindextable, LibKeeperindextableAdmin)

class LibKeeperindextable1Admin(admin.ModelAdmin):
    list_display = LibKeeperindextable1._meta.get_all_field_names()

admin.site.register(LibKeeperindextable1, LibKeeperindextable1Admin)

class LibKeeperpreferencetableAdmin(admin.ModelAdmin):
    list_display = LibKeeperpreferencetable._meta.get_all_field_names()

admin.site.register(LibKeeperpreferencetable, LibKeeperpreferencetableAdmin)

class LibKeeperpreferencetable1Admin(admin.ModelAdmin):
    list_display = LibKeeperpreferencetable1._meta.get_all_field_names()

admin.site.register(LibKeeperpreferencetable1, LibKeeperpreferencetable1Admin)

class LibPre96CbDbAdmin(admin.ModelAdmin):
    list_display = LibPre96CbDb._meta.get_all_field_names()

admin.site.register(LibPre96CbDb, LibPre96CbDbAdmin)

class LibPre96CbDb1Admin(admin.ModelAdmin):
    list_display = LibPre96CbDb1._meta.get_all_field_names()

admin.site.register(LibPre96CbDb1, LibPre96CbDb1Admin)

class LibPre96EbDbAdmin(admin.ModelAdmin):
    list_display = LibPre96EbDb._meta.get_all_field_names()

admin.site.register(LibPre96EbDb, LibPre96EbDbAdmin)

class LibPre96EbDbOldAdmin(admin.ModelAdmin):
    list_display = LibPre96EbDbOld._meta.get_all_field_names()

admin.site.register(LibPre96EbDbOld, LibPre96EbDbOldAdmin)

class LibRomanpinintableAdmin(admin.ModelAdmin):
    list_display = LibRomanpinintable._meta.get_all_field_names()

admin.site.register(LibRomanpinintable, LibRomanpinintableAdmin)

class LibRomanpinintable1Admin(admin.ModelAdmin):
    list_display = LibRomanpinintable1._meta.get_all_field_names()

admin.site.register(LibRomanpinintable1, LibRomanpinintable1Admin)

class LibVbstapesAdmin(admin.ModelAdmin):
    list_display = LibVbstapes._meta.get_all_field_names()

admin.site.register(LibVbstapes, LibVbstapesAdmin)

class LibVbstapes1Admin(admin.ModelAdmin):
    list_display = LibVbstapes1._meta.get_all_field_names()

admin.site.register(LibVbstapes1, LibVbstapes1Admin)

class LibYcmDbAdmin(admin.ModelAdmin):
    list_display = LibYcmDb._meta.get_all_field_names()

admin.site.register(LibYcmDb, LibYcmDbAdmin)

class LibYcmDb1Admin(admin.ModelAdmin):
    list_display = LibYcmDb1._meta.get_all_field_names()

admin.site.register(LibYcmDb1, LibYcmDb1Admin)

class LibYcvDbAdmin(admin.ModelAdmin):
    list_display = LibYcvDb._meta.get_all_field_names()

admin.site.register(LibYcvDb, LibYcvDbAdmin)

class LibYcvDb1Admin(admin.ModelAdmin):
    list_display = LibYcvDb1._meta.get_all_field_names()

admin.site.register(LibYcvDb1, LibYcvDb1Admin)

class LibYebDbAdmin(admin.ModelAdmin):
    list_display = LibYebDb._meta.get_all_field_names()

admin.site.register(LibYebDb, LibYebDbAdmin)

class LibYevDbAdmin(admin.ModelAdmin):
    list_display = LibYevDb._meta.get_all_field_names()

admin.site.register(LibYevDb, LibYevDbAdmin)

class LibYevDb1Admin(admin.ModelAdmin):
    list_display = LibYevDb1._meta.get_all_field_names()

admin.site.register(LibYevDb1, LibYevDb1Admin)

class LibYearindextableAdmin(admin.ModelAdmin):
    list_display = LibYearindextable._meta.get_all_field_names()

admin.site.register(LibYearindextable, LibYearindextableAdmin)

class LibYearindextable1Admin(admin.ModelAdmin):
    list_display = LibYearindextable1._meta.get_all_field_names()

admin.site.register(LibYearindextable1, LibYearindextable1Admin)

class LibShuJiaBianMuAdmin(admin.ModelAdmin):
    list_display = LibShuJiaBianMu._meta.get_all_field_names()

admin.site.register(LibShuJiaBianMu, LibShuJiaBianMuAdmin)

class LibShuJiaBianMu1Admin(admin.ModelAdmin):
    list_display = LibShuJiaBianMu1._meta.get_all_field_names()

admin.site.register(LibShuJiaBianMu1, LibShuJiaBianMu1Admin)

class LibShuJiaBianMuOldAdmin(admin.ModelAdmin):
    list_display = LibShuJiaBianMuOld._meta.get_all_field_names()

admin.site.register(LibShuJiaBianMuOld, LibShuJiaBianMuOldAdmin)

class LibShuJiaBianMuOld1Admin(admin.ModelAdmin):
    list_display = LibShuJiaBianMuOld1._meta.get_all_field_names()

admin.site.register(LibShuJiaBianMuOld1, LibShuJiaBianMuOld1Admin)

class LibTieShangCuoWuAdmin(admin.ModelAdmin):
    list_display = LibTieShangCuoWu._meta.get_all_field_names()

admin.site.register(LibTieShangCuoWu, LibTieShangCuoWuAdmin)
