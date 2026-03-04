class ApkError(Exception):
    pass


class ApkFileNotFoundError(ApkError):
    pass


class ApkInvalidError(ApkError):
    pass


class ApkParsingError(ApkError):
    pass
