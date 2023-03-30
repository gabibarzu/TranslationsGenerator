DECLARE @LanguageIdForEN INT = 1
DECLARE @LanguageIdForNL INT = 2
DECLARE @Area VARCHAR(50)
DECLARE @ResourceKey VARCHAR(50)

SET @Area = 'Area'

SET @ResourceKey = '[lbl_Decription1]'
EXEC InsertResourceItem @Area, @ResourceKey, 'Description 1'
EXEC InsertOrUpdateResourceTranslation @LanguageIdForEN, @Area, @ResourceKey, 'English Translation 1'
EXEC InsertOrUpdateResourceTranslation @LanguageIdForNL, @Area, @ResourceKey, 'Duth translation 1'

SET @ResourceKey = '[lbl_Decription1]'
EXEC InsertResourceItem @Area, @ResourceKey, 'Description 2'
EXEC InsertOrUpdateResourceTranslation @LanguageIdForEN, @Area, @ResourceKey, 'English Translation 2'
EXEC InsertOrUpdateResourceTranslation @LanguageIdForNL, @Area, @ResourceKey, 'Duth translation 2'

SET @ResourceKey = '[lbl_Decription1]'
EXEC InsertResourceItem @Area, @ResourceKey, 'Description 3'
EXEC InsertOrUpdateResourceTranslation @LanguageIdForEN, @Area, @ResourceKey, 'English Translation 3'
EXEC InsertOrUpdateResourceTranslation @LanguageIdForNL, @Area, @ResourceKey, 'Duth translation 3'

