# Type hint
# age: int
# name: str
# test: bool


def canDrive(age: int) -> bool:
    if age > 18:
        can_drive = True
    else:
        can_drive = False
    return can_drive


print(canDrive(18))